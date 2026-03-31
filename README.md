# 📊 Projeto POPS — Análise de Banco de Horas (Omie)

> **Pergunta central:** *Investir mais tempo em discovery reduz esforço em delivery?*

## 🎯 O que é este projeto

Análise estratégica dos dados de horas registradas no Jira (via Clockwork) para o time de produto da **Omie**. O objetivo é avaliar produtividade, distribuição de esforço, custo por funcionalidade e qualidade do processo de apontamento, embasando decisões estratégicas, orçamentárias (como a Lei do Bem) e negociações com áreas de negócio.

---

## 📁 Estrutura do Projeto

A organização de diretórios segue uma arquitetura modular, separando a base de contexto estratégico, dados brutos, execução técnica e resultados gerados:

```text
Clockdata/
├── .vibeflow/             ← Padrões, convenções de código e arquitetura (IA)
├── core/                  ← Documentação estratégica, escopo e planos de ação
├── data/                  ← Dados brutos e planilhas de exportação (Excel)
├── docs/                  ← Contexto de domínio, discovery e dicionários
├── output/                ← Resultados da análise, relatórios e métricas geradas
├── prompts/               ← Prompts estruturados para IAs executoras
├── scripts/               ← Scripts de execução (Extração Python e Análise)
├── MEMORY.md              ← Índice de contexto rápido para os agentes AI
└── README.md              ← Você está aqui
```

---

## 🚀 Como Executar (Time Técnico & IA)

### Pré-requisitos
- **Python 3.10+** (Recomenda-se ambiente virtual, ex: `venv` ou `conda`)
- Arquivos Excel de base exportados para a pasta `data/`

### Passo a Passo

```bash
# 1. Instalar as dependências necessárias do projeto
pip install -r scripts/requirements.txt

# 2. Explorar os dados brutos e gerar um profiling (qualidade/lacunas)
python scripts/extract_and_explore.py

# 3. Executar o motor de análise estratégica e consolidar visões
python scripts/analyze_hours.py
```
> **Nota:** Todos os resultados (relatórios em Markdown e bases CSV/Excel tratadas) serão automaticamente salvados na raiz da pasta `output/`.

---

## 📖 Documentação Importante

Aqui estão os principais documentos recomendados para compreender o escopo e as regras de negócio:

| Documento | Descrição |
|-----------|-----------|
| **[Visão Geral do Projeto](core/project_overview.md)** | Contexto do negócio, horizonte de análise, objetivos principais e stakeholders. |
| **[Fundamentos Estratégicos](core/strategic_metrics_foundations.md)** | Epistemologia de Engenharia, Qualidade (Shift-Left, Lean) e métricas base. |
| **[Resumo Executivo](core/analysis_executive_summary.md)** | Diagnóstico resumido contemplando os principais KPIs de horas e esforço. |
| **[Metodologia & Framework](core/methodology_framework.md)** | Diretrizes de como cruzar variáveis, agrupar tags e responder as perguntas. |
| **[Time & Papéis](core/team_roles.md)** | Premissas de aderência e detalhamento por papéis (PM, PD, Dev, QA). |
| **[Plano de Ação](core/action_plan.md)** | Ações priorizadas divididas em visões (Tático/Curto Prazo vs. Estratégico). |
| **[Dicionário de Dados](docs/data_dictionary.md)** | Schema esperado, relacionamentos e significado das tabelas vindas do Jira. |
| **[Notas da Reunião](docs/meeting_notes_camila.md)** | Insights qualitativos, "pegadinhas" e premissas levantadas com a PM Camila. |
| **[Vibeflow Docs](.vibeflow/index.md)** | Regras de codificação, setup e documentação arquitetural da heurística (AI). |

---

## 🧠 Fluxo de Trabalho (Humanos + IA)

O ecossistema é projetado para atuar orquestrado entre raciocínio (Claude) e execução (IA Local):

```text
  [Discovery / Estratégia]            [Delivery / IA Executora]
  ─────────────────────────           ─────────────────────────
  • Absorção de core/ e docs/   ----► • Instala dependências (requirements)
  • Define roteiros de análise  ----► • Processa scripts de Python
  • Levanta hipóteses com base  ◄---- • Identifica lacunas (heurística)
    no Jira e time Omie               • Exporta sumários em output/
```

---

## 👥 Responsáveis & Papéis

- **Mariana Rodrigues** — Coordenação, Análise e Orquestração
- **Bia / Edu / Camila** — Stakeholders (Tomada de Decisão / Monitoramento Omie)
- **Claude (Discovery)** — Planejamento estratégico, definição de hipóteses e questionamentos
- **IA Executora (Delivery)** — Motor de processamento, extração de dados brutos e materialização dos outputs estratégico