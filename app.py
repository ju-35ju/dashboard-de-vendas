import streamlit as st
import pandas as pd

# CONFIGURAÇÃO
st.set_page_config(
    page_title="Painel de Vendas",
    layout="wide"
)

# TÍTULO
st.title("📊 Painel de Vendas")

st.write("Análise de vendas usando Streamlit")

# LER CSV
df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")
st.write(df.columns)

# KPIs
# KPIs
total_vendas = df["Sales"].sum()
total_lucro = 0
total_pedidos = len(df)

col1, col2, col3 = st.columns(3)

col1.metric("Total de Vendas", f"${total_vendas:,.2f}")
col2.metric("Lucro Total", f"${total_lucro:,.2f}")
col3.metric("Pedidos", total_pedidos)

# FILTRO
categoria = st.selectbox(
    "Escolha a categoria",
    df["Category"].unique()
)

df_filtrado = df[df["Category"] == categoria]

# TABELA
st.subheader("Dados Filtrados")
st.dataframe(df_filtrado)

# GRÁFICO
st.subheader("Vendas por Subcategoria")

grafico = df_filtrado.groupby("Sub-Category")["Sales"].sum()

st.bar_chart(grafico)
