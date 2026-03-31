# Spec: Central de Auditoria Semanal do Banco de Horas

> Fonte: `.vibeflow/prds/central-auditoria-semanal-banco-horas.md`  
> Data: 2026-03-30  
> Budget alvo: <= 4 arquivos por tarefa

## Objective
Estabelecer uma base tecnica enxuta e auditavel para extracao e analise semanal do banco de horas, produzindo relatorio `.md` rastreavel para Edu e Bia.

## Context
Hoje o projeto ja possui scripts e documentacao robusta de contexto, mas a estrutura fisica esta achatada na raiz e o fluxo ainda depende de organizacao manual. Isso compromete repetibilidade e auditabilidade da analise semanal.

No estado atual, os padroes existentes ja suportam o v0:
- carregamento resiliente de dados por `pathlib` e `pandas`;
- deteccao heuristica de colunas PT/EN;
- geracao de relatorio markdown por secoes.

O foco desta spec e consolidar organizacao da informacao e confiabilidade do processo, sem ampliar para automacoes avancadas.

## Definition of Done
- [ ] Estrutura fisica minima do projeto e aplicada na pasta (ex.: `core/`, `docs/`, `scripts/`, `prompts/`, `data/`, `output/`) sem quebrar referencias de execucao.
- [ ] `scripts/extract_and_explore.py` executa com sucesso a partir da raiz e gera `output/data_profile.md`.
- [ ] `scripts/analyze_hours.py` executa com sucesso a partir da raiz e gera `output/analysis_report.md`.
- [ ] Existe um template de relatorio semanal em markdown com secoes obrigatorias de rastreabilidade: fonte, transformacao/regra, metrica calculada, resultado e limitacoes.
- [ ] Para cada pergunta critica de `docs/discovery_questions.md`, o relatorio final marca status binario: `Respondida` ou `Nao respondida (com justificativa de dados faltantes)`.
- [ ] Cada insight relevante no relatorio aponta explicitamente a origem dos dados (arquivo, aba quando aplicavel, coluna e regra de calculo).
- [ ] **Quality gate:** implementacao segue `conventions.md` e os padroes de `.vibeflow/patterns/`, sem violar a secao `## Don'ts` (especialmente nao assumir schema fixo e manter warnings quando deteccao falhar).

## Scope
- Reorganizar artefatos existentes para arquitetura de informacao enxuta e legivel.
- Ajustar caminhos/referencias dos scripts para refletir a estrutura organizada.
- Padronizar output de auditoria semanal em markdown auditavel.
- Garantir rastreabilidade de insights e explicitacao de lacunas de dados.
- Preservar e reutilizar scripts existentes como base (sem reescrever pipeline do zero).

## Anti-scope
- Automacao completa de ponta a ponta (agendamento, orquestracao, CI de dados).
- Integracao com Jira API ou qualquer fonte externa nova.
- Dashboard, BI interativo ou camada de visualizacao dedicada.
- Modelos preditivos, scoring avancado ou estatistica complexa.
- Definicao de SLA/deadline operacional nesta fase.

## Technical Decisions
1. **Arquitetura fisica alinhada ao modelo logico do README**
   - Decisao: mover arquivos para `core/`, `docs/`, `scripts/`, `prompts/`, mantendo `data/` e `output/`.
   - Trade-off: pequeno custo inicial de ajuste de paths vs grande ganho em navegacao e escalabilidade.
   - Justificativa: reduz ambiguidade e facilita onboarding/manutencao semanal.

2. **Manter pipeline em scripts Python locais (sem orquestrador externo)**
   - Decisao: preservar execucao por CLI simples (`python scripts/...`).
   - Trade-off: menos automacao agora vs menor complexidade operacional.
   - Justificativa: aderente ao objetivo lean e ao anti-scope.

3. **Relatorio orientado a evidencias como contrato principal de entrega**
   - Decisao: output oficial do v0 sera markdown auditavel.
   - Trade-off: menos polish visual vs rastreabilidade objetiva para auditoria.
   - Justificativa: atende diretamente ao requisito "como chegou no insight".

4. **Tolerancia a variacao de schema com heuristicas e warning explicito**
   - Decisao: manter deteccao PT/EN por keywords + fallback seguro + alertas no relatorio.
   - Trade-off: risco de falso positivo em schema muito diferente vs robustez para ambiente real heterogeneo.
   - Justificativa: consistente com dados Jira/Clockwork variaveis e com convencoes atuais.

## Applicable Patterns
- `.vibeflow/patterns/data-loading-and-path-setup.md`
- `.vibeflow/patterns/heuristic-column-detection.md`
- `.vibeflow/patterns/markdown-report-generation.md`

Novo padrao potencial (se confirmado na implementacao):
- `audit-traceability-reporting.md` (padrao para matriz de evidencias por insight: pergunta -> fonte -> regra -> metrica -> conclusao -> confianca).

## Risks
- **Quebra de paths apos reorganizacao de pastas**  
  Mitigacao: validar execucao dos dois scripts apos cada movimento estrutural.

- **Schema real divergir das heuristicas atuais**  
  Mitigacao: manter warnings obrigatorios e registrar gaps no relatorio.

- **Relatorio responder parcialmente perguntas criticas**  
  Mitigacao: status binario por pergunta e secao explicita de "dados ausentes".

- **Escopo crescer para automacao/BI antes da base estar solida**  
  Mitigacao: reforcar anti-scope e validar DoD de fundacao antes de evoluir.

## Assumptions / TODOs
- Assuncao: a pasta `data/` sera mantida como entrada oficial de arquivos semanais.
- TODO: fechar nomenclatura final de arquivos de entrada para reduzir hardcode de periodo.
- TODO: definir conjunto minimo de metricas obrigatorias (core KPI set) para toda semana.
