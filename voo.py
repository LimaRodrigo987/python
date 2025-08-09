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




