## Audit Report: central-auditoria-semanal-banco-horas

**Verdict: FAIL**

### Test Gate (mandatory)
- **Status:** FAIL
- **Command executado:** `python -m pytest`
- **Resultado:** `collected 0 items` com `exit code 5`
- **Regra aplicada:** test runner detectado + retorno diferente de zero => auditoria falha automaticamente.

### DoD Checklist
- [ ] Nao auditado — bloqueado pelo Test Gate (pytest falhou por ausencia de testes coletados).

### Pattern Compliance
- [ ] Nao auditado — bloqueado pelo Test Gate (a regra de auditoria interrompe validacao de DoD/padroes quando testes falham).

### Convention Violations (if any)
- Nao avaliado nesta rodada por bloqueio no Test Gate.

### Gaps (if PARTIAL or FAIL)
1. **Nao existe suite minima de testes coletavel pelo pytest**
   - O que falta: pelo menos 1 teste de smoke para validar execucao dos scripts criticos.
   - O que precisa para fechar:
     - Criar pasta `tests/`
     - Adicionar teste(s) smoke para:
       - `scripts/extract_and_explore.py` (gera `output/data_profile.md`)
       - `scripts/analyze_hours.py` (gera `output/analysis_report.md`)
     - Garantir que `python -m pytest` retorna exit code 0.
   - Esforco estimado: **M**

2. **Aviso de permissao para cache do pytest**
   - O que falta: estabilizar ambiente de teste para evitar ruído de permissao (`.pytest_cache`).
   - O que precisa para fechar:
     - Ajustar execucao sem depender de cache, ou
     - Corrigir permissao da pasta do workspace.
   - Esforco estimado: **S**

### Incremental Prompt Pack (if PARTIAL or FAIL)
Objetivo: fechar apenas os gaps de teste para destravar a auditoria, sem refatorar o pipeline.

```
Implemente uma suíte mínima de smoke tests para o projeto Clockdata.

Contexto:
- Stack Python com scripts CLI:
  - scripts/extract_and_explore.py
  - scripts/analyze_hours.py
- O audit falhou porque `python -m pytest` retornou exit code 5 (0 testes coletados).
- Não alterar arquitetura nem escopo funcional; foque apenas em testes.

Requisitos:
1) Criar pasta `tests/` com pelo menos 2 testes:
   - teste de smoke para `extract_and_explore.py` (execução sem crash + geração de `output/data_profile.md`)
   - teste de smoke para `analyze_hours.py` (execução sem crash + geração de `output/analysis_report.md`)
2) Se necessário, usar monkeypatch/fixtures para isolar I/O e evitar dependência frágil de ambiente.
3) Manter aderência aos padrões:
   - `.vibeflow/patterns/data-loading-and-path-setup.md`
   - `.vibeflow/patterns/heuristic-column-detection.md`
   - `.vibeflow/patterns/markdown-report-generation.md`
4) Respeitar convenções:
   - `.vibeflow/conventions.md`
   - sem dependências novas sem justificativa
   - sem hardcode de caminho absoluto
5) Critério de aceite:
   - `python -m pytest` deve retornar exit code 0.

Entregue:
- arquivos de teste criados
- breve nota de execução dos testes
```
