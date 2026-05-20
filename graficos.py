import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CONFIGURAÇÃO
st.set_page_config(
    page_title="Gráficos",
    layout="wide"
)

st.title("📈 Página de Gráficos")

# CARREGAR DADOS
df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

# VENDAS POR CATEGORIA
vendas_categoria = (
    df.groupby("Category")["Sales"]
    .sum()
)

# GRÁFICO DE BARRAS
st.subheader("Vendas por Categoria")

st.bar_chart(vendas_categoria)

# GRÁFICO DE PIZZA
st.subheader("Participação por Categoria")

fig, ax = plt.subplots()

ax.pie(
    vendas_categoria,
    labels=vendas_categoria.index,
    autopct='%1.1f%%'
)

st.pyplot(fig)