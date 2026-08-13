# 💸 Dashboard de Finanças Pessoais

Dashboard interativo desenvolvido em **Python** para análise e visualização de gastos pessoais.

A aplicação permite fazer o upload de uma planilha `.csv`, aplicar filtros e analisar os gastos através de indicadores, gráficos interativos e insights automáticos.

🌐 **[Acessar o Dashboard](https://dashboard-financas-pess.streamlit.app/)**

## 📊 Funcionalidades

* 📂 Upload de arquivos `.csv`
* 🔎 Filtros por categoria e mês
* 💰 Resumo dos principais indicadores:

  * Total de gastos
  * Média de gastos
  * Maior gasto
  * Quantidade de transações
* 📅 Evolução mensal dos gastos
* 📈 Comparação mensal em gráfico de barras
* 🏷️ Distribuição dos gastos por categoria
* 💳 Comparação entre custos fixos e variáveis
* 🥇 Ranking dos 10 maiores gastos
* 🚨 Identificação de gastos acima da média
* 💡 Insight automático sobre a categoria com maior gasto
* 📋 Visualização dos gastos filtrados

## 🤖 Gerador de Dados

O projeto também possui um **gerador de arquivos CSV** para criar uma base de dados fictícia utilizada nos testes do dashboard.

O gerador foi criado com **apoio de IA** e utiliza Python para gerar automaticamente **500 registros de gastos**, incluindo diferentes categorias, datas, descrições, valores e tipos de gastos.

O script utiliza:

```python
import csv
import random
from datetime import datetime, timedelta
```

As categorias utilizadas são:

* Alimentação
* Transporte
* Lazer
* Moradia
* Saúde

O arquivo gerado possui as seguintes colunas:

```text
Data
Categoria
Tipo
Descricao
Valor
```

Os gastos também são classificados entre **Fixo** e **Variável**.

## 🛠️ Tecnologias

* **Python** - Desenvolvimento da aplicação e geração dos dados
* **Pandas** - Tratamento, transformação e análise dos dados
* **Plotly** - Criação dos gráficos interativos
* **Streamlit** - Desenvolvimento da interface do dashboard
* **CSV** - Armazenamento e importação dos dados

## 📁 Estrutura do Projeto

```text
📦 Dashboard-de-Finan-as-Pessoais
│
├── app.py
├── gerar_dados.py
├── gastos_500.csv
├── requirements.txt
└── README.md
```

## 💻 Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/isamedeirospassos/Dashboard-de-Finan-as-Pessoais.git
```

### 2. Entre na pasta do projeto

```bash
cd Dashboard-de-Finan-as-Pessoais
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Gere uma base de dados para teste

```bash
python gerar_dados.py
```

O comando irá gerar o arquivo:

```text
gastos_500.csv
```

### 5. Execute o dashboard

```bash
streamlit run app.py
```

## 🌐 Projeto Online

Você pode testar o dashboard diretamente pelo Streamlit:

**[🚀 Acessar Dashboard de Finanças Pessoais](https://dashboard-financas-pess.streamlit.app/)**

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como parte dos meus estudos em **Python e Análise de Dados**, com foco em transformar dados financeiros em informações visuais e fáceis de interpretar.

Durante o desenvolvimento, foram praticados conceitos de:

* Manipulação e tratamento de dados com Pandas
* Conversão e organização de datas
* Agrupamento e agregação de dados
* Criação de filtros interativos
* Criação de indicadores
* Visualização de dados
* Desenvolvimento de dashboards com Streamlit
* Criação de gráficos interativos com Plotly
* Geração de dados fictícios para testes
* Uso de IA como ferramenta de apoio no desenvolvimento

## 👩‍💻 Desenvolvido por

**Isabella Passos**

[GitHub](https://github.com/isamedeirospassos)
