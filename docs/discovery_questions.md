# Discovery Questions — Roteiro da Análise

> Este documento é o **roteiro de investigação**. Cada pergunta tem hipótese, métricas e fonte de dados. A IA executora deve responder cada uma com evidências.

---

## 🔴 Pergunta Central

### **Investir mais tempo em Discovery reduz esforço em Delivery?**

**Hipótese:** Sim. Funcionalidades (Épicos) com maior proporção de horas em Discovery apresentam menos bugs, menos retrabalho e menor tempo total de Delivery.

**Como responder:**
1. Classificar worklogs como Discovery ou Delivery via **Issue Types**
   - Discovery: Spike, Research, Prototype, Design, Análise, Prototipação
   - Delivery: Story, Task, Sub-task, Development, Codificação
   - Qualidade: Bug, Defeito, Test, Correção
   - Overhead: Meeting, Reunião, Documentação
2. Calcular razão Discovery/Delivery **por Épico**
3. Cruzar com volume de bugs/correções por Épico
4. Calcular correlação

**Faixa ideal:** razão D/D entre 0.15–0.25

---

## Dimensão 1: Qualidade do Processo de Apontamento

### P1.1: O apontamento reflete a realidade?
- **Hipótese:** A maioria registra horas reais, mas há padrões artificiais
- **Como:** Calcular desvio padrão diário por pessoa. Desvio < 0.3h = possível padrão artificial
- **Fonte:** `timesheet_*.xlsx`

### P1.2: Quais lacunas o modelo de apontamento tem?
- **Hipótese:** Reuniões, gestão e alinhamentos não são capturados
- **Contexto reunião:** PMs/PNs realizam muitas reuniões que **não são vinculadas a funcionalidades** `00:00:00`
- **Como:** Comparar `totals` (esperado vs apontado), segmentar gap por papel
- **Fonte:** `totals_*.xlsx` + classificação de `team_roles.md`

### P1.3: O que PMs/PDs fazem com o tempo não registrado?
- **Contexto reunião:** "Não conseguem dedicar 6h em funcionalidades se trabalham 8-10h/dia" `00:05:41`
- **Como:** Calcular gap médio por papel e listar atividades não registráveis prováveis
- **Fonte:** `totals_*.xlsx` + entrevistas qualitativas

---

## Dimensão 2: Distribuição de Esforço

### P2.1: Onde o tempo está sendo investido?
- **Como:** Agrupar horas por **Issue Type** (prototipação, documentação, codificação, reunião)
- **Fonte:** `worklogs_*.xlsx`

### P2.2: Quanto tempo vai para cada Épico (funcionalidade)?
- **Contexto reunião:** Clockwork permite **Breaking Down por Épicos** `00:09:00` `00:11:23`
- **Como:** Somar horas por Épico, rankear, identificar Pareto (80/20)
- **Fonte:** `worklogs_*.xlsx`

### P2.3: Existem funcionalidades com +3 meses?
- **Contexto reunião:** +3 meses pode indicar problemas `00:03:13`
  - Falta de alinhamento
  - Demandas mal definidas
  - Necessidade de quebra em partes menores
- **Como:** Calcular data primeira/última hora por Épico
- **Fonte:** `worklogs_*.xlsx` (necessita dados de múltiplos períodos)

---

## Dimensão 3: Custo por Funcionalidade

### P3.1: Quanto custa construir uma funcionalidade?
- **Contexto reunião:** "Quanto custa colocar um produto ou funcionalidade no ar?" `00:06:41`
- **Como:** Total horas por Épico × custo/hora médio
- **Fonte:** `worklogs_*.xlsx` + premissa de custo/hora (solicitar à Mariana)

### P3.2: O custo das funcionalidades é justificável?
- **Contexto reunião:** Avaliar se entregas foram boas, tempo necessário, alinhamentos corretos `00:06:41`
- **Como:** Comparar custo real vs estimativa (se disponível nos OKRs)
- **Fonte:** `worklogs_*.xlsx` + `Planejamento de OKRs - POPs.xlsx`

### P3.3: Os dados geram poder de negociação?
- **Contexto reunião:** "500 horas de uma squad" como argumento com Comercial `00:07:54`
- **Como:** Calcular custo total por squad/período para cenários de negociação
- **Fonte:** `worklogs_*.xlsx` + custo/hora

---

## Dimensão 4: Aderência por Papel

### P4.1: PMs e PDs estão na faixa esperada?
- **Contexto reunião:** PDs mais próximos do esperado; PMs/PNs com muitas reuniões paralelas `00:00:00`
- **Como:** Calcular aderência real por pessoa, agrupar por papel
- **Fonte:** `totals_*.xlsx` + `team_roles.md`

### P4.2: A aderência é estável ao longo do tempo?
- **Como:** Comparar múltiplos períodos
- **Fonte:** Necessita dados de 3-6 meses

---

## Dimensão 5: Viabilidade da Análise Contínua

### P5.1: Podemos replicar esta análise para outros times?
- **Contexto reunião:** Outros times de tecnologia começarão a usar Jira `00:20:22`
- **Como:** Documentar processo, criar templates de relatórios Clockwork
- **Fonte:** Definição de processo

### P5.2: Os relatórios salvos no Clockwork são suficientes?
- **Contexto reunião:** Camila sugeriu salvar relatórios personalizados por squad `00:17:26`
- **Como:** Testar relatórios com filtros de Épico + Issue Type + período 3-6 meses
- **Fonte:** Clockwork

---

## Checklist de Execução

A IA executora deve:
- [ ] Responder cada pergunta com dados reais
- [ ] Indicar nível de confiança (Alto / Médio / Baixo)
- [ ] Marcar perguntas que **não podem ser respondidas** com dados atuais
- [ ] Listar dados adicionais necessários
- [ ] Gerar visualizações para perguntas-chave
- [ ] Destacar quais insights são apresentáveis à **Bia**
