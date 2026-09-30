# Análise da Qualidade do Ar em Pequim (Beijing Air Quality Analysis)

Este projeto realiza uma análise exploratória de dados (EDA) e processamento de dados sobre a qualidade do ar em Pequim (Beijing), utilizando dados de múltiplos locais de monitoramento ambiental coletados ao longo de vários anos.

---

## 📌 Origem dos Dados

Os datasets utilizados neste projeto foram obtidos a partir do Kaggle:
* **Fonte do Dataset:** [Kaggle - Beijing Multi-Site Air-Quality Data Set](https://www.kaggle.com/datasets/sid321axn/beijing-multisite-airquality-data-set/code?datasetId=409180&sortBy=voteCount)

Os arquivos brutos estão localizados na pasta `datasets/` e contém leituras horárias de poluentes e variáveis meteorológicas de 12 estações de monitoramento de Pequim de 1º de março de 2013 a 28 de fevereiro de 2017.

---

## 📁 Estrutura do Repositório

```bash
├── datasets/                     # Arquivos CSV brutos por estação de monitoramento
├── prepare_all_datasets.py       # Script para consolidação e preparação dos dados
├── beijing_air_quality_ds.csv    # Dataset unificado e consolidado (gerado pelo script)
├── beijing_air_quality.ipynb    # Jupyter Notebook principal com a análise de dados
├── .venv/                        # Ambiente virtual Python
├── LICENSE                       # Licença do projeto
└── README.md                     # Documentação do projeto
```

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

O projeto foi desenvolvido em **Python 3** utilizando as seguintes ferramentas e bibliotecas instaladas no ambiente virtual (`.venv`):

* **Análise e Manipulação de Dados:**
  * [Pandas](https://pandas.pydata.org/) (v3.0.6)
  * [NumPy](https://numpy.org/) (v2.5.3)
* **Visualização de Dados:**
  * [Matplotlib](https://matplotlib.org/) (v3.11.2)
  * [Seaborn](https://seaborn.pydata.org/) (v0.13.2)
* **Ambiente de Desenvolvimento:**
  * [Jupyter Notebook / IPython](https://jupyter.org/) (ipykernel v7.4.0)

---

## ⚙️ Como Rodar o Projeto

Siga as instruções abaixo para configurar o ambiente e executar as análises.

### 1. Clonar o repositório
```bash
git clone <url-do-repositorio>
cd beijing_air_quality_analisys
```

### 2. Configurar e Ativar o Ambiente Virtual
Se você deseja usar o `.venv` existente ou criar um novo:
```bash
# Para ativar o .venv existente (macOS/Linux)
source .venv/bin/activate

# Para ativar o .venv existente (Windows)
.venv\Scripts\activate
```

### 3. Consolidar os Datasets das Estações
Antes de rodar a análise, é necessário unir os 12 datasets individuais de cada estação em um único arquivo de dados consolidado. Execute o script `prepare_all_datasets.py`:
```bash
python prepare_all_datasets.py
```
Isso gerará o arquivo **`beijing_air_quality_ds.csv`** na raiz do projeto, contendo a combinação de todos os dados agregados com uma nova coluna `datetime` gerada a partir das variáveis de ano, mês, dia e hora.

### 4. Executar o Jupyter Notebook
Para visualizar as análises de forma interativa, inicie o servidor do Jupyter:
```bash
jupyter notebook beijing_air_quality.ipynb
```
Ou abra o arquivo diretamente em sua IDE de preferência (como VS Code ou PyCharm) configurando o Kernel para usar o interpretador do `.venv`.

---

## 📊 Resumo da Análise e Principais Descobertas

O projeto está estruturado em três etapas fundamentais descritas no notebook principal `beijing_air_quality.ipynb`:

### 1) Sanity Check e Tratamento de Dados
* **Criação de Datetime:** Conversão e junção das colunas temporais individuais em uma única série de tempo estruturada.
* **Limpeza e Redundância:** Exclusão de colunas desnecessárias e remoção de registros duplicados.
* **Tratamento de Valores Nulos:** Aplicação de interpolação linear física agrupada por estação de monitoramento (preservando o comportamento local) e correção de nulos residuais através de preenchimento direcional (`ffill` e `bfill`).

### 2) Análise Exploratória de Dados (EDA)
Foco principal na concentração de **PM2.5** (Material Particulado Fino):
* **Sazonalidade Anual:** Observa-se um ciclo sazonal acentuado com picos severos no inverno (Dezembro a Fevereiro), impulsionados pela queima de carvão para aquecimento residencial, e quedas acentuadas no meio do ano (Verão).
* **Ciclo Diário:** A poluição atinge níveis máximos durante a noite (decorrente da menor dispersão e estabilidade atmosférica térmica) e mínimos nas primeiras horas da tarde.
* **Correlação entre Poluentes:** Altíssima correlação positiva entre PM2.5 com PM10 (0.88) e CO (0.78), sugerindo fontes de emissão comuns (ex: combustão veicular e industrial).
* **Impacto Meteorológico:** Fortes indícios de que a velocidade do vento (WSPM) e a ocorrência de chuva (RAIN) funcionam como fatores críticos de dispersão e mitigação da poluição.

### 3) Próximos Passos
* **Engenharia de Recursos (Feature Engineering):** Aplicar técnicas como *One-Hot Encoding* na direção do vento (`wd`) e codificação das estações.
* **Modelagem Preditiva:** Criação e treinamento de modelos de Machine Learning (por exemplo, Regressão, Random Forest ou modelos de Séries Temporais como LSTM/Prophet) para prever as concentrações futuras de PM2.5 com base nas condições climáticas e histórico de poluentes.
