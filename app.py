import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configurar o título da página
st.set_page_config(page_title="Meu Dashboard Financeiro", layout="wide")
st.title("💸 Dashboard de Finanças Pessoais")

# 2. Criar o botão de Upload
arquivo_upload = st.file_uploader("Faça o upload da sua planilha de gastos", type=["csv"])

# 3. Só executa o resto do código SE o usuário tiver enviado um arquivo
if arquivo_upload is not None:

    df = pd.read_csv(arquivo_upload)

    # Mostrar a tabela na tela
    st.subheader("Visualização da Planilha")
    st.dataframe(df, use_container_width=True)

    # Criar um gráfico de gastos por categoria
    st.subheader("Gastos por Categoria")
    
    # Agrupamos os dados por Categoria e somamos os Valores
    gastos_por_categoria = df.groupby("Categoria")["Valor"].sum().reset_index()
    
    # Criamos o gráfico com Plotly
    grafico = px.bar(gastos_por_categoria, x="Categoria", y="Valor", color="Categoria")
    
    # Exibimos o gráfico no Streamlit
    st.plotly_chart(grafico, use_container_width=True)

else:
    # Mensagem que aparece enquanto o usuário não envia o arquivo
    st.info("👆 Por favor, envie um arquivo CSV com as colunas: Data, Categoria, Descricao e Valor para visualizar o dashboard.")