import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ========== CONFIGURAÇÕES INICIAIS ==========
st.set_page_config(page_title="Dashboard de Voos", layout="wide")
st.title("✈️ Dashboard de Análise de Voos")
st.markdown("Visualização de dados com filtros por companhia aérea.")

# ========== CARREGAMENTO DOS DADOS ==========
df = pd.read_csv("dados_voos.csv")
df["Rota"] = df["Origem"] + " → " + df["Destino"]

# ========== FILTRO POR COMPANHIA ==========
companhias = sorted(df["Companhia"].unique())
companhia_selecionada = st.selectbox("Selecione uma companhia aérea:", companhias)

df_filtrado = df[df["Companhia"] == companhia_selecionada]

# ========== ESTATÍSTICAS ==========
st.subheader("📊 Estatísticas da Companhia Selecionada")

preco_medio = df_filtrado["Preco_R$"].mean()
mediana_duracao = df_filtrado["Duracao_min"].median()
atraso_medio = df_filtrado["Atraso_min"].mean()
preco_max = df_filtrado["Preco_R$"].max()
preco_min = df_filtrado["Preco_R$"].min()

mes_maior_preco = df_filtrado.groupby("Mes")["Preco_R$"].mean().idxmax() if not df_filtrado.empty else "N/A"
origem_maior_atraso = df_filtrado.groupby("Origem")["Atraso_min"].mean().idxmax() if not df_filtrado.empty else "N/A"
rotas_repetidas = df_filtrado["Rota"].value_counts()[df_filtrado["Rota"].value_counts() > 1]
rota_mais_frequente = rotas_repetidas.idxmax() if not rotas_repetidas.empty else "Nenhuma"

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Preço Médio", f"R$ {preco_medio:.2f}")
    st.metric("🕒 Duração Mediana", f"{mediana_duracao:.0f} min")

with col2:
    st.metric("⏱️ Atraso Médio", f"{atraso_medio:.2f} min")
    st.metric("📈 Preço Máx", f"R$ {preco_max:.2f}")

with col3:
    st.metric("📉 Preço Mín", f"R$ {preco_min:.2f}")
    st.metric("📅 Mês mais caro", f"{mes_maior_preco}")

st.markdown(f"🛫 **Origem com maior atraso médio:** {origem_maior_atraso}")
st.markdown(f"🔁 **Rota mais frequente:** {rota_mais_frequente}")

# ========== GRÁFICOS ==========
st.subheader("📈 Visualizações")

# Gráfico 1 - Preço médio por companhia (com todos os dados, não só filtrado)
st.markdown("#### Preço médio por companhia aérea")
fig1, ax1 = plt.subplots(figsize=(6, 4))
df.groupby("Companhia")["Preco_R$"].mean().sort_values().plot(kind='bar', ax=ax1)
ax1.set_ylabel("Preço (R$)")
ax1.set_title("Preço Médio por Companhia")
st.pyplot(fig1)


# Gráfico 2 - Boxplot de preços por mês
st.markdown("#### Distribuição de Preços por Mês")
fig2, ax2 = plt.subplots()
sns.boxplot(x="Mes", y="Preco_R$", data=df_filtrado, ax=ax2)
ax2.set_title("Boxplot de Preço por Mês")
st.pyplot(fig2)

# Gráfico 3 - Histograma de duração
st.markdown("#### Duração dos Voos")
fig3, ax3 = plt.subplots()
sns.histplot(df_filtrado["Duracao_min"], bins=10, kde=True, ax=ax3)
ax3.set_xlabel("Duração (min)")
ax3.set_title("Histograma da Duração dos Voos")
st.pyplot(fig3)

# Gráfico 4 - Heatmap
st.markdown("#### Correlação entre Variáveis")
fig4, ax4 = plt.subplots()
sns.heatmap(df_filtrado[["Preco_R$", "Duracao_min", "Atraso_min"]].corr(), annot=True, cmap="coolwarm", ax=ax4)
ax4.set_title("Mapa de Calor")
st.pyplot(fig4)

# ========== TABELA DE DADOS ==========
st.subheader("📋 Dados da Companhia Selecionada")
st.dataframe(df_filtrado.reset_index(drop=True))


"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# Cole seus dados aqui (mantendo a estrutura CSV)
from io import StringIO


df = pd.read_csv("dados_voos.csv")

# Estatísticas e insights
df["Rota"] = df["Origem"] + " → " + df["Destino"]
preco_medio = df["Preco_R$"].mean()
mediana_duracao = df["Duracao_min"].median()
companhia_maior_preco = df.groupby("Companhia")["Preco_R$"].mean().idxmax()
atraso_medio = df["Atraso_min"].mean()
preco_max, preco_min = df["Preco_R$"].max(), df["Preco_R$"].min()
mes_maior_preco = df.groupby("Mes")["Preco_R$"].mean().idxmax()
origem_maior_atraso = df.groupby("Origem")["Atraso_min"].mean().idxmax()
companhia_menor_duracao = df.groupby("Companhia")["Duracao_min"].mean().idxmin()
rotas_repetidas = df["Rota"].value_counts()[df["Rota"].value_counts() > 1]
rota_mais_frequente = rotas_repetidas.idxmax() if not rotas_repetidas.empty else "Nenhuma"

# Diferença entre preço médio mais caro e mais barato
medias_por_companhia = df.groupby("Companhia")["Preco_R$"].mean()
dif_preco = medias_por_companhia.max() - medias_por_companhia.min()

# Outliers
q1, q3 = df["Preco_R$"].quantile([0.25, 0.75])
iqr = q3 - q1
lim_sup = q3 + 1.5 * iqr
outliers = df[df["Preco_R$"] > lim_sup]["Companhia"].unique()

# Gráficos
medias_por_companhia.sort_values().plot(kind='bar', title="Preço médio por companhia", ylabel="R$ Preço")
plt.tight_layout()
plt.show()

sns.boxplot(x="Mes", y="Preco_R$", data=df)
plt.title("Distribuição de preços por mês")
plt.show()

sns.histplot(df["Duracao_min"], bins=10, kde=True)
plt.title("Histograma de duração dos voos")
plt.xlabel("Duração (min)")
plt.show()

sns.heatmap(df[["Preco_R$", "Duracao_min", "Atraso_min"]].corr(), annot=True, cmap="coolwarm")
plt.title("Mapa de calor: correlações")
plt.show()

# Resultados
print(f"Preço médio: R${preco_medio:.2f}")
print(f"Mediana da duração: {mediana_duracao} min")
print(f"Companhia com maior preço médio: {companhia_maior_preco}")
print(f"Atraso médio: {atraso_medio:.2f} min")
print(f"Preço máximo: R${preco_max:.2f}, mínimo: R${preco_min:.2f}")
print(f"Mês com maior preço médio: {mes_maior_preco}")
print(f"Origem com maior atraso médio: {origem_maior_atraso}")
print(f"Companhia com menor duração média: {companhia_menor_duracao}")
print(f"Rota mais frequente: {rota_mais_frequente}")
print(f"Diferença de preço médio entre mais cara e mais barata: R${dif_preco:.2f}")
print(f"Companhias com preços fora do padrão: {list(outliers)}")
"""