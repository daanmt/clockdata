# Coding Conventions

<!-- vibeflow:auto:start -->
## Python and Data Stack
- Scripts em Python usam `pandas` para transformacao e agregacao tabular.
- Paths sao definidos com `pathlib.Path`, ancorados em `PROJECT_ROOT`.
- Saidas textuais sao markdown em `output/`, gravadas com `encoding="utf-8"`.
- Profiling e analise devem funcionar sem dependencia obrigatoria de `tabulate` (usar fallback para texto).

## File and Function Organization
- Scripts seguem fluxo linear: configuracao global -> funcoes utilitarias -> bloco `if __name__ == "__main__":`.
- Funcoes de analise retornam `str` markdown em vez de escrever direto em disco.
- Cada etapa de analise vira uma secao separada no relatorio final.
- Estrutura fisica oficial do projeto: `core/`, `docs/`, `scripts/`, `prompts/`, `data/`, `output/`.

## Naming Patterns
- Constantes globais em UPPER_CASE (`DATA_DIR`, `OUTPUT_FILE`, `ROLE_MAP`).
- Funcoes em snake_case com verbo inicial (`load_data`, `analyze_quality`, `generate_report`).
- Variaveis de coluna usam sufixo `_col` quando representam nomes de coluna detectados.
- Classificacao de papeis deve usar normalizacao de texto (acentos/case) para evitar erro por variacao de grafia.

## Schema Handling
- Deteccao de schema usa heuristicas por palavras-chave PT/EN (via `analyze_hours.py`).
- Fallback explicito quando coluna nao encontrada: `None` ou `cols[0]`, seguido de mensagem de alerta no markdown.
- Colunas numericas sao detectadas por `select_dtypes(include='number')`.
- Campos `HH:MM` devem ser convertidos para horas numericas antes de agregacoes.

## Operational Workflow
- Ordem esperada de execucao: profiling (`extract_and_explore.py`) antes da analise estrategica (`analyze_hours.py`) (via `README.md` e `prompt_data_extraction.md`).
- Classificacoes de Discovery/Delivery/Qualidade sao tratadas como hipoteses e devem ser refinadas apos profiling (via `data_dictionary.md` e comentarios no codigo).
- Relatorio semanal deve ser orientado a perguntas-chave e resposta executiva (via `docs/report_template_semanal.md`).

## Source-attributed Rules
- Evitar conclusao forte sem dados completos de 3-6 meses (via `discovery_questions.md`).
- Consolidar leitura por squad/produto para uso gerencial, nao por individuo isolado (via `project_overview.md`).
- Documentar lacunas de dados explicitamente no resultado final (via `prompt_analysis.md`).
- Quando houver remocao de fonte (ex.: arquivo ausente em `data/`), refletir no escopo da analise e nas respostas auditaveis.

## Don'ts
- Nao assumir schema fixo do Jira/Clockwork sem validar com profiling previo.
- Nao usar caminho absoluto local para dados; manter resolucao relativa por `PROJECT_ROOT`.
- Nao tratar gap de apontamento de PM/PD automaticamente como erro operacional (via `project_overview.md`).
- Nao remover alertas quando coluna essencial nao for encontrada; eles fazem parte do contrato do relatorio.
- Nao adicionar dependencia nova sem necessidade clara de analise/reporting.
- Nao publicar relatorio com dump bruto de tabelas longas sem sintese de indicadores.
- Nao responder pergunta de negocio sem metrica e fonte explicitadas.
<!-- vibeflow:auto:end -->
