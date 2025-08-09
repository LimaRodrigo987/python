
import numpy as np
# estatistica 
from statistics import mode

# Sequencia numerica
dados = [10, 12, 10, 14, 15, 15, 20]

# media -> Tendencia Central
media = np.mean(dados)
# mediana -> Valor Central, robusto contra outliers
mediana = np.median(dados)
# Moda -> Valor mais frequente
moda = mode(dados)
# Desvio Padrao -> Dispersão dos Dados
desvio_padrao = np.std(dados)
# Variância -> Quadrado do Desvio padrão
variancia = np.var(dados)

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Desvio Padrão:{desvio_padrao}")
print(f"Variância:{variancia}")
