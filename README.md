# 💸 Dashboard de Finanças Pessoais

Dashboard interativo desenvolvido em **Python** para análise de gastos pessoais.

A aplicação permite importar uma planilha `.csv` e visualizar os gastos de forma simples e dinâmica, facilitando a identificação de onde o dinheiro está sendo utilizado.

🌐 **[Acessar o Dashboard](https://dashboard-financas-pess.streamlit.app/)**

## 🚀 Funcionalidades

* 📂 Upload de arquivos `.csv`
* 📊 Visualização dos dados financeiros
* 📈 Gráficos interativos de gastos por categoria
* 🔎 Agrupamento e análise dos gastos
* 🧪 Gerador de dados para testes
* 🤖 Gerador de arquivos CSV desenvolvido com apoio de IA

### Gerador de dados

O projeto possui um script `gerar_dados.py` responsável por criar uma base de dados fictícia para testes.

O gerador utiliza as bibliotecas:

```python
import csv
import random
from datetime import datetime, timedelta
```

Com ele, é possível gerar automaticamente arquivos `.csv` com registros de gastos, facilitando os testes do dashboard sem a necessidade de criar uma planilha manualmente.

## 🛠️ Tecnologias

* **Python**
* **Pandas**
* **Streamlit**
* **Plotly**
* **CSV**

## 💻 Como executar

Clone o repositório:

```bash
git clone https://github.com/isamedeirospassos/Dashboard-de-Finan-as-Pessoais.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Gere uma base de dados para teste:

```bash
python gerar_dados.py
```

Execute o dashboard:

```bash
streamlit run app.py
```

## 🌐 Projeto online

Teste o projeto diretamente pelo Streamlit:

**[🚀 Dashboard de Finanças Pessoais](https://dashboard-financas-pess.streamlit.app/)**

## 👩‍💻 Sobre o projeto

Projeto desenvolvido como parte dos meus estudos em **Python e Análise de Dados**, com foco em manipulação de dados, visualização e construção de aplicações interativas.
