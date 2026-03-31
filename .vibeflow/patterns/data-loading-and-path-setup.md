---
tags: [python, pandas, excel, pathlib, data-loading]
modules: [./]
applies_to: [scripts, services]
confidence: inferred
---
# Pattern: Data Loading and Path Setup

<!-- vibeflow:auto:start -->
## What
Padrao para localizar a raiz do projeto a partir do script, declarar caminhos fixos e carregar planilhas Excel com checagens de existencia.

## Where
Scripts de automacao e analise de dados na raiz do projeto.

## The Pattern
1. Definir `PROJECT_ROOT` com `Path(__file__).parent.parent`.
2. Declarar constantes de paths (`DATA_DIR`, `OUTPUT_DIR`, `OUTPUT_FILE`).
3. Antes de leitura, validar `exists()` e tratar falhas sem derrubar todo o pipeline.
4. Ler Excel com `pandas.read_excel` e registrar status no console.

## Rules
- Sempre usar `pathlib.Path` para composicao de caminhos.
- Evitar strings absolutas hardcoded para arquivos locais.
- Criar `output/` com `mkdir(parents=True, exist_ok=True)` no fluxo principal.
- Em erro de leitura de planilha, registrar mensagem clara e continuar quando possivel.

## Examples from this codebase
File: extract_and_explore.py
```python
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_FILE = OUTPUT_DIR / "data_profile.md"

for key, filename in DATA_FILES.items():
    filepath = DATA_DIR / filename
    if not filepath.exists():
        print(f"⚠️  Arquivo não encontrado: {filepath}")
        continue
```

File: analyze_hours.py
```python
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_FILE = OUTPUT_DIR / "analysis_report.md"

worklogs_file = DATA_DIR / "worklogs_2026-03-23_2026-03-30.xlsx"
if worklogs_file.exists():
    data["worklogs"] = pd.read_excel(worklogs_file)
```
<!-- vibeflow:auto:end -->

## Anti-patterns (if found)
- `import os` aparece nos dois scripts sem uso direto; manter imports minimos evita ruido.
