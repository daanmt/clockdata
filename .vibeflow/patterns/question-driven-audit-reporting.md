---
tags: [analytics, reporting, auditability, traceability, decision-support]
modules: [scripts/, output/, docs/]
applies_to: [scripts, services, configs]
confidence: inferred
---
# Pattern: Question-Driven Audit Reporting

<!-- vibeflow:auto:start -->
## What
Padrao para gerar relatorios semanais orientados por perguntas de negocio, com resposta objetiva, evidencia numerica e trilha de rastreabilidade.

## Where
Principalmente em `scripts/analyze_hours.py`, com saída em `output/analysis_report.md` e alinhamento com `docs/report_template_semanal.md`.

## The Pattern
1. Definir perguntas-chave e responder cada uma com metrica objetiva.
2. Organizar o relatorio em camadas: resumo executivo, analises por tema, status auditavel, conclusoes.
3. Em cada bloco analitico, registrar fonte, colunas, regra/metodo e metrica principal.
4. Reduzir ruido de output: preferir top-N e indicadores sintese em vez de dumps extensos.

## Rules
- Toda conclusao deve apontar evidencia quantitativa.
- Sempre explicitar limitacoes e dados faltantes no fim do relatorio.
- Usar linguagem executiva para leitura por gestao (objetiva, sem jargao excessivo).
- Evitar secoes sem resposta; quando faltar dado, marcar como "Nao respondida (dados faltantes)".

## Examples from this codebase
File: scripts/analyze_hours.py
```python
lines.append("## Resumo Executivo")
lines.append("- Foco: qualidade do registro no Jira e efeito operacional da distribuição de esforço.")
...
lines.append("| Pergunta-chave | Resposta objetiva | Evidência |")
```

File: scripts/analyze_hours.py
```python
add_traceability_block(
    lines,
    "Distribuição operacional de esforço",
    "data/worklogs_2026-03-23_2026-03-30.xlsx",
    [author_col, issue_type_col, hours_col, project_col, status_col],
    "Classificação semântica de Issue Type em Discovery/Delivery/Qualidade/Overhead e agregação por horas.",
    "Participação percentual de horas por categoria e razão Discovery/Delivery.",
)
```
<!-- vibeflow:auto:end -->

## Anti-patterns (if found)
- Gerar tabelas extensas sem síntese executiva.
- Declarar resposta sem indicar a fonte da métrica.
