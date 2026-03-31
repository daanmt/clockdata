# Framework de Metodologia — Análise de Horas POPS

## Diretrizes Estratégicas

### 1. Aderência ≠ Erro — É Ponto de Partida

A diferença entre horas esperadas vs. apontadas **não é falha**. Deve ser analisada como:
- Indicador de atividades não mapeadas
- Diferença natural do papel (PMs, PDs, PNs)
- Ponto de partida para entender: **o que estão fazendo e se é necessário**

**Foco da análise:**
- Aderência individual por papel
- Padrões de comportamento
- Coerência do apontamento

### 2. Custo por Funcionalidade (Prioridade da Diretoria)

As horas respondem: *"Quanto custa colocar uma funcionalidade no ar?"*

Usar **Clockwork → Breaking Down por Épicos** para consolidar horas por funcionalidade.

> [!WARNING]
> Funcionalidades com **+3 meses** podem indicar: falta de alinhamento, escopo mal definido ou necessidade de quebra em partes menores.

### 3. Discovery vs Delivery (via Issue Types)

Usar **Issue Types** do Jira para classificar:
- **Discovery:** Prototipação, Análise, Design, Spike
- **Delivery:** Codificação, Story, Task
- **Qualidade:** Bug, Correção, Test
- **Overhead:** Reunião, Documentação

Responder: *"Investir mais em discovery reduz esforço em delivery?"*

### 4. Visão por Épico e Squad (não individual)

- Dados atuais são **muito individuais** — dificulta comparar Produto X vs Produto Y
- Épicos = funcionalidades
- Consolidar por **Squad** e **Produto**
- Configurar relatórios salvos no Clockwork **por Squad**

### 5. Dois Horizontes de Análise

| Horizonte | Período | Uso |
|-----------|---------|-----|
| **Tático** | Semanal | Acompanhamento de aderência (solicitado pelo Edu) |
| **Estratégico** | 3-6 meses | Custo por funcionalidade, Discovery/Delivery |

> [!IMPORTANT]
> Épicos ficam abertos por 3-6 meses. Análise semanal é insuficiente para avaliar funcionalidades.

### 6. Uso Estratégico

Os dados devem gerar:
- **Poder de negociação** com Comercial (ex: custo de 500h de uma squad)
- Melhor priorização de roadmap
- Insumos para **Lei do Bem** (benefícios fiscais em P&D)
- Avaliação de qualidade: entregas boas? tempo necessário? alinhamentos corretos?

---

## Análises Obrigatórias

| Análise | Métricas | Visualização |
|---------|----------|--------------|
| **Aderência** | Horas apontadas vs esperado, ranking por papel | Barras |
| **Qualidade do apontamento** | Padrões repetitivos, desvio padrão diário | Heatmap |
| **Distribuição de esforço** | Por Épico, por Issue Type, por Projeto | Pizza/Barras |
| **Discovery vs Delivery** | Razão D/D por Épico, correlação com bugs | Scatter |
| **Custo por funcionalidade** | Horas × custo/hora por Épico | Barras |
| **Análise temporal** | Tático (semanal) + Estratégico (3-6 meses) | Linha |

## Alertas de Qualidade

- 🔴 Horas **iguais todos os dias** → padrão artificial
- 🔴 Épicos abertos **+3 meses** sem conclusão → investigar
- 🟡 **Sub ou super alocação** fora dos limites do papel
- 🟢 Variação natural → apontamento orgânico
