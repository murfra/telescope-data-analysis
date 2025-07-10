import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Carregar os dados (ajuste o nome do arquivo se necessário)
df = pd.read_csv('dados.csv')

# 1️⃣ Resumo geral
print("Total de registros:", len(df))
print("Colunas:", df.columns)

# 2️⃣ Média e desvio padrão do koi_score
mean_score = df['koi_score'].mean()
std_score = df['koi_score'].std()
print(f"Média do koi_score: {mean_score:.2f}")
print(f"Desvio padrão do koi_score: {std_score:.2f}")

# 3️⃣ Histograma do koi_score
plt.figure(figsize=(8,4))
plt.hist(df['koi_score'], bins=1000, color='skyblue', edgecolor='black')
plt.title('Distribuição do koi_score')
plt.xlabel('koi_score')
plt.ylabel('Frequência')
plt.show()

# 4️⃣ Diferença entre CONFIRMED e FALSE POSITIVE no koi_score
confirmed = df[df['koi_disposition']=='CONFIRMED']['koi_score']
false_positive = df[df['koi_disposition']=='FALSE POSITIVE']['koi_score']

# Teste t de Student
t_stat, p_value = stats.ttest_ind(confirmed, false_positive, equal_var=False)
print(f"Teste t: t={t_stat:.2f}, p={p_value:.4f}")

# 5️⃣ Boxplot do koi_period
plt.figure(figsize=(8,4))
df.boxplot(column='koi_period', by='koi_disposition')
plt.title('Período orbital por status')
plt.ylabel('Período (dias)')
plt.suptitle('')
plt.show()

# 6️⃣ Curiosidades
# - Média do raio planetário (koi_prad) por status
mean_radius_confirmed = df[df['koi_disposition']=='CONFIRMED']['koi_prad'].mean()
mean_radius_fp = df[df['koi_disposition']=='FALSE POSITIVE']['koi_prad'].mean()
print(f"Raio médio CONFIRMED: {mean_radius_confirmed:.2f} Terras")
print(f"Raio médio FALSE POSITIVE: {mean_radius_fp:.2f} Terras")

# - Quantos confirmados receberam nome
total_confirmed = len(df[df['koi_disposition']=='CONFIRMED'])
named_confirmed = df[(df['koi_disposition']=='CONFIRMED') & (df['kepler_name'].notna())]
percent_named = len(named_confirmed) / total_confirmed * 100
print(f"{percent_named:.1f}% dos planetas confirmados têm nome oficial")

# - Temperatura média
mean_teq_confirmed = df[df['koi_disposition']=='CONFIRMED']['koi_teq'].mean()
mean_teq_fp = df[df['koi_disposition']=='FALSE POSITIVE']['koi_teq'].mean()
print(f"Temperatura média CONFIRMED: {mean_teq_confirmed:.0f} K")
print(f"Temperatura média FALSE POSITIVE: {mean_teq_fp:.0f} K")
