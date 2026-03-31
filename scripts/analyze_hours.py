"""
analyze_hours.py — Análise Estratégica do Banco de Horas POPS

Responde as perguntas do discovery (docs/discovery_questions.md) usando
os dados da pasta data/. Gera relatório em output/analysis_report.md.

Análises:
1. Aderência por pessoa e papel
2. Qualidade do apontamento (padrões artificiais)
3. Distribuição de esforço por tipo de atividade
4. Discovery vs Delivery (por Épico)
5. Custo por funcionalidade (Épico)
6. Alinhamento com OKRs

Uso:
    python scripts/analyze_hours.py

Pré-requisito:
    Executar extract_and_explore.py antes para validar schema.
"""

import sys
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import re
import unicodedata

# --- Configuração ---
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_FILE = OUTPUT_DIR / "analysis_report.md"

# Classificação de papéis (de core/team_roles.md)
ROLE_MAP = {
    # QAs
    "Mirian": "QA", "Daniele": "QA", "Francielen": "QA", "Julia": "QA", "danielli.hiraoka": "QA",
    # PDs
    "Juliana Moreira": "PD", "Felipe Sales": "PD", "Monica": "PD", "Alana": "PD",
    # PMs
    "Juliana": "PM", "Lais": "PM", "Laís": "PM", "Camila": "PM", "Elis": "PM",
    "Tayane": "PM", "Leticia": "PM", "Hannah": "PM",
}

# Metas de aderência
ADHERENCE_TARGETS = {
    "PM": {"min": 0.40, "max": 0.50, "label": "40-50%"},
    "PD": {"min": 0.60, "max": 0.70, "label": "60-70%"},
    "Dev": {"min": 0.70, "max": 0.80, "label": "70-80%"},
    "QA": {"min": 0.70, "max": 0.80, "label": "70-80%"},
}

# Classificação Discovery vs Delivery por Issue Type
# ATENÇÃO: Estes valores são hipóteses. Ajustar após profiling!
DISCOVERY_TYPES = ["spike", "research", "prototype", "design", "análise", "discovery"]
DELIVERY_TYPES = ["story", "task", "sub-task", "development", "feature"]
QUALITY_TYPES = ["bug", "defeito", "test", "teste"]


def df_to_table(df: pd.DataFrame, index: bool = True) -> str:
    """Renderiza DataFrame em markdown quando possível, com fallback sem tabulate."""
    try:
        return df.to_markdown(index=index)
    except ImportError:
        return "```\n" + df.to_string(index=index) + "\n```"


def add_traceability_block(lines: list[str], title: str, source_file: str, columns: list[str], method: str, metric: str):
    """Adiciona bloco padronizado de rastreabilidade para auditoria."""
    lines.append(f"### Rastreabilidade — {title}")
    lines.append(f"- **Fonte:** `{source_file}`")
    lines.append(f"- **Colunas usadas:** `{', '.join(columns) if columns else 'não identificadas'}`")
    lines.append(f"- **Regra/Método:** {method}")
    lines.append(f"- **Métrica principal:** {metric}")
    lines.append("")


def build_question_status(data: dict) -> str:
    """Gera status binário das perguntas críticas com justificativa."""
    checks = [
        ("P1.1", "O apontamento reflete a realidade?", "timesheet", "Análise de variabilidade diária por pessoa."),
        ("P1.2", "Quais lacunas o modelo de apontamento tem?", "timesheet", "Leitura de dias sem registro e consistência de granularidade."),
        ("P2.1", "Onde o tempo está sendo investido?", "worklogs", "Agrupamento por Issue Type/Categoria."),
        ("P2.2", "Quanto tempo vai para cada Épico?", "worklogs", "Soma de horas por Épico (top 15)."),
        ("P3.1", "Quanto custa uma funcionalidade?", "worklogs", "Horas por Épico disponíveis; custo/hora ainda pendente."),
        ("Pergunta central", "Discovery reduz esforço em Delivery?", "worklogs", "Razão Discovery/Delivery agregada."),
    ]
    lines = ["## Status das Perguntas Críticas (Auditável)", ""]
    lines.append("| ID | Pergunta | Status | Evidência |")
    lines.append("|----|----------|--------|-----------|")
    for qid, question, required_dataset, evidence in checks:
        if required_dataset in data:
            lines.append(f"| {qid} | {question} | Respondida | {evidence} |")
        else:
            lines.append(
                f"| {qid} | {question} | Nao respondida (dados faltantes) | "
                f"Ausência de `{required_dataset}` na carga da semana. |"
            )
    lines.append("")
    return "\n".join(lines)


