# Prompt: Análise Estratégica do Banco de Horas

> **Para:** IA Executora (Delivery)
> **Contexto:** Projeto POPS — Análise de Banco de Horas da Omie
> **Pré-requisito:** Ter executado `prompt_data_extraction.md` primeiro

---

## Sua Tarefa

Executar a análise estratégica completa e responder às perguntas de discovery.

## Leitura Obrigatória (ANTES de executar)

Leia estes documentos na ordem:
1. `README.md` — estrutura do projeto
2. `core/project_overview.md` — contexto e objetivos
3. `core/methodology_framework.md` — framework de análise
4. `core/team_roles.md` — classificação do time
5. `docs/discovery_questions.md` — **ROTEIRO DA ANÁLISE** ← mais importante
6. `docs/data_dictionary.md` — schema dos dados (já validado se passo 1 foi feito)
7. `output/data_profile.md` — profiling dos dados (gerado no passo anterior)

## Passo a Passo

### 1. Executar o Script de Análise
```bash
python scripts/analyze_hours.py
```

### 2. Revisar o Output
Abrir `output/analysis_report.md` e verificar se as análises foram geradas corretamente.

### 3. Ajustar o Script se Necessário

O script `analyze_hours.py` tem auto-detecção de colunas, mas pode precisar de ajustes:

- **ROLE_MAP** (linha ~30): Verificar se os nomes batem com os dados reais
- **DISCOVERY_TYPES / DELIVERY_TYPES** (linha ~45): Ajustar values de Issue Type com base no profiling
- **Colunas**: Se a auto-detecção falhar, mapear manualmente

### 4. Responder as Perguntas de Discovery

Para cada pergunta em `docs/discovery_questions.md`:

| Campo | O que preencher |
|-------|----------------|
| **Resposta** | O que os dados mostram |
| **Confiança** | Alto / Médio / Baixo |
| **Evidência** | Número, tabela ou gráfico |
| **Limitação** | O que faltou para responder melhor |

### 5. Gerar Relatório Final

Criar `output/final_report.md` com esta estrutura:

```markdown
# Relatório Final — Projeto POPS

## Resumo Executivo (1 parágrafo)

## Pergunta Central
> Investir mais em discovery reduz esforço em delivery?
[Resposta fundamentada]

## Diagnóstico
### O que está funcionando bem
### O que precisa melhorar
### Problemas de processo vs operação

## Insights por Dimensão
### Aderência
### Qualidade do Apontamento
### Distribuição de Esforço
### Discovery vs Delivery
### Custo por Funcionalidade

## Recomendações (priorizadas)

## Dados Adicionais Necessários (para próximo ciclo)
```

### 6. Gerar Visualizações (se possível)

Adicionar ao script ou gerar separadamente:
- Gráfico de barras: aderência por pessoa (colorido por papel)
- Pizza: distribuição Discovery / Delivery / Qualidade / Overhead
- Barras: Top 10 épicos por horas investidas
- Scatter: razão Discovery/Delivery vs bugs por épico (se houver dados)

Salvar em `output/charts/`.

## Critérios de Sucesso

- [ ] `output/analysis_report.md` gerado
- [ ] `output/final_report.md` com todas as perguntas respondidas
- [ ] Cada pergunta com nível de confiança e evidência
- [ ] Perguntas não respondíveis marcadas com motivo
- [ ] Recomendações priorizadas e acionáveis

## Contexto Estratégico

**O diagnóstico anterior indicou que:**
- 70% do problema é PROCESSO (modelo de apontamento incompleto)
- 20% é INTERPRETAÇÃO (gap visto como erro)
- 10% é OPERACIONAL

**Sua análise deve validar ou refutar esse diagnóstico com os dados reais.**

**A pergunta central é:**
> *Investir mais tempo em Discovery reduz esforço em Delivery?*

Responda com dados. Se não for possível com os dados atuais, documente **exatamente** quais dados seriam necessários.
