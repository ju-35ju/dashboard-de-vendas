import streamlit as st

# CONFIGURAÇÃO
st.set_page_config(
    page_title="Dashboard de Vendas",
    layout="wide"
)

# HERO
st.title("📊 Dashboard Empresarial")

st.subheader("Análise estratégica de vendas")

st.write("""
Este projeto apresenta uma análise de dados empresariais utilizando:

- Python
- Streamlit
- Pandas
- Visualização de dados

O sistema permite:
- análise de vendas
- filtros dinâmicos
- gráficos
- indicadores estratégicos
""")

# MÉTRICAS VISUAIS
col1, col2, col3 = st.columns(3)

col1.metric("Clientes", "999+")
col2.metric("Pedidos", "500+")
col3.metric("Categorias", "3")

# BOTÃO
st.success("Projeto funcionando online 🚀")