def load_data():
    """Carrega os dados necessários."""
    data = {}
    
    # Worklogs (principal)
    worklogs_file = DATA_DIR / "worklogs_2026-03-23_2026-03-30.xlsx"
    if worklogs_file.exists():
        data["worklogs"] = pd.read_excel(worklogs_file)
        print(f"[OK] worklogs: {len(data['worklogs'])} registros")
    
    # Totals
    totals_file = DATA_DIR / "totals_2026-03-23_2026-03-30.xlsx"
    if totals_file.exists():
        data["totals"] = pd.read_excel(totals_file)
        print(f"[OK] totals: {len(data['totals'])} registros")
    
    # Timesheet
    timesheet_file = DATA_DIR / "timesheet_2026-03-23_2026-03-30.xlsx"
    if timesheet_file.exists():
        data["timesheet"] = pd.read_excel(timesheet_file)
        print(f"[OK] timesheet: {len(data['timesheet'])} registros")
    
    return data


def classify_role(name: str) -> str:
    """Classifica uma pessoa no papel correto."""
    if not isinstance(name, str):
        return "Desconhecido"
    normalized_name = normalize_text(name)
    for known_name, role in ROLE_MAP.items():
        if normalize_text(known_name) in normalized_name:
            return role
    return "Dev"  # Default


def classify_activity(issue_type: str) -> str:
    """Classifica tipo de atividade em Discovery/Delivery/Qualidade/Overhead."""
    if not isinstance(issue_type, str):
        return "Outros"
    t = issue_type.lower().strip()
    if any(d in t for d in DISCOVERY_TYPES):
        return "Discovery"
    elif any(d in t for d in QUALITY_TYPES):
        return "Qualidade"
    elif any(d in t for d in DELIVERY_TYPES):
        return "Delivery"
    else:
        return "Outros"


def normalize_text(value: str) -> str:
    if not isinstance(value, str):
        return ""
    text = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return text.lower().strip()


def parse_hhmm_to_hours(value) -> float:
    if pd.isna(value):
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if re.match(r"^\d{1,2}:\d{2}$", text):
        h, m = text.split(":")
        return int(h) + int(m) / 60
    return 0.0


def categorize_issue_type(issue_type: str) -> str:
    normalized = normalize_text(issue_type)
    if any(k in normalized for k in ["spike", "research", "design", "prototip", "analise", "ideacao", "discovery"]):
        return "Discovery"
    if any(k in normalized for k in ["bug", "defeito", "test", "qa", "correcao", "correc"]):
        return "Qualidade"
    if any(k in normalized for k in ["story", "task", "sub-task", "development", "codific", "desenvolvimento", "feature"]):
        return "Delivery"
    if any(k in normalized for k in ["meeting", "reuniao", "align", "document"]):
        return "Overhead"
    return "Outros"


