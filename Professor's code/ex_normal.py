import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Configurações iniciais
np.random.seed(120)  # para reprodutibilidade
n = 100              # tamanho da amostra
mu_real = 70         # média populacional verdadeira
sigma_real = 12      # desvio padrão populacional verdadeiro

# Gerar 100 valores aleatórios com distribuição normal
amostra = np.random.normal(loc=mu_real, scale=sigma_real, size=n)

# Criar DataFrame com os valores gerados
valores_df = pd.DataFrame({
    "Valores Aleatórios": np.round(amostra, 2)
})

# Estatísticas da amostra
media_amostral = np.mean(amostra) 
desvio_amostral = np.std(amostra, ddof=1)
variancia_amostral = desvio_amostral**2

# Intervalo de Confiança (95%) usando distribuição normal (σ conhecido)
z_critico = stats.norm.ppf(0.975)  # z_{alpha/2} para 95%
erro_normal = z_critico * (sigma_real / np.sqrt(n))
n=((z_critico *sigma_real)/ erro_normal)**2  # Tamanho da amostra necessário para o IC
ic_normal = (media_amostral - erro_normal, media_amostral + erro_normal)

# Exibir resultados
# Exibir os 10 primeiros (você pode mudar para .head(100) para mostrar todos)
print(valores_df.head(10))  # Exibe as primeiras 10 linhas
print("Z_c=", z_critico)
print("Tamanho da amostra (n):", n)
print("Média amostral:", round(media_amostral, 2))
print("Variância amostral:", round(variancia_amostral, 2))
print("\nIC 95% com distribuição normal (σ conhecido):")
print(f"[{ic_normal[0]:.2f} ; {ic_normal[1]:.2f}]")
print(n)

# Criar histograma com densidade
plt.figure(figsize=(10, 6))
sns.histplot(amostra, bins=15, stat='density', color='lightblue', edgecolor='black', label='Frequência')

# Curva normal ajustada
x = np.linspace(min(amostra), max(amostra), 200)
y = norm.pdf(x, loc=media_amostral, scale=desvio_amostral)
plt.plot(x, y, color='red', linewidth=2, label='Distribuição Normal Ajustada')

# Marcar média
plt.axvline(media_amostral, color='blue', linestyle='--', label=f'Média = {media_amostral:.2f}')

# Títulos e legendas
plt.title("Distribuição de Frequência com Curva Normal Ajustada")
plt.xlabel("Valores")
plt.ylabel("Densidade")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()