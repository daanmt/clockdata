# Project: Clockdata (Projeto POPS)
> Analyzed: 2026-03-31
> Stack: Python 3.10+, pandas, openpyxl, markdown reporting
> Type: other (analytics workspace with scripts + documentation)
> Suggested budget: <= 4 files per task

## Structure
Workspace orientada a auditoria semanal de banco de horas Jira/Clockwork, com pipeline Python em `scripts/`, dados em `data/` e saidas auditaveis em `output/`.

## Structural Units
- `scripts/`: automacao de profiling e analise estrategica orientada a perguntas-chave.
- `docs/`: dicionario de dados, discovery questions e template de relatorio semanal.
- `core/`: contexto de negocio, metodologia, plano de acao e papeis do time.
- `prompts/`: instrucoes de execucao para fluxo assistido por IA.
- `data/`: fontes Excel semanais (timesheet, totals, worklogs).
- `output/`: artefatos gerados (`data_profile.md`, `analysis_report.md`).

## Pattern Registry

<!-- vibeflow:patterns:start -->
patterns:
  - file: patterns/data-loading-and-path-setup.md
    tags: [python, pandas, excel, pathlib, data-loading]
    modules: [scripts/, data/, output/]
  - file: patterns/heuristic-column-detection.md
    tags: [python, pandas, schema-detection, heuristics, analytics]
    modules: [scripts/, data/]
  - file: patterns/markdown-report-generation.md
    tags: [python, markdown, reporting, pipeline, analytics-output]
    modules: [scripts/, output/]
  - file: patterns/question-driven-audit-reporting.md
    tags: [analytics, reporting, auditability, traceability, decision-support]
    modules: [scripts/, output/, docs/]
<!-- vibeflow:patterns:end -->

## Pattern Docs Available
- `patterns/data-loading-and-path-setup.md` — Padrao de inicializacao de caminhos e leitura resiliente de Excel.
- `patterns/heuristic-column-detection.md` — Heuristicas PT/EN para detectar colunas em schemas variaveis.
- `patterns/markdown-report-generation.md` — Composicao de relatorios markdown por secoes reutilizaveis.
- `patterns/question-driven-audit-reporting.md` — Relatorio auditavel orientado por perguntas de negocio e evidencias.

## Key Files
- `README.md` — guia principal de execucao e arquitetura logica.
- `scripts/extract_and_explore.py` — profiling de datasets e geracao de `output/data_profile.md`.
- `scripts/analyze_hours.py` — analise Jira-first e geracao de `output/analysis_report.md`.
- `scripts/requirements.txt` — dependencias minimas de analytics.
- `docs/discovery_questions.md` — roteiro investigativo com hipoteses e metricas.
- `docs/data_dictionary.md` — contrato esperado de schema e relacoes dos datasets.
- `docs/report_template_semanal.md` — template de entrega auditavel para comunicacao interna.
- `core/project_overview.md` — contexto de negocio, objetivos e stakeholders.
- `prompts/prompt_data_extraction.md` — fluxo de setup e validacao do schema.
- `prompts/prompt_analysis.md` — passos para analise final e criterios de sucesso.
- `core/action_plan.md` — backlog de acoes taticas e estrategicas.

## Dependencies (critical only)
- `pandas` — carga de Excel, agregacao e transformacao de dados.
- `openpyxl` — engine para leitura de arquivos `.xlsx`.
- `matplotlib` — base para visualizacoes solicitadas nos prompts.
- `seaborn` — visualizacoes estatisticas em nivel executivo.

## Known Issues / Tech Debt
- `README.md` ainda referencia arquivo de OKRs em `data/`, mas essa fonte pode estar ausente em rodadas atuais.
- Datas de arquivo Excel estao hardcoded no nome dos arquivos, exigindo manutencao manual por periodo.
- Sem cobertura de testes automatizados para heuristicas de deteccao de colunas.
- `extract_and_explore.py` ainda tenta carregar OKRs por padrao e gera warning quando arquivo nao existe.
