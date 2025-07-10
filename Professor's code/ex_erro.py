import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- Dados originais ---
dados = np.array([
    14.1, 14.5, 15.5, 16.0, 16.0, 16.7, 16.9, 17.1, 17.5, 17.8,
    17.8, 18.1, 18.2, 18.3, 18.3, 19.0, 19.2, 19.4, 20.0, 20.0,
    20.8, 20.8, 21.0, 21.5, 23.5, 27.5, 27.5, 28.0, 28.3, 30.0,
    30.0, 31.6, 31.7, 31.7, 32.5, 33.5, 33.9, 35.0, 35.0, 35.0,
    36.7, 40.0, 40.0, 41.3, 41.7, 47.5, 50.0, 51.0, 51.8, 54.4,
    55.0, 57.0
])

# --- Estatísticas amostrais ---
media = np.mean(dados)
desvio_padrao = np.std(dados, ddof=1)

# --- Padronização ---
dados_z = (dados - media) / desvio_padrao

# --- Distribuição normal ajustada ---
x1 = np.linspace(min(dados) - 5, max(dados) + 5, 500)
y1 = norm.pdf(x1, loc=media, scale=desvio_padrao)

# --- Distribuição normal padrão ---
x2 = np.linspace(-4, 4, 500)
y2 = norm.pdf(x2, loc=0, scale=1)

# --- Plot dos dois gráficos lado a lado ---
fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: Dados originais com normal ajustada
axs[0].hist(dados, bins=10, density=True, alpha=0.6, color='gray', edgecolor='black', label='Dados originais')
axs[0].plot(x1, y1, color='blue', label='Normal ajustada')
axs[0].set_title("Dados Originais com Curva Normal Ajustada")
axs[0].set_xlabel("DCP (mm/fluxo)")
axs[0].set_ylabel("Densidade")
axs[0].legend()
axs[0].grid(True)

# Gráfico 2: Dados padronizados com normal padrão
axs[1].hist(dados_z, bins=10, density=True, alpha=0.6, color='gray', edgecolor='black', label='Dados padronizados (Z)')
axs[1].plot(x2, y2, color='green', label='Distribuição Normal Padrão')
axs[1].set_title("Dados Padronizados com Curva Normal Padrão")
axs[1].set_xlabel("z")
axs[1].set_ylabel("Densidade")
axs[1].legend()
axs[1].grid(True)

# Layout e exibição
plt.tight_layout()
plt.show()