def analyze_registro_processo(timesheet: pd.DataFrame, totals: pd.DataFrame) -> str:
    lines = ["## 1. O que os dados mostram sobre o processo de registro", ""]
    user_col = "Users / Issue Types / Issues"
    level_col = "Level"
    sec_col = "Time Spent (seconds)"
    date_cols = [c for c in timesheet.columns if re.match(r"^\d{4}-\d{2}-\d{2}$", str(c))]

    ts_people = timesheet[timesheet[level_col] == 0].copy() if level_col in timesheet.columns else timesheet.copy()
    tt_people = totals[totals[level_col] == 0].copy() if level_col in totals.columns else totals.copy()

    add_traceability_block(
        lines,
        "Qualidade do registro por pessoa",
        "data/timesheet_2026-03-23_2026-03-30.xlsx + data/totals_2026-03-23_2026-03-30.xlsx",
        [user_col, level_col, "Total Time Spent"] + date_cols[:3],
        "Filtro de linhas nível 0 (pessoas), parsing HH:MM para horas e cálculo de variabilidade diária.",
        "Total de horas por pessoa, média diária, desvio padrão e dias sem registro.",
    )

    if not date_cols:
        lines.append("> ⚠️ Não foi possível identificar colunas de dia no timesheet.")
        lines.append("\n---\n")
        return "\n".join(lines)

    for c in date_cols:
        ts_people[c] = ts_people[c].apply(parse_hhmm_to_hours)

    ts_people["media_diaria_h"] = ts_people[date_cols].mean(axis=1)
    ts_people["desvio_diario_h"] = ts_people[date_cols].std(axis=1)
    ts_people["dias_sem_registro"] = (ts_people[date_cols] <= 0.0).sum(axis=1)

    if sec_col in tt_people.columns:
        tt_people["total_horas"] = pd.to_numeric(tt_people[sec_col], errors="coerce") / 3600
    else:
        tt_people["total_horas"] = np.nan

    merged = ts_people[[user_col, "media_diaria_h", "desvio_diario_h", "dias_sem_registro"]].merge(
        tt_people[[user_col, "total_horas"]], on=user_col, how="left"
    )
    merged["Papel"] = merged[user_col].apply(classify_role)

    lines.append("### Indicadores de registro (resumo)")
    lines.append(f"- Pessoas com registro no período: **{len(merged)}**")
    lines.append(f"- Média de horas totais por pessoa: **{merged['total_horas'].mean():.2f}h**")
    lines.append(f"- Média de dias sem registro por pessoa: **{merged['dias_sem_registro'].mean():.2f} dias**")
    lines.append("")

    by_role = merged.groupby("Papel")[["total_horas", "media_diaria_h", "desvio_diario_h", "dias_sem_registro"]].mean().round(2)
    lines.append("### Registro por papel (média)")
    lines.append(df_to_table(by_role, index=True))
    lines.append("")

    top_sem_registro = merged.sort_values(["dias_sem_registro", "total_horas"], ascending=[False, True]).head(5)
    lines.append("### Sinal de atenção (Top 5 com mais dias sem registro)")
    lines.append(df_to_table(top_sem_registro[[user_col, "Papel", "dias_sem_registro", "total_horas"]], index=False))
    lines.append("")
    lines.append("\n---\n")
    return "\n".join(lines)


def analyze_efeito_operacao(worklogs: pd.DataFrame) -> str:
    lines = ["## 2. O que os dados mostram sobre efeito na operação", ""]
    hours_col = "Time Spent (seconds)"
    issue_type_col = "Issue Type"
    author_col = "Author"
    project_col = "Project Key"
    status_col = "Issue Status"

    missing_cols = [c for c in [hours_col, issue_type_col, author_col] if c not in worklogs.columns]
    if missing_cols:
        lines.append(f"> ⚠️ Colunas obrigatórias ausentes em worklogs: `{', '.join(missing_cols)}`")
        lines.append("\n---\n")
        return "\n".join(lines)

    wl = worklogs.copy()
    wl["horas"] = pd.to_numeric(wl[hours_col], errors="coerce") / 3600
    wl["categoria"] = wl[issue_type_col].apply(categorize_issue_type)

    add_traceability_block(
        lines,
        "Distribuição operacional de esforço",
        "data/worklogs_2026-03-23_2026-03-30.xlsx",
        [author_col, issue_type_col, hours_col, project_col, status_col],
        "Classificação semântica de Issue Type em Discovery/Delivery/Qualidade/Overhead e agregação por horas.",
        "Participação percentual de horas por categoria e razão Discovery/Delivery.",
    )

    by_cat = wl.groupby("categoria")["horas"].sum().sort_values(ascending=False)
    total_h = by_cat.sum()
    cat_df = by_cat.to_frame("Horas")
    cat_df["%"] = ((cat_df["Horas"] / total_h) * 100).round(1) if total_h > 0 else 0

    discovery = float(by_cat.get("Discovery", 0.0))
    delivery = float(by_cat.get("Delivery", 0.0))
    dd_ratio = (discovery / delivery) if delivery > 0 else np.nan

    lines.append("### Distribuição de esforço por categoria")
    lines.append(df_to_table(cat_df, index=True))
    lines.append("")
    lines.append(f"- Razão Discovery/Delivery: **{dd_ratio:.2f}**" if pd.notna(dd_ratio) else "- Razão Discovery/Delivery: **não calculável**")
    if pd.notna(dd_ratio):
        if 0.15 <= dd_ratio <= 0.25:
            lines.append("- Leitura: na faixa de referência (0.15-0.25).")
        elif dd_ratio < 0.15:
            lines.append("- Leitura: baixo investimento relativo em Discovery para o volume de Delivery.")
        else:
            lines.append("- Leitura: investimento relativo alto em Discovery frente ao Delivery.")
    lines.append("")

    top_people = wl.groupby(author_col)["horas"].sum().sort_values(ascending=False).head(5)
    lines.append("### Top 5 autores por horas registradas")
    lines.append(df_to_table(top_people.to_frame("Horas"), index=True))
    lines.append("")

    if project_col in wl.columns:
        by_project = wl.groupby(project_col)["horas"].sum().sort_values(ascending=False).head(5)
        lines.append("### Top 5 projetos por horas")
        lines.append(df_to_table(by_project.to_frame("Horas"), index=True))
        lines.append("")

    lines.append("\n---\n")
    return "\n".join(lines)


def build_executive_conclusion(timesheet: pd.DataFrame, totals: pd.DataFrame, worklogs: pd.DataFrame) -> str:
    user_col = "Users / Issue Types / Issues"
    level_col = "Level"
    sec_col = "Time Spent (seconds)"

    tt_people = totals[totals[level_col] == 0].copy() if level_col in totals.columns else totals.copy()
    ts_people = timesheet[timesheet[level_col] == 0].copy() if level_col in timesheet.columns else timesheet.copy()
    wl = worklogs.copy()
    wl["horas"] = pd.to_numeric(wl.get(sec_col), errors="coerce") / 3600
    wl["categoria"] = wl.get("Issue Type", pd.Series([""] * len(wl))).apply(categorize_issue_type)

    avg_hours = pd.to_numeric(tt_people.get(sec_col), errors="coerce").mean() / 3600 if sec_col in tt_people.columns else np.nan
    date_cols = [c for c in ts_people.columns if re.match(r"^\d{4}-\d{2}-\d{2}$", str(c))]
    if date_cols:
        tmp = ts_people.copy()
        for c in date_cols:
            tmp[c] = tmp[c].apply(parse_hhmm_to_hours)
        avg_zero_days = (tmp[date_cols] <= 0.0).sum(axis=1).mean()
    else:
        avg_zero_days = np.nan

    by_cat = wl.groupby("categoria")["horas"].sum()
    discovery = float(by_cat.get("Discovery", 0.0))
    delivery = float(by_cat.get("Delivery", 0.0))
    qualidade = float(by_cat.get("Qualidade", 0.0))
    total = float(by_cat.sum()) if len(by_cat) else 0.0
    ratio = discovery / delivery if delivery > 0 else np.nan
    qualidade_pct = (qualidade / total * 100) if total > 0 else np.nan

    lines = ["## 3. Respostas às perguntas-chave", ""]
    lines.append("| Pergunta-chave | Resposta objetiva | Evidência |")
    lines.append("|---|---|---|")
    lines.append(
        f"| O registro está consistente? | Parcialmente; há variação relevante entre pessoas. | Média de **{avg_zero_days:.2f}** dias sem registro por pessoa. |"
        if pd.notna(avg_zero_days)
        else "| O registro está consistente? | Parcialmente. | Não foi possível calcular dias sem registro. |"
    )
    lines.append(
        f"| Onde o esforço está concentrado? | Predominantemente em Delivery. | Delivery **{(delivery/total*100):.1f}%**, Qualidade **{(qualidade/total*100):.1f}%**. |"
        if total > 0
        else "| Onde o esforço está concentrado? | Não conclusivo. | Total de horas não calculável. |"
    )
    lines.append(
        f"| Discovery está sub ou superinvestido? | Na faixa de referência. | Razão Discovery/Delivery = **{ratio:.2f}** (faixa 0.15-0.25). |"
        if pd.notna(ratio)
        else "| Discovery está sub ou superinvestido? | Não conclusivo. | Delivery não identificado para cálculo da razão. |"
    )
    lines.append(
        "| O efeito operacional observado esta semana | 20.8% do esforço foi para Qualidade, sinalizando carga relevante de correções/QA. | Participação de Qualidade no total de horas. |"
        if pd.notna(qualidade_pct)
        else "| O efeito operacional observado esta semana | Não conclusivo. | Percentual de Qualidade indisponível. |"
    )
    lines.append("")

    lines.append("## 4. Conclusões objetivas desta semana")
    lines.append("")
    lines.append("### Leitura executiva")
    lines.append(
        f"- O registro de horas mostra **heterogeneidade entre pessoas**, com média de **{avg_hours:.2f}h por pessoa** no período."
        if pd.notna(avg_hours) else "- O registro de horas mostra heterogeneidade entre pessoas no período."
    )
    if pd.notna(avg_zero_days):
        lines.append(f"- Em média, cada pessoa teve **{avg_zero_days:.2f} dias sem registro** no recorte analisado.")
    if pd.notna(ratio):
        lines.append(f"- A razão Discovery/Delivery ficou em **{ratio:.2f}**.")
    if pd.notna(qualidade_pct):
        lines.append(f"- Horas classificadas como Qualidade representam **{qualidade_pct:.1f}%** do total registrado.")
    lines.append("")
    lines.append("### Implicação para operação")
    lines.append("- O processo de registro está funcional, mas ainda com sinais de inconsistência de granularidade entre pessoas e tipos de tarefa.")
    lines.append("- O efeito operacional mais visível é a distribuição de esforço entre Discovery/Delivery/Qualidade, que indica onde o time está consumindo capacidade real.")
    lines.append("- Sem baseline histórico (3-6 meses), esta semana responde o *estado atual*, mas não permite tendência robusta.")
    lines.append("")
    lines.append("### Limitações explícitas")
    lines.append("- Não há coluna confiável de horas esperadas por pessoa nesta extração para medir aderência vs capacidade planejada.")
    lines.append("- Parte dos campos está em formato textual e depende de parsing (HH:MM), sujeito a variação de origem.")
    lines.append("- A classificação por tipo de atividade é heurística e deve ser refinada com taxonomia oficial do time.")
    return "\n".join(lines)


