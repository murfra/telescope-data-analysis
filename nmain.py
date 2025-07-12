import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# -------------------- TAMANHO -------------------------------------
############### primeira celula ################
# 1) Lê o CSV para um DataFrame
df_original = pd.read_csv('data/planets.csv')

# Suponha que a coluna que você quer checar se chama 'col_importante'

# 2) Máscara para filtrar os dados mantendo só as linhas onde 'col_importante' NÃO é NaN
mask = (
    (df_original['pl_hostname'] != '') &
    (df_original['pl_dens'].notna()) &
    (df_original['pl_orbeccen'].notna()) &
    (df_original['pl_bmassj'] != '') &
    (df_original['pl_radj'].notna()) &
    (df_original['pl_orbper'].notna()) &
    (df_original['st_teff'].notna())
)

"""
Alternativa usando dropna para as colunas numéricas e filtragem específica para as strings:

python

Copiar código
# 1) remove linhas com NaN nas colunas numéricas
df2 = df.dropna(subset=['pl_dens','pl_radj','pl_orbper','st_teff'])

# 2) filtra as colunas de string para não-vazias
mask_str = (df2['pl_hostname'].str.strip() != '') & (df2['pl_bmassj'].str.strip() != '')
df_filtrado = df2[mask_str]
Assim você garante que só sobram linhas em que todas as colunas que você listou estejam efetivamente preenchidas.
"""

df_filtrado = df_original[mask]

# Alternativamente, você também pode "dropar" as linhas faltantes diretamente:
# df.dropna(subset=['col_importante'], inplace=True)

# 3) A partir daqui use df_filtrado para suas análises
# print(df_filtrado.head(5))
print(f"População que será utilizada nos testes: {len(df_filtrado)}")
##############################################

###################### celula 2 ######################
# Parâmetros
coluna = "pl_radj"
x      = 0.09123     # valor alvo (float)
tol    = 0.1        # tolerância, ex.: ±0.1

mask_r = (df_filtrado[coluna] - x).abs() <= tol
df_r = df_filtrado[mask_r]

# Média
media = df_r[coluna].mean()

# Variância amostral
variancia_amostral = df_r[coluna].var(ddof=1)

# Desvio padrão
desvio_amostral = df_r[coluna].std(ddof=1)

print(f"Cerca de {len(df_r[coluna])} planetas possuem o raio semelhante ao da Terra!")
# Mostra quantos, dos planetas encontrados, possuem raio semelhante ao da Terra
print(f"Proporção dos planetas encontrados: {len(df_r)/len(df_filtrado) :.7f}")
print(f"Média do raio dos planetas: {media:.7f}")
print(f"Variância (amost.): {variancia_amostral:.7f}")
print(f"Desvio-padrão (amost.): {desvio_amostral:.7f}")

# --- plotando histograma ---
plt.figure(figsize=(8, 5))

df_r[coluna].plot.hist(bins=20, color="skyblue", edgecolor="black")
plt.title("Histograma dos Raios")
plt.xlabel("Raio")
plt.ylabel("Frequência")
plt.grid(alpha=0.7)
plt.show()

# df_fitrado: dados na tabela que possuem um valor de raio
menores = (df_filtrado[coluna] < x).mean() * 100
maiores = (df_filtrado[coluna] > x).mean() * 100
print(f"Proporção (planetas menores que a Terra): {menores:.2f}%")
print(f"Proporção (planetas maiores que a Terra): {maiores:.2f}%\n")
print(f"Proporção com raio médio de todos os planetas: {media/df_filtrado[coluna].mean():.5f}")
######################################################

##################### IC dos raio ####################

# Média dos raios semelhantes à terra / Média dos raios de todos os planetas
p_hat = media/df_filtrado[coluna].mean()
alpha = 0.05
z = norm.ppf(1 - alpha/2)

# Margem de erro
se = math.sqrt(p_hat * (1 - p_hat) / len(df_filtrado))
me = z * se

ic_lower = p_hat - me
ic_upper = p_hat + me

print(f"IC 95% (Normal): [{ic_lower:.4f}, {ic_upper:.4f}]")
################################################

# --------------------- MASSA ---------------------------------

########### Célula das massas ##################
# Parâmetros
coluna = "pl_bmassj"
x      = 0.003147     # valor alvo (float)
tol    = 0.01       # tolerância, ex.: ±0.01

mask_m = (df_filtrado[coluna] - x).abs() <= tol
df_m = df_filtrado[mask_m]

# Média
media = df_m[coluna].mean()

# Variância amostral
variancia_amostral = df_m[coluna].var(ddof=1)

# Desvio padrão
desvio_amostral = df_m[coluna].std(ddof=1)
 
print(f"Cerca de {len(df_m[coluna])} planetas possuem massa semelhante a da Terra!")
print(f"Proporção dos planetas encontrados: {(len(df_m)/len(df_filtrado)) * 100 :.2f}%")
print(f"Média da massa dos planetas: {media:.7f}")
print(f"Variância (amost.): {variancia_amostral:.7f}")
print(f"Desvio-padrão (amost.): {desvio_amostral:.7f}")
 
serie = df_m[coluna]
 
# --- plotando histograma ---
plt.figure(figsize=(8, 5))
 
serie.plot.hist(bins=20, color="skyblue", edgecolor="black")
plt.title("Histograma das Massas")
plt.xlabel("Massa")
plt.ylabel("Frequência")
plt.grid(alpha=0.7)
plt.show()

menores = (df_r[coluna] < x).mean() * 100
print(f"Proporção (planetas menos massivo que a Terra): {menores:.2f}%")
print(f"Proporção (planetas mais massivo que a Terra): {100 - menores:.2f}%")
print(f"Proporção com raio médio de todos os planetas: {media/df_filtrado[coluna].mean():.5f}")
###############################################

################# IC de Massa #################

# Média das massa semelhantes à terra / Média das massa de todos os planetas
p_hat = media/df_filtrado[coluna].mean()
alpha = 0.05
z = norm.ppf(1 - alpha/2)

# Margem de erro
se = math.sqrt(p_hat * (1 - p_hat) / len(df_filtrado))
me = z * se

ic_lower = p_hat - me
ic_upper = p_hat + me

print(f"IC 95% (Normal): [{ic_lower:.4f}, {ic_upper:.4f}]")
################################################

# ------------------------ EXCENTRICIDADE ORBITAL (ACHATAMENTO DA ÓRBITA) ------------------------------

########### Célula da Excentridade Orbital ##################
# Parâmetros
coluna = "pl_orbeccen"
x      = 0.0167     # valor alvo (float)
tol    = 0.01       # tolerância, ex.: ±0.01

mask_e = (df_filtrado[coluna] - x).abs() <= tol
df_e = df_filtrado[mask_e]

# Média
media = df_e[coluna].mean()

# Variância amostral
variancia_amostral = df_e[coluna].var(ddof=1)

# Desvio padrão
desvio_amostral = df_e[coluna].std(ddof=1)
 
print(f"Cerca de {len(df_e[coluna])} planetas possuem excentridade orbital semelhante a da Terra!")
print(f"Proporção dos planetas encontrados: {(len(df_e)/len(df_filtrado)) * 100 :.2f}%")
print(f"Média da excentridade dos planetas: {media:.7f}")
print(f"Variância (amost.): {variancia_amostral:.7f}")
print(f"Desvio-padrão (amost.): {desvio_amostral:.7f}")
 
serie = df_e[coluna]
 
# --- plotando histograma ---
plt.figure(figsize=(8, 5))
 
serie.plot.hist(bins=20, color="skyblue", edgecolor="black")
plt.title("Histograma das Excentridades")
plt.xlabel("Excentridade Orbital")
plt.ylabel("Frequência")
plt.grid(alpha=0.7)
plt.show()

menores = (df_r[coluna] < x).mean() * 100
print(f"Proporção (planetas com excentridade menor que a Terra): {menores:.2f}%")
print(f"Proporção (planetas com excentridade maior que a Terra): {100 - menores:.2f}%")
print(f"Proporção com excentridade média de todos os planetas: {media/df_filtrado[coluna].mean():.5f}")
###############################################

################# IC de Excentridade #################

# Média das excentridades semelhantes à terra / Média das excentricidades orbitais de todos os planetas
p_hat = media/df_filtrado[coluna].mean()
alpha = 0.05
z = norm.ppf(1 - alpha/2)

# Margem de erro
se = math.sqrt(p_hat * (1 - p_hat) / len(df_filtrado))
me = z * se

ic_lower = p_hat - me
ic_upper = p_hat + me

print(f"IC 95% (Normal): [{ic_lower:.4f}, {ic_upper:.4f}]")
################################################


