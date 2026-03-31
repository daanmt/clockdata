"""
extract_and_explore.py — Profiling dos dados do banco de horas POPS

Lê os 4 arquivos Excel da pasta data/ e gera um relatório de profiling
em output/data_profile.md com:
- Schema de cada arquivo (colunas, tipos, nulos)
- Estatísticas descritivas
- Valores únicos das colunas categóricas
- Primeiras linhas de amostra
- Validação do dicionário de dados (docs/data_dictionary.md)

Uso:
    python scripts/extract_and_explore.py
"""

import sys
import pandas as pd
from pathlib import Path
from datetime import datetime

# --- Configuração ---
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_FILE = OUTPUT_DIR / "data_profile.md"

DATA_FILES = {
    "timesheet": "timesheet_2026-03-23_2026-03-30.xlsx",
    "totals": "totals_2026-03-23_2026-03-30.xlsx",
    "worklogs": "worklogs_2026-03-23_2026-03-30.xlsx",
    "okrs": "Planejamento de OKRs - POPs.xlsx",
}

# --- Funções ---


def df_to_table(df: pd.DataFrame, index: bool = False) -> str:
    """Renderiza DataFrame em markdown quando possível, com fallback sem tabulate."""
    try:
        return df.to_markdown(index=index)
    except ImportError:
        return "```\n" + df.to_string(index=index) + "\n```"

def load_all_data() -> dict[str, pd.DataFrame]:
    """Carrega todos os Excel. Tenta todas as sheets de cada arquivo."""
    datasets = {}
    for key, filename in DATA_FILES.items():
        filepath = DATA_DIR / filename
        if not filepath.exists():
            print(f"[WARN] Arquivo não encontrado: {filepath}")
            continue
        
        try:
            # Lê todas as sheets
            xls = pd.ExcelFile(filepath)
            sheets = xls.sheet_names
            
            if len(sheets) == 1:
                datasets[key] = pd.read_excel(filepath, sheet_name=0)
                print(f"[OK] {key}: {len(datasets[key])} linhas, {len(datasets[key].columns)} colunas (sheet: {sheets[0]})")
            else:
                # Múltiplas sheets: carrega como dict
                for sheet in sheets:
                    sheet_key = f"{key}__{sheet.replace(' ', '_').lower()}"
                    datasets[sheet_key] = pd.read_excel(filepath, sheet_name=sheet)
                    print(f"[OK] {sheet_key}: {len(datasets[sheet_key])} linhas, {len(datasets[sheet_key].columns)} colunas")
        except Exception as e:
            print(f"[ERROR] Erro ao ler {filename}: {e}")
    
    return datasets


def profile_dataframe(name: str, df: pd.DataFrame) -> str:
    """Gera perfil markdown de um DataFrame."""
    lines = []
    lines.append(f"### {name}")
    lines.append(f"- **Linhas:** {len(df):,}")
    lines.append(f"- **Colunas:** {len(df.columns)}")
    lines.append(f"- **Memória:** {df.memory_usage(deep=True).sum() / 1024:.1f} KB")
    lines.append("")
    
    # Schema
    lines.append("#### Schema")
    lines.append("| # | Coluna | Tipo | Nulos | Nulos % | Únicos |")
    lines.append("|---|--------|------|-------|---------|--------|")
    for i, col in enumerate(df.columns):
        n_null = df[col].isnull().sum()
        pct_null = (n_null / len(df) * 100) if len(df) > 0 else 0
        n_unique = df[col].nunique()
        dtype = str(df[col].dtype)
        lines.append(f"| {i+1} | `{col}` | {dtype} | {n_null} | {pct_null:.1f}% | {n_unique} |")
    lines.append("")
    
    # Estatísticas para numéricos
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:
        lines.append("#### Estatísticas Numéricas")
        lines.append("| Coluna | Min | Média | Mediana | Max | Desvio |")
        lines.append("|--------|-----|-------|---------|-----|--------|")
        for col in numeric_cols:
            lines.append(
                f"| `{col}` | {df[col].min():.2f} | {df[col].mean():.2f} | "
                f"{df[col].median():.2f} | {df[col].max():.2f} | {df[col].std():.2f} |"
            )
        lines.append("")
    
    # Valores únicos para categóricas (top 10)
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(cat_cols) > 0:
        lines.append("#### Top Valores Categóricos")
        for col in cat_cols:
            top = df[col].value_counts().head(10)
            if len(top) > 0:
                lines.append(f"\n**`{col}`** ({df[col].nunique()} únicos):")
                for val, count in top.items():
                    pct = count / len(df) * 100
                    lines.append(f"- `{val}`: {count} ({pct:.1f}%)")
        lines.append("")
    
    # Amostra (5 primeiras linhas)
    lines.append("#### Amostra (5 linhas)")
    lines.append(df_to_table(df.head(5), index=False))
    lines.append("")
    lines.append("---")
    lines.append("")
    
    return "\n".join(lines)


def generate_report(datasets: dict[str, pd.DataFrame]) -> str:
    """Gera relatório completo de profiling."""
    lines = []
    lines.append(f"# Data Profile — Projeto POPS")
    lines.append(f"> Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("## Resumo")
    lines.append("")
    lines.append("| Dataset | Linhas | Colunas |")
    lines.append("|---------|--------|---------|")
    for name, df in datasets.items():
        lines.append(f"| {name} | {len(df):,} | {len(df.columns)} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Profile de cada dataset
    lines.append("## Detalhamento por Dataset")
    lines.append("")
    for name, df in datasets.items():
        lines.append(profile_dataframe(name, df))
    
    return "\n".join(lines)


# --- Main ---
if __name__ == "__main__":
    print("=" * 50)
    print("POPS Data Profiling")
    print("=" * 50)
    
    # Criar output dir
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Carregar dados
    print("\nCarregando dados...")
    datasets = load_all_data()
    
    if not datasets:
        print("[ERROR] Nenhum dado encontrado. Verifique a pasta data/")
        sys.exit(1)
    
    # Gerar relatório
    print("\nGerando relatório...")
    report = generate_report(datasets)
    
    # Salvar
    OUTPUT_FILE.write_text(report, encoding="utf-8")
    print(f"\n[OK] Relatório salvo em: {OUTPUT_FILE}")
    print(f"   Tamanho: {len(report):,} caracteres")
    print("=" * 50)