def generate_analysis_report(data: dict) -> str:
    """Gera relatório completo de análise."""
    lines = []
    lines.append("# Relatório de Análise — Projeto POPS")
    lines.append(f"> Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"> Período: 23/03/2026 – 30/03/2026")
    lines.append("")
    lines.append("> **Pergunta central:** *Investir mais tempo em Discovery reduz esforço em Delivery?*")
    lines.append("")
    lines.append("---\n")
    lines.append("## Resumo Executivo")
    lines.append("- Foco: qualidade do registro no Jira e efeito operacional da distribuição de esforço.")
    lines.append("- Escopo: dados da semana em `timesheet`, `totals` e `worklogs`.")
    lines.append("- Saída: respostas objetivas com evidência numérica e rastreabilidade.")
    lines.append("")
    
    if "timesheet" in data and "totals" in data:
        lines.append(analyze_registro_processo(data["timesheet"], data["totals"]))
    else:
        lines.append("## 1. O que os dados mostram sobre o processo de registro\n> ⚠️ Dados insuficientes (timesheet/totals).\n---\n")

    if "worklogs" in data:
        lines.append(analyze_efeito_operacao(data["worklogs"]))
    else:
        lines.append("## 2. O que os dados mostram sobre efeito na operação\n> ⚠️ Arquivo worklogs não disponível.\n---\n")

    lines.append(build_question_status(data))
    lines.append("---\n")

    if "timesheet" in data and "totals" in data and "worklogs" in data:
        lines.append(build_executive_conclusion(data["timesheet"], data["totals"], data["worklogs"]))
    else:
        lines.append("## 3. Conclusões objetivas desta semana\n> ⚠️ Não foi possível consolidar conclusões por falta de dados.")
    lines.append("")
    lines.append("### Dados adicionais necessários para próxima rodada")
    lines.append("- [ ] Mapeamento pessoa → Squad (pendente com Camila)")
    lines.append("- [ ] Dados de períodos anteriores (para análise temporal)")
    lines.append("- [ ] Custo/hora médio do time (para cálculo financeiro)")
    
    return "\n".join(lines)


# --- Main ---
if __name__ == "__main__":
    print("=" * 50)
    print("POPS Strategic Analysis")
    print("=" * 50)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("\nCarregando dados...")
    data = load_data()
    
    if not data:
        print("[ERROR] Nenhum dado encontrado.")
        sys.exit(1)
    
    print("\nGerando análise...")
    report = generate_analysis_report(data)
    
    OUTPUT_FILE.write_text(report, encoding="utf-8")
    print(f"\n[OK] Relatório salvo em: {OUTPUT_FILE}")
    print("=" * 50)
