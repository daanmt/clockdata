# PRD: Central de Auditoria Semanal do Banco de Horas

> Generated via /vibeflow:discover on 2026-03-30

## Problem
O processo atual de extracao e analise do banco de horas possui material relevante (scripts, planilhas e documentos), mas a organizacao da pasta e do fluxo operacional ainda esta fragil. Isso dificulta consistencia, rastreabilidade e evolucao do projeto.

Os stakeholders principais (Edu e Bia, Heads de Produto/Operacoes) precisam de analises confiaveis e auditaveis, com clareza sobre como cada insight foi produzido. O problema nao e apenas "ter um numero", mas provar origem, metodo, metricas e limites da analise.

Sem uma central organizada, o time perde tempo com navegacao/manualidade, aumenta risco de erro em leitura de fontes e reduz reuso do pipeline ao longo das semanas.

## Target Audience
Usuario primario: Edu e Bia (Heads de Produto/Operacoes), com uso operacional pela pessoa responsavel pela extracao e analise semanal.

## Proposed Solution
Criar uma central lean para auditoria semanal do banco de horas, com arquitetura de informacao clara, fluxo de extracao e analise funcional e um output padrao em `.md` orientado a evidencias.

A central deve priorizar rastreabilidade de ponta a ponta: fonte de dados, transformacoes aplicadas, metricas calculadas, perguntas respondidas e limitacoes identificadas.

## Success Criteria
- Relatorio semanal em `.md` gerado com secoes auditaveis (fonte, metrica, metodo e resultado).
- Todas as perguntas criticas descritas na documentacao sao respondidas ou marcadas como "nao respondida" com justificativa de dados faltantes.
- Cada insight relevante no relatorio aponta explicitamente para a origem (arquivo/aba/coluna/regra de calculo) usada na analise.
- Estrutura de pasta padronizada e compreensivel para manutencao incremental do pipeline.

## Scope v0
- Definir e aplicar arquitetura de pastas enxuta e coerente com os documentos existentes.
- Consolidar o processo de extracao + profiling + analise usando os scripts Python ja existentes.
- Padronizar template de relatorio semanal `.md` com foco em auditabilidade e rastreabilidade.
- Garantir que o fluxo documentado de "como chegar ao insight" esteja explicito no output.
- Registrar dados faltantes e limites de confianca por pergunta de stakeholder.

## Anti-scope
- Nao automatizar pipeline completo fim a fim nesta fase.
- Nao construir dashboard, BI interativo ou camada de visualizacao avancada.
- Nao integrar APIs externas (ex.: Jira API) nesta etapa inicial.
- Nao incluir previsoes/preditivo ou modelagem estatistica complexa.
- Nao priorizar deadlines operacionais agora; foco e qualidade do processo analitico.

## Technical Context
Com base em `.vibeflow/`, o projeto usa Python + pandas + openpyxl e geracao de markdown. Ja existem padroes detectados de:
- setup de paths com `PROJECT_ROOT` e leitura resiliente de arquivos Excel;
- deteccao heuristica de colunas PT/EN para schemas variaveis;
- composicao de relatorios por secoes markdown.

Principais artefatos existentes:
- `extract_and_explore.py` para profiling de datasets;
- `analyze_hours.py` para analise estrategica;
- documentacao de contexto/perguntas em `README.md`, `project_overview.md`, `data_dictionary.md`, `discovery_questions.md` e prompts.

Restricoes conhecidas:
- estrutura fisica atual achatada na raiz;
- nomes de arquivos de dados com periodo hardcoded;
- ausencia de testes automatizados para heuristicas de schema.

## Open Questions
- Qual nomenclatura final e definitiva das pastas (fisica) sera adotada para refletir a estrutura logica (core/docs/scripts/prompts/data/output)?
- Quais metricas minimas devem ser tratadas como "obrigatorias" no relatorio semanal para Edu e Bia em toda rodada?
