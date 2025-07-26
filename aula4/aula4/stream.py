# Biliboteca para criação de Dashboards
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df= pd.read_csv("aula4/vendas_loja.csv")
df["Receita"] = df["Quantidade"] * df["Preço_unitario"]
df["Data"] = pd.to_datetime(df["Data"])
df["Mês"] = df["Data"].dt.to_period("M")

st.title("Dashboards de Vendas")

# Infos principais
# f "R$ {}" -> Format(String)
# R$ 2764.32
# df["Receita"].sum() -> :,.2f -> .2f
st.metric("Total de Vendas",f"R${df["Receita"].sum():,.2f}")
st.metric("Média por venda",f"R${df["Receita"].mean():,.2f}")

# Filtro por categoria
categorias = df["Categoria"].unique() # Categoria é unicas
categoria_selecionada = st.selectbox("Selecione a categoria :",categorias)
# Categoria == CategoriaSelecionada
df_filtrado =df[df["Categoria"] == categoria_selecionada] 

# Gráfico por produto
st.subheader("Receita por Produto")
# Criar uma figura, que vai ser o gráfico

#Grafico por mes
st.subheader("Receita Mensal")
fig2, ax2 = plt.subplots()
df.groupby("Mês")["Receita"].sum().plot(ax=ax2)
st.pyplot(fig2)

