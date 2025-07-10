import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Gerar amostra binária aleatória
np.random.seed(1000)
n = 500 # Tamanho da amostra
p_real = 0.65 # Proporção real de sucessos 
amostra = np.random.binomial(n=1, p=p_real, size=n) # Gerar amostra binomial

# Calcular estatísticas
sucessos = np.sum(amostra) # Contar sucessos (1's)
fracassos = n - sucessos # Contar fracassos (0's)
# Proporção amostral e intervalo de confiança
p_hat = sucessos / n
alpha = 0.05 # Nível de significância (intervalo de confiança de 95%)
# Cálculo do intervalo de confiança usando a distribuição normal
z_critico = stats.norm.ppf(1 - alpha/2)
erro = z_critico * np.sqrt(p_hat * (1 - p_hat) / n) #Erro padrão
ic = (p_hat - erro, p_hat + erro) # Intervalo de confiança

# Dados
categorias = ['Fracasso (0)', 'Sucesso (1)'] # Categorias para o gráfico
frequencias = [fracassos, sucessos] # Frequências de fracassos e sucessos
porcentagens = [f"{(f/n)*100:.1f}%" for f in frequencias] # Porcentagens formatadas

# Exibir resultados
print("Dados da Amostra Binária (0 = fracasso, 1 = sucesso):")
print(pd.Series(amostra).to_string(index=False))
print(f"\nTamanho da amostra: {n}")
print(f"Número de sucessos: {sucessos}")
print(f"Proporção amostral (p̂): {p_hat:.3f}")
print(f"Intervalo de Confiança 95%: [{ic[0]:.3f} ; {ic[1]:.3f}]")

# Gráfico de barras com rótulo
plt.figure(figsize=(6, 4))
bars = plt.bar(categorias, frequencias, color=['gray', 'green'])

# Adicionar rótulos no topo das barras
for bar, label in zip(bars, porcentagens):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 1, label,
             ha='center', va='bottom', fontsize=10)

# Estética
plt.title('Frequência de Sucessos e Fracassos na Amostra')
plt.ylabel('Frequência')
plt.ylim(0, max(frequencias) + 10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()