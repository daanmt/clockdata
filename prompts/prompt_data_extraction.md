# Prompt: Extração e Profiling dos Dados

> **Para:** IA Executora (Delivery)
> **Contexto:** Projeto POPS — Análise de Banco de Horas da Omie

---

## Sua Tarefa

Você é a IA executora do Projeto POPS. Sua tarefa é:

1. **Ler o README.md** na raiz do projeto para entender a estrutura
2. **Executar o script** `scripts/extract_and_explore.py`
3. **Analisar o output** gerado em `output/data_profile.md`
4. **Validar** o dicionário de dados em `docs/data_dictionary.md`
5. **Atualizar** o dicionário com os nomes reais das colunas

## Passo a Passo

### 1. Setup do Ambiente
```bash
cd [raiz do projeto]
pip install -r scripts/requirements.txt
```

### 2. Executar o Profiling
```bash
python scripts/extract_and_explore.py
```

### 3. Analisar o Output
Abrir `output/data_profile.md` e verificar:
- [ ] Quais colunas existem em cada arquivo?
- [ ] Os nomes estão em PT ou EN?
- [ ] Existem colunas de Épico nos worklogs?
- [ ] Existe coluna de Issue Type para classificar Discovery/Delivery?
- [ ] Qual a coluna de horas (hours, logged, time spent)?
- [ ] Existem colunas de data para análise temporal?

### 4. Atualizar Dicionário de Dados
Editar `docs/data_dictionary.md` substituindo as colunas hipotéticas pelas reais.

### 5. Reportar Gaps
Liste quais dados estão **ausentes** e são necessários para a análise:
- Mapeamento pessoa → Squad
- Dados de períodos anteriores
- Custo/hora do time

## Critérios de Sucesso
- `output/data_profile.md` gerado sem erros
- `docs/data_dictionary.md` atualizado com schema real
- Lista de gaps documentada

## Contexto Adicional
Leia estes documentos ANTES de executar:
- `core/project_overview.md` — entender o projeto
- `core/team_roles.md` — saber quem é quem
- `docs/discovery_questions.md` — saber o que estamos investigando
