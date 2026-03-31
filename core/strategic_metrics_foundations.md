# Fundamentos Estratégicos & Métricas de Engenharia

> **Objetivo deste documento:** Elevar o ecossistema de dados do Projeto POPS. Deixar de encarar o apontamento de horas como puro "banco de horas e microgerenciamento" e passar a utilizá-lo como um **motor de inferência sofisticado**, embasado nas melhores escolas de Engenharia de Software, Gestão de Produtos e Qualidade.

---

## 1. As Epistemologias de Referência

Toda a taxonomia das nossas análises, variáveis e conclusões provém da interseção de três grandes escolas empíricas da tecnologia global:

### A. Product Management (Dual-Track Agile)
Disciplina que postula que o ciclo de construção de software é sempre dividido em duas vias paralelas e interdependentes:
*   **Discovery (Descoberta):** Focada em mitigação de riscos (Valor, Usabilidade, Viabilidade Técnica e Negócio). Mede-se pelo esforço em prototipações, documentações, pesquisas de tela e refinamentos de critérios de aceite originais. Responde à pergunta: *"Estamos construindo a coisa certa?"*
*   **Delivery (Entrega):** A materialização do valor. Onde códigos são gerados e colocados em produção. Responde à pergunta: *"Estamos construindo da forma certa e rápida?"*

### B. Engenharia de Software & QA (Shift-Left Testing)
Princípio fundamental da Garantia de Qualidade focado na prevenção precoce. A tese do **Shift-Left** (Mover para a Esquerda) atesta matematicamente que descobrir uma falha lógica, de fluxo ou de regra de negócio durante as fases de desenho estrutural (à esquerda do eixo de um projeto temporal) custa até 100x menos tempo e dinheiro do que descobri-la na fase de correção pós-código (à direita).

### C. Filosofia Lean e Sistema Toyota de Produção
Foco obsessivo na redução de **Overheads** (processos paralelos, falta de foco da equipe e alinhamentos improdutivos sem saída de valor), mapeando a cadeia de valor ponta a ponta para eliminar gargalos (Bugs e Correções eternas).

---

## 2. Métricas de Sofisticação e Inferências

Os futuros relatórios devem transmutar linhas de planilhas nestes três grandes **indicadores de eficiência (KPIs)**:

### 2.1 Razão Discovery vs Delivery (D/D Ratio)
A relação central de saúde operacional de uma Squad.

*   **Matemática:** `Total de Horas Discovery ÷ Total de Horas Delivery` (Medido sempre dentro do escopo de um **Épico** específico num horizonte trimestral/semestral).
*   **Faixa Ideal:** Estudos globais apontam que a eficiência máxima ocorre numa faixa de **0.15 a 0.25** (ou seja, 15% a 25% do tempo do time consumido em planejamento rigoroso, e o restante em execução impecável).
*   **Inferências no Relatório:**
    *   **D/D < 0.10 (Sinal de Alerta):** A equipe está codificando "no escuro". Gera altíssima probabilidade de refação, débitos técnicos arquiteturais acelerados e estouro de horas na ponta em atividades de QA (Teste).
    *   **D/D > 0.35 (Analysis Paralysis):** A equipe está sofrendo de lentidão decisória, burocracia excessiva no levantamento de hipóteses ou falta de capacidade gerencial para fechar escopo e iniciar o desenvolvimento.

### 2.2 Taxa de Qualidade e a Teoria da Curva em "U" (Bugs vs Planejamento)
Baseado na epistemologia do Shift-Left, validamos cruzamentos diretos dentro do Jira:

*   **Matemática:** Cruzar o percentual gasto em **Discovery** (Variável preditora) com a fatia de apontamentos classificados como **Bug/Correção** (Variável dependente), meses depois.
*   **Inferências no Relatório:** Demonstração empírica de que "planejamento não é atraso, é economia de capacidade produtiva". Apontar à área de negócio e parceiros comerciais as razões pelas quais não se pode apertar prazos em fases exploratórias sob a pena severa do aumento direto do Custo Total Operacional (TCO) por falhas em produção.

### 2.3 Taxa de Fricção e Overhead Não-Operacional
Monitora o impacto que a infraestrutura corporativa cobra do tempo das pessoas fundamentais.

*   **Matemática:** Isolar, a partir dos apontamentos, cargas de "Reuniões gerais, alinhamentos 1:1, treinamentos".
*   **Inferências no Relatório:** Se desenvolvedores dedicarem rotineiramente mais de **15-20%** ao Overhead ou PMs/PDs não conseguirem dedicar sequer 50% às tarefas nativas pelas agendas tomadas, reporta-se oficialmente um gargalo na cadeia e processo, dando munição objetiva (ex: "estamos jogando fora 40h de liderança técnica toda semana em reuniões soltas").

---

## 3. Direcionamento Prático para os Novos Relatórios

Diante desses preceitos, a linha de conduta para os modelos locais de inteligência (e scripts em Python) de agora em diante passa a seguir o padrão ouro:

1.  **Cruzar Worklogs e Issue Types:** Toda tarefa exportada deve obrigatoriamente cair num balde semântico (Discovery, Delivery, Qualidade ou Overhead) na fase de parsing.
2.  **Consolidar as Respostas a Nível Épico:** Esqueça a micro-tarefa da semana isolada. A análise precisa abraçar todo o tempo de vida do Épico (3 a 6 meses de exportação) para poder provar o fenômeno elástico da qualidade e do retorno de investimento técnico.
3.  **Financeirizar o Argumento (Lei do Bem e Comercial):** Traduzir horas bem empregadas num relatório em *Poder de Negociação*: tangibilizar monetariamente o quão cara foi a produção da funcionalidade vs estimativa (ROI) e habilitar a Diretoria na recuperação de custos de Pesquisa e Desenvolvimento em subsídios corporativos.
