#Pandas , utilizando para DataSciene ,Machine learning e 
#Analise e Estatistica
import pandas as pd
import matplotlib.pyplot as plt

#ler o csv
df= pd.read_csv("aula5/venda_lojas.csv")

#Nomes das colunas
# criar coluna chamada receita
df["Receita"] = df["Quantidade"] * df["Preço"]

#sum -> somar
total_receita=df["Receita"].sum() 
print("Total de vendas R$",total_receita) # Total de receita faturado

#mean - media
media_receita =df["Receita"]. mean()
print("Média da Receita R$",media_receita)

# Produto mais vendido em quantidade
produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()
# idxmax -> pegar o maior valor
print("Produto mais vendido:", produto_mais_vendido)

# Categoria com maior receita
categoria_top_receita =df.groupby("Categoria")["Receita"].sum().idxmax()
print("Categoria com a maior receita: ",categoria_top_receita)

#Gráfico de barras - Receita por categoria
df.groupby("Categoria")["Receita"].sum().plot(kind="bar",title="Receita por Categoria")
plt.ylabel("Receita (R$)")
plt.tight_layout() #finalizar layout
plt.show() #exibir o gráfico

# Gráfico de linha - Receita por Mês
#DateTime
df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] =df["Data"].dt.to_period("M") # Capturando o M -> Mes da data
#Group by
df.groupby("Mes")["Receita"].sum().plot(kind="line",title="Receita Mensal")
plt.ylabel("Receita R$")
plt.xlabel("Mês")
plt.tight_layout()
plt.show()

receita_mes =df.groupby("Categoria")["Receita"].sum()
plt.figure(figsize=(8, 5))
receita_mes.plot(kind="line", marker ="o",color="green", title="Receita Mensal")
plt.ylabel("Receita (R$)")
plt.xlabel("Mês")
plt.tight_layout()
plt.show()

receita_por_categoria =df.groupby("Categoria")["Receita"].sum()
plt.figure(figsize=(6, 6))
plt.pie(receita_por_categoria, labels=receita_por_categoria.index, autopct="%1.1f%%",startangle=90,shadow=True)
plt.title("Categoria Vendas Totais")
plt.tight_layout()
plt.show()

 