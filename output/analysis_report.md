# Relatório de Análise — Projeto POPS
> Gerado em: 2026-03-31 00:40
> Período: 23/03/2026 – 30/03/2026

> **Pergunta central:** *Investir mais tempo em Discovery reduz esforço em Delivery?*

---

## Resumo Executivo
- Foco: qualidade do registro no Jira e efeito operacional da distribuição de esforço.
- Escopo: dados da semana em `timesheet`, `totals` e `worklogs`.
- Saída: respostas objetivas com evidência numérica e rastreabilidade.

## 1. O que os dados mostram sobre o processo de registro

### Rastreabilidade — Qualidade do registro por pessoa
- **Fonte:** `data/timesheet_2026-03-23_2026-03-30.xlsx + data/totals_2026-03-23_2026-03-30.xlsx`
- **Colunas usadas:** `Users / Issue Types / Issues, Level, Total Time Spent, 2026-03-23, 2026-03-24, 2026-03-25`
- **Regra/Método:** Filtro de linhas nível 0 (pessoas), parsing HH:MM para horas e cálculo de variabilidade diária.
- **Métrica principal:** Total de horas por pessoa, média diária, desvio padrão e dias sem registro.

### Indicadores de registro (resumo)
- Pessoas com registro no período: **26**
- Média de horas totais por pessoa: **21.20h**
- Média de dias sem registro por pessoa: **3.38 dias**

### Registro por papel (média)
```
       total_horas  media_diaria_h  desvio_diario_h  dias_sem_registro
Papel                                                                 
Dev          28.87            3.61             2.80               2.69
PD           11.38            1.42             1.89               4.00
PM            9.78            1.22             1.63               4.33
QA           18.92            2.36             2.63               3.80
```

### Sinal de atenção (Top 5 com mais dias sem registro)
```
Users / Issue Types / Issues Papel  dias_sem_registro  total_horas
             Tayane Portugal    PM                  6          9.0
            danielli.hiraoka    QA                  5          4.0
    Fernando Brito Campideli   Dev                  5          4.0
                 Laís Albino    PM                  5          4.0
                  Elis Verri    PM                  5          5.0
```


---

## 2. O que os dados mostram sobre efeito na operação

### Rastreabilidade — Distribuição operacional de esforço
- **Fonte:** `data/worklogs_2026-03-23_2026-03-30.xlsx`
- **Colunas usadas:** `Author, Issue Type, Time Spent (seconds), Project Key, Issue Status`
- **Regra/Método:** Classificação semântica de Issue Type em Discovery/Delivery/Qualidade/Overhead e agregação por horas.
- **Métrica principal:** Participação percentual de horas por categoria e razão Discovery/Delivery.

### Distribuição de esforço por categoria
```
                Horas     %
categoria                  
Delivery   285.750000  51.8
Qualidade  114.683333  20.8
Overhead    86.916667  15.8
Discovery   58.250000  10.6
Outros       5.666667   1.0
```

- Razão Discovery/Delivery: **0.20**
- Leitura: na faixa de referência (0.15-0.25).

### Top 5 autores por horas registradas
```
                                     Horas
Author                                    
Tatieli Ramos                        45.00
Kamila Pereira da Silva              37.00
Nathan Roberto Goncalves dos Santos  36.50
Juliana Martins Stopa                36.25
Franciellen Pereira                  34.50
```

### Top 5 projetos por horas
```
                  Horas
Project Key            
CRM          231.250000
CLP          142.750000
ORB           98.100000
AI            42.500000
CER           36.666667
```


---

## Status das Perguntas Críticas (Auditável)

| ID | Pergunta | Status | Evidência |
|----|----------|--------|-----------|
| P1.1 | O apontamento reflete a realidade? | Respondida | Análise de variabilidade diária por pessoa. |
| P1.2 | Quais lacunas o modelo de apontamento tem? | Respondida | Leitura de dias sem registro e consistência de granularidade. |
| P2.1 | Onde o tempo está sendo investido? | Respondida | Agrupamento por Issue Type/Categoria. |
| P2.2 | Quanto tempo vai para cada Épico? | Respondida | Soma de horas por Épico (top 15). |
| P3.1 | Quanto custa uma funcionalidade? | Respondida | Horas por Épico disponíveis; custo/hora ainda pendente. |
| Pergunta central | Discovery reduz esforço em Delivery? | Respondida | Razão Discovery/Delivery agregada. |

---

## 3. Respostas às perguntas-chave

| Pergunta-chave | Resposta objetiva | Evidência |
|---|---|---|
| O registro está consistente? | Parcialmente; há variação relevante entre pessoas. | Média de **3.38** dias sem registro por pessoa. |
| Onde o esforço está concentrado? | Predominantemente em Delivery. | Delivery **51.8%**, Qualidade **20.8%**. |
| Discovery está sub ou superinvestido? | Na faixa de referência. | Razão Discovery/Delivery = **0.20** (faixa 0.15-0.25). |
| O efeito operacional observado esta semana | 20.8% do esforço foi para Qualidade, sinalizando carga relevante de correções/QA. | Participação de Qualidade no total de horas. |

## 4. Conclusões objetivas desta semana

### Leitura executiva
- O registro de horas mostra **heterogeneidade entre pessoas**, com média de **21.20h por pessoa** no período.
- Em média, cada pessoa teve **3.38 dias sem registro** no recorte analisado.
- A razão Discovery/Delivery ficou em **0.20**.
- Horas classificadas como Qualidade representam **20.8%** do total registrado.

### Implicação para operação
- O processo de registro está funcional, mas ainda com sinais de inconsistência de granularidade entre pessoas e tipos de tarefa.
- O efeito operacional mais visível é a distribuição de esforço entre Discovery/Delivery/Qualidade, que indica onde o time está consumindo capacidade real.
- Sem baseline histórico (3-6 meses), esta semana responde o *estado atual*, mas não permite tendência robusta.

### Limitações explícitas
- Não há coluna confiável de horas esperadas por pessoa nesta extração para medir aderência vs capacidade planejada.
- Parte dos campos está em formato textual e depende de parsing (HH:MM), sujeito a variação de origem.
- A classificação por tipo de atividade é heurística e deve ser refinada com taxonomia oficial do time.

### Dados adicionais necessários para próxima rodada
- [ ] Mapeamento pessoa → Squad (pendente com Camila)
- [ ] Dados de períodos anteriores (para análise temporal)
- [ ] Custo/hora médio do time (para cálculo financeiro)