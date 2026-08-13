import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configurar o título da página
st.set_page_config(page_title="Meu Dashboard Financeiro", layout="wide")
st.title("💸 Dashboard de Finanças Pessoais")

# 2. Carregar os dados (Pandas)
# Lemos o arquivo CSV que criamos
df = pd.read_csv("gastos.csv")

# 3. Mostrar a tabela na tela
st.subheader("Visualização da Planilha")
st.dataframe(df, use_container_width=True)

# 4. Criar um gráfico de gastos por categoria
st.subheader("Gastos por Categoria")

# Agrupamos os dados por Categoria e somamos os Valores
gastos_por_categoria = df.groupby("Categoria")["Valor"].sum().reset_index()

# Criamos o gráfico com Plotly
grafico = px.bar(gastos_por_categoria, x="Categoria", y="Valor", color="Categoria")

# Exibimos o gráfico no Streamlit
st.plotly_chart(grafico, use_container_width=True)