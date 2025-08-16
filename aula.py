import pandas as pd
import matplotlib.pyplot as plt
import os

# Nome do arquivo
ARQUIVO = "dados_aula_escola.csv"

# Criar o CSV com dados de exemplo (caso não exista)
if not os.path.exists(ARQUIVO):
    
    pd.DataFrame(dados).to_csv(ARQUIVO, index=False)
    print(f"Arquivo '{ARQUIVO}' criado.\n")

# --- 1. Ler o CSV e mostrar as 5 primeiras linhas ---
df = pd.read_csv(ARQUIVO)
df["Idade"] = pd.to_numeric(df["Idade"], errors="coerce")
df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")

print("# 1. Primeiras 5 linhas:")
print(df.head())

# --- 2. Informações gerais e resumo estatístico ---
print("\n# 2. Informações gerais:")
df.info()

print("\n# 3. Resumo estatístico:")
print(df.describe())

# --- 4. Filtros e consultas ---
print("\n# 4.1 Alunos com nota acima de 7:")
print(df[df["Nota"] > 7])

print("\n# 4.2 Nome e nota dos alunos do 9º ano:")
print(df[df["Ano_Serie"] == "9º"][["Nome", "Nota"]])

print("\n# 4.3 Quantidade de alunos com idade ≥ 14:")
print((df["Idade"] >= 14).sum())

print("\n# 4.4 Alunos com idade < 10 e nota < 5:")
print(df[(df["Idade"] < 10) & (df["Nota"] < 5)])

# --- 5. Agrupamentos e estatísticas ---
print("\n# 5.1 Média das notas por série:")
media_por_serie = df.groupby("Ano_Serie")["Nota"].mean()
print(media_por_serie)

print("\n# 5.2 Série com maior média de notas:")
print(f"{media_por_serie.idxmax()} com média {media_por_serie.max():.2f}")

print("\n# 5.3 Idade média de alunos com nota > 8:")
print(df[df["Nota"] > 8]["Idade"].mean())

# --- 6. Ordenações ---
print("\n# 6.1 Alunos em ordem decrescente de nota:")
print(df.sort_values(by="Nota", ascending=False))

print("\n# 6.2 Alunos mais novos primeiro e por nota:")
print(df.sort_values(by=["Idade", "Nota"]))

# --- 7. Manipulação de colunas ---
print("\n# 7.1 Adicionando coluna 'Situação':")
df["Situação"] = df["Nota"].apply(lambda x: "Aprovado" if x >= 6 else "Reprovado")
print(df[["Nome", "Nota", "Situação"]])

print("\n# 7.2 Alunos aprovados no 7º ano:")
print(df[(df["Ano_Serie"] == "7º") & (df["Situação"] == "Aprovado")])

# --- 8. Desafios extras ---
print("\n# 8.1 Maior nota e quem tirou:")
print(df[df["Nota"] == df["Nota"].max()])

print("\n# 8.2 Quantidade de alunos por série:")
print(df["Ano_Serie"].value_counts())

print("\n# 8.3 Gráfico de barras da média de notas por série:")
media_por_serie.sort_index().plot(
    kind="bar",
    title="Média de Notas por Série",
    ylabel="Nota Média",
    xlabel="Série"
)
plt.tight_layout()
plt.show()

# --- Gráficos extras ---


# Gráfico de barras da quantidade de alunos por idade
plt.figure()
df["Idade"].value_counts().sort_index().plot(
    kind="bar",
    title="Quantidade de Alunos por Idade",
    xlabel="Idade",
    ylabel="Número de Alunos"
)
plt.tight_layout()
plt.show()

# Gráfico de pizza dos alunos aprovados x reprovados
plt.figure()
df["Situação"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    title="Proporção de Alunos Aprovados e Reprovados"
)
plt.ylabel("")  # Remove label y
plt.tight_layout()
plt.show()
