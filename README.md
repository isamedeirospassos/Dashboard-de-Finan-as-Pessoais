# 💸 Dashboard de Finanças Pessoais

Um dashboard interativo e clean construído com Python para analisar gastos pessoais. O usuário pode fazer o upload da própria planilha de gastos e visualizar para onde o dinheiro está indo através de gráficos dinâmicos.

## 🚀 Funcionalidades

- **Upload Dinâmico:** Aceita arquivos `.csv` com os dados financeiros do usuário.
- **Visualização de Dados:** Exibição da planilha de forma estruturada e interativa.
- **Gráficos Automáticos:** Gráfico de barras mostrando o consolidado de gastos por categoria.
- **Gerador de Dados:** Inclui um script (`gerar_dados.py`) que cria automaticamente uma base de testes realista com 500 registros.

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** - Linguagem principal.
- **[Streamlit](https://streamlit.io/)** - Criação da interface web e deploy.
- **[Pandas](https://pandas.pydata.org/)** - Leitura, agrupamento e manipulação dos dados CSV.
- **[Plotly](https://plotly.com/python/)** - Geração de gráficos bonitos e interativos.

## 💻 Como rodar o projeto localmente

1. Clone este repositório no seu computador:
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   ```

2. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

3. (Opcional) Para gerar um arquivo de testes (`gastos_500.csv`):
   ```bash
   python gerar_dados.py
   ```

4. Inicie a aplicação:
   ```bash
   streamlit run app.py
   ```

## 🌐 Acesso Online

O projeto está hospedado no Streamlit Community Cloud. Você pode testar a aplicação funcionando ao vivo aqui:
**[Acessar o Dashboard](https://seu-link-do-streamlit.streamlit.app/)**