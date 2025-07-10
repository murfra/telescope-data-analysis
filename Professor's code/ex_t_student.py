import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

# 1. Gerar amostra aleatória
np.random.seed(42)
n = 15
mu_real = 100
sigma_real = 20
amostra = np.random.normal(loc=mu_real, scale=sigma_real, size=n)

valores_df = pd.DataFrame({
    "Valores Aleatórios": np.round(amostra, 2)
})

# 2. Calcular estatísticas da amostra
media_amostral = np.mean(amostra)
desvio_amostral = np.std(amostra, ddof=1)
gl = n - 1  # graus de liberdade

# 3. Calcular intervalo de confiança de 95% usando t-Student
alpha = 0.05
t_critico = stats.t.ppf(1 - alpha/2, df=gl)
erro = t_critico * (desvio_amostral / np.sqrt(n))
ic_t = (media_amostral - erro, media_amostral + erro)

# 4. Exibir resultados no console
print("\nAmostra de valores:", valores_df) 
print(f"Média amostral: {media_amostral:.2f}")
print(f"Desvio padrão amostral: {desvio_amostral:.2f}")
print(f"t crítico (gl = {gl}): {t_critico:.3f}")
print(f"Erro da estimativa: {erro:.2f}")
print(f"IC 95% (t-Student): [{ic_t[0]:.2f} ; {ic_t[1]:.2f}]")


# 5. Gerar gráfico do intervalo de confiança
plt.figure(figsize=(8, 4))
plt.axhline(0, color='gray', linewidth=0.5)
plt.errorbar(media_amostral, 0, xerr=erro, fmt='o', color='blue', capsize=10, label='IC 95% (t-Student)')
plt.plot(media_amostral, 0, 'ro', label='Média amostral')

# Anotações e layout
plt.title('Intervalo de Confiança 95% usando t-Student')
plt.yticks([])
plt.xlabel('Valores')
plt.xlim(ic_t[0] - 5, ic_t[1] + 5)
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()