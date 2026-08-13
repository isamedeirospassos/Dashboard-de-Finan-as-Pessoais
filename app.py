import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configurar o título e layout da página
st.set_page_config(page_title="Meu Dashboard Financeiro", layout="wide")
st.title("💸 Dashboard de Finanças Pessoais")

# 2. Criar o botão de Upload na barra lateral para ficar mais limpo
st.sidebar.header("📁 Importar Dados")
arquivo_upload = st.sidebar.file_uploader("Faça o upload da sua planilha (CSV)", type=["csv"])

# 3. Executa o dashboard se o arquivo existir
if arquivo_upload is not None:
    df = pd.read_csv(arquivo_upload)

    # TRATAMENTO DE DADOS
    df["Data"] = pd.to_datetime(df["Data"])
    
    df["Mês"] = df["Data"].dt.to_period("M").astype(str)
    
    # 5. Criar a coluna 'Tipo'
    categorias_fixas = ["Moradia", "Saúde"] 
    df["Tipo"] = df["Categoria"].apply(lambda x: "Fixo" if x in categorias_fixas else "Variável")


    # 4. FILTROS (Barra Lateral)
    st.sidebar.header("🔎 Filtros")
    
    categorias_selecionadas = st.sidebar.multiselect(
        "Selecione as Categorias",
        options=df["Categoria"].unique(),
        default=df["Categoria"].unique()
    )
    
    meses_selecionados = st.sidebar.multiselect(
        "Selecione os Meses",
        options=df["Mês"].unique(),
        default=df["Mês"].unique()
    )

    df_filtrado = df[
        (df["Categoria"].isin(categorias_selecionadas)) & 
        (df["Mês"].isin(meses_selecionados))
    ]


    #1. CARDS COM PRINCIPAIS NÚMEROS 
    st.markdown("### 💰 Resumo Geral")
    col1, col2, col3, col4 = st.columns(4)
    
    total_gasto = df_filtrado["Valor"].sum()
    media_gasto = df_filtrado["Valor"].mean()
    maior_gasto = df_filtrado["Valor"].max()
    qtd_transacoes = df_filtrado["Valor"].count()

    # Formatando para Moeda Brasileira (Substituindo . por ,)
    col1.metric("Total", f"R$ {total_gasto:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    col2.metric("Média de Gastos", f"R$ {media_gasto:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    col3.metric("Maior Gasto", f"R$ {maior_gasto:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    col4.metric("Transações", qtd_transacoes)


    #9. INSIGHTS AUTOMÁTICOS
    if not df_filtrado.empty:
        categoria_mais_gasta = df_filtrado.groupby("Categoria")["Valor"].sum().idxmax()
        pct_maior_cat = (df_filtrado.groupby("Categoria")["Valor"].sum().max() / total_gasto) * 100
        
        st.success(f"💡 **Insight:** Sua maior despesa está na categoria **{categoria_mais_gasta}**, representando **{pct_maior_cat:.1f}%** dos gastos no período filtrado.")


    st.divider()


    # DIVISÃO DA TELA PARA OS GRÁFICOS
    col_esq1, col_dir1 = st.columns(2)

    with col_esq1:
        # 2. GASTOS AO LONGO DO TEMPO
        st.markdown("#### 📅 Evolução Mensal Geral")
        
        gastos_mes_linha = df_filtrado.groupby("Mês")["Valor"].sum().reset_index()
        gastos_mes_linha = gastos_mes_linha.sort_values("Mês")

        fig_linha = px.line(gastos_mes_linha, x="Mês", y="Valor", markers=True)
        st.plotly_chart(fig_linha, use_container_width=True)

    with col_dir1:
        #7. COMPARAÇÃO MENSAL POR CATEGORIA
        st.markdown("#### 📈 Gastos por Mês e Categoria")

        gastos_mes_cat = df_filtrado.groupby(["Mês", "Categoria"])["Valor"].sum().reset_index()
        gastos_mes_cat = gastos_mes_cat.sort_values("Mês") 

        fig_mes_cat = px.bar(gastos_mes_cat, x="Mês", y="Valor", color="Categoria")
        st.plotly_chart(fig_mes_cat, use_container_width=True)


    col_esq2, col_dir2 = st.columns(2)

    with col_esq2:
        # 3. DISTRIBUIÇÃO POR CATEGORIA
        st.markdown("#### 🏷️ Distribuição por Categoria")
        gastos_cat = df_filtrado.groupby("Categoria")["Valor"].sum().reset_index()

        fig_donut = px.pie(gastos_cat, values="Valor", names="Categoria", hole=0.4) 
        st.plotly_chart(fig_donut, use_container_width=True)

    with col_dir2:
        # 5. GASTOS POR TIPO 
        st.markdown("#### 💳 Custos Fixos x Variáveis")
        gastos_tipo = df_filtrado.groupby("Tipo")["Valor"].sum().reset_index()
        fig_tipo = px.pie(gastos_tipo, values="Valor", names="Tipo", color="Tipo", 
                          color_discrete_map={"Fixo": "red", "Variável": "green"})
        st.plotly_chart(fig_tipo, use_container_width=True)


    st.divider()


    col_esq3, col_dir3 = st.columns(2)

    with col_esq3:
        # 6. RANKING DOS MAIORES GASTOS
        st.markdown("#### 🥇 Top 10 Maiores Gastos")
        top_10 = df_filtrado.nlargest(10, "Valor")[["Data", "Categoria", "Descricao", "Valor"]]

        st.dataframe(top_10, hide_index=True, use_container_width=True)

    with col_dir3:
        #8. IDENTIFICAÇÃO DE GASTOS ACIMA DA MÉDIA
        st.markdown("#### 🚨 Atenção: Gastos Acima da Média")
        acima_media = df_filtrado[df_filtrado["Valor"] > media_gasto]
        st.warning(f"Você possui **{len(acima_media)}** gastos individuais que superam a sua média geral de R$ {media_gasto:.2f}.")
        st.dataframe(acima_media[["Data", "Descricao", "Valor"]].sort_values("Valor", ascending=False), hide_index=True, use_container_width=True)

else:
    st.info("👆 Abra a barra lateral à esquerda e faça o upload da sua planilha CSV (Data, Categoria, Descricao, Valor) para gerar seu Dashboard Analytics.")