---
tags: [python, pandas, schema-detection, heuristics, analytics]
modules: [./]
applies_to: [scripts, models]
confidence: inferred
---
# Pattern: Heuristic Column Detection

<!-- vibeflow:auto:start -->
## What
Padrao para detectar colunas de forma resiliente quando o schema pode variar entre portugues e ingles.

## Where
Analises em `analyze_hours.py`, especialmente nas funcoes de aderencia, qualidade e distribuicao de esforco.

## The Pattern
1. Capturar lista de colunas com `df.columns.tolist()`.
2. Escolher coluna-alvo com `next(..., fallback)` usando palavras-chave multilanguage.
3. Detectar colunas numericas com `select_dtypes(include='number')`.
4. Gerar aviso explicito quando a deteccao falha.

## Rules
- Sempre definir fallback seguro (`cols[0]` ou `None`) para nao quebrar o script.
- Tratar colunas em PT/EN (`user`, `usuário`, `name`, `horas`, `hours`).
- Quando nao achar coluna critica, escrever warning no relatorio markdown.
- Preferir heuristica legivel com listas pequenas de keywords.

## Examples from this codebase
File: analyze_hours.py
```python
cols = totals.columns.tolist()
user_col = next((c for c in cols if any(k in c.lower() for k in ['user', 'usuário', 'nome', 'name', 'member'])), cols[0])
numeric_cols = totals.select_dtypes(include='number').columns.tolist()
```

File: analyze_hours.py
```python
hours_col = next((c for c in cols if any(k in c.lower() for k in ['hours', 'horas', 'time', 'logged'])), None)
type_col = next((c for c in cols if any(k in c.lower() for k in ['type', 'tipo', 'issue type'])), None)
epic_col = next((c for c in cols if any(k in c.lower() for k in ['epic', 'épico'])), None)
```
<!-- vibeflow:auto:end -->

## Anti-patterns (if found)
- Heuristicas dependem de substrings e podem ter falso positivo em schemas muito diferentes; quando mudar fonte de dados, revisar listas de keywords.
