# Decision Log
> Newest first. Updated automatically by the architect agent.

## 2026-03-31 — Audit gate de testes bloqueou release
- Durante `/vibeflow:audit` da spec `central-auditoria-semanal-banco-horas`, o comando `python -m pytest` retornou `exit code 5` (0 testes coletados), o que dispara **FAIL automático**.
- Pitfall confirmado: sem suite minima de testes, a auditoria formal não avança mesmo com execução manual dos scripts funcionando.
- Decisão operacional: incluir smoke tests mínimos para os scripts críticos como pré-condição de "ready to ship".
