# Vibeflow Index
> Project: Clockdata (Projeto POPS) | Stack: Python + pandas + Excel + markdown reports | Analyzed: 2026-03-31

## .vibeflow/ docs available
- index.md — project overview and structure
- conventions.md — coding conventions
- patterns/data-loading-and-path-setup.md — setup de paths e leitura de dados Excel
- patterns/heuristic-column-detection.md — deteccao heuristica de colunas PT/EN
- patterns/markdown-report-generation.md — montagem de relatorios markdown
- patterns/question-driven-audit-reporting.md — relatorio orientado a perguntas e evidencias
- decisions.md — architectural decision log

## Quick Reference
- Sempre ancorar caminhos em `PROJECT_ROOT` com `pathlib.Path`.
- Rodar profiling antes da analise estrategica.
- Tratar schemas como variaveis (PT/EN) e manter fallback + warning.
- Gerar saidas em markdown orientadas por perguntas-chave e rastreabilidade.
- Registrar lacunas de dados explicitamente no relatorio final.

## Instructions
Before generating ANY spec, prompt pack, or audit:
1. Read .vibeflow/index.md for project context
2. Read .vibeflow/conventions.md for coding standards
3. Read the relevant pattern docs from .vibeflow/patterns/
4. Embed applicable patterns in your output

When you learn something new about this project, update:
- .vibeflow/decisions.md for architectural decisions
- .vibeflow/conventions.md if new conventions are discovered
- .vibeflow/patterns/*.md if patterns evolve
- This MEMORY.md index if new docs are added
