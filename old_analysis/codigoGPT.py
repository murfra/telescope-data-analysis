# Vamos gerar os gráficos conforme combinamos, a partir dos dados enviados.
# Como não consigo acessar o arquivo diretamente aqui, vou criar um pequeno DataFrame de exemplo
# simulando a estrutura real para mostrar como seriam os gráficos.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Simular dados semelhantes aos que você enviou
np.random.seed(0)
n = 200
df = pd.DataFrame({
    'koi_score': np.clip(np.random.normal(0.8, 0.2, n), 0, 1),
    'koi_disposition': np.random.choice(['CONFIRMED', 'FALSE POSITIVE'], n, p=[0.6, 0.4]),
    'koi_period': np.random.exponential(10, n),
    'koi_prad': np.random.normal(2.5, 1.0, n).clip(0.5, 15),
    'kepler_name': np.random.choice([None, 'Kepler-22 b', 'Kepler-10 c', 'Kepler-186 f'], n, p=[0.5, 0.2, 0.2, 0.1]),
    'koi_teq': np.random.normal(800, 300, n).clip(200, 2000)
})

# 1️⃣ Histograma do koi_score
plt.figure(figsize=(8,4))
plt.hist(df['koi_score'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuição do koi_score')
plt.xlabel('koi_score')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# 2️⃣ Boxplot do koi_period por koi_disposition
plt.figure(figsize=(8,4))
df.boxplot(column='koi_period', by='koi_disposition')
plt.title('Período orbital por status')
plt.ylabel('Período (dias)')
plt.suptitle('')
plt.tight_layout()
plt.show()

# 3️⃣ Histograma do koi_prad
plt.figure(figsize=(8,4))
plt.hist(df['koi_prad'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribuição do raio do planeta (koi_prad)')
plt.xlabel('Raio (em Terras)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# 4️⃣ Scatter plot: raio vs temperatura
plt.figure(figsize=(8,4))
plt.scatter(df['koi_prad'], df['koi_teq'], alpha=0.6, c='orange', edgecolor='black')
plt.title('Relação entre raio e temperatura dos planetas')
plt.xlabel('Raio (koi_prad)')
plt.ylabel('Temperatura de equilíbrio (koi_teq)')
plt.tight_layout()
plt.show()

# 5️⃣ Gráfico de barras: quantidade de confirmados e falsos positivos
counts = df['koi_disposition'].value_counts()
plt.figure(figsize=(6,4))
counts.plot(kind='bar', color=['steelblue', 'salmon'])
plt.title('Quantidade de planetas por status')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
