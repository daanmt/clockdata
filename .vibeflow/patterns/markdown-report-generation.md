---
tags: [python, markdown, reporting, pipeline, analytics-output]
modules: [./]
applies_to: [services, scripts]
confidence: inferred
---
# Pattern: Markdown Report Generation

<!-- vibeflow:auto:start -->
## What
Padrao de gerar relatorios markdown por composicao de linhas em lista e `"\n".join(lines)` ao final.

## Where
Funcoes `generate_report`, `profile_dataframe` e `generate_analysis_report` nos scripts principais.

## The Pattern
1. Inicializar `lines = []`.
2. Adicionar secoes com `lines.append(...)`, incluindo tabelas markdown.
3. Reutilizar funcoes de secao para montar o documento final.
4. Persistir em arquivo com `write_text(..., encoding="utf-8")`.

## Rules
- Estruturar o relatorio em secoes com titulos previsiveis.
- Sempre incluir data de geracao no cabecalho.
- Para tabelas dinamicas, calcular agregacoes no pandas e serializar com `to_markdown()`.
- Separar bloco de calculo da camada de apresentacao textual.

## Examples from this codebase
File: extract_and_explore.py
```python
def generate_report(datasets: dict[str, pd.DataFrame]) -> str:
    lines = []
    lines.append(f"# Data Profile — Projeto POPS")
    lines.append(f"> Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    ...
    for name, df in datasets.items():
        lines.append(profile_dataframe(name, df))
    return "\n".join(lines)
```

File: analyze_hours.py
```python
lines.append("## 4. Conclusões e Próximos Passos\n")
lines.append("> Esta seção deve ser preenchida pela IA executora após análise dos resultados acima.")
...
report = generate_analysis_report(data)
OUTPUT_FILE.write_text(report, encoding="utf-8")
```
<!-- vibeflow:auto:end -->

## Anti-patterns (if found)
- Nao ha validacao formal de schema antes da escrita final; o relatorio depende de warnings textuais para sinalizar falhas.
