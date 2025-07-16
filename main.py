# %% [markdown]
# # Tratamento de Dados de Satélite
# **Equipe:** Daniel, Jones, Kleberson, Murilo

# %% [markdown]
# ## Apresentação
# ### O Telescópio Kepler e a Descoberta de Exoplanetas
# 
# #### Introdução
# - O Telescópio Espacial Kepler, lançado pela NASA em 2009, foi projetado para descobrir exoplanetas, <br>
#   ou seja, planetas que orbitam estrelas fora do nosso sistema solar.
# - A missão Kepler teve como objetivo principal explorar a estrutura e a diversidade dos sistemas <br>
# planetários, contribuindo significativamente para a nossa compreensão do universo.
# 
# #### Objetivos da Missão Kepler
# - **Exploração da Diversidade Planetária**: Investigar a variedade de planetas e suas características.
# - **Identificação de Exoplanetas**: Detectar planetas em zonas habitáveis, onde a vida poderia existir.
# - **Coleta de Dados**: Fornecer dados extensivos que apoiem futuras missões da NASA e pesquisas científicas.
# 
# #### O Conjunto de Dados
# - O conjunto de dados contém informações sobre aproximadamente **3.373 exoplanetas confirmados**.
# - Inclui dados coletados durante as missões Kepler e K2, abrangendo vários anos de observação.
# - **Informações Disponíveis**:
#   - Nome da estrela hospedeira
#   - Características dos planetas (tamanho, massa, composição)
#   - Parâmetros orbitais (período orbital, distância da estrela)
#   - Métodos de descoberta (transito, velocidade radial)
#   - Propriedades estelares (tipo de estrela, temperatura)
# 
# #### Importância dos Dados
# - Os dados do Kepler são cruciais para entender a formação e evolução dos sistemas planetários.
# - Permitem a análise estatística da distribuição de exoplanetas em diferentes tipos de estrelas e suas características.
# - A pesquisa com esses dados pode revelar padrões que ajudam a identificar quais sistemas planetários têm maior probabilidade de abrigar vida.
# 
# 

# %% [markdown]
# ## Análise dos Dados

# %% [markdown]
# **Bibliotecas necessárias**

# %%
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# %% [markdown]
# **Resultados obtidos**

# %%
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

# %% [markdown]
# ### Proporções

# %% [markdown]
# **Planetas cujo raio se assemelha ao da Terra**
# 
# Como o raio de cada planeta está medido em **raios de júpiter**, faremos uma conversão do raio da Terra:
# 
# $R_{Terra} = 6378,1~km = \frac{6378,1}{69911} \approx 0,09123$ raios de júpiter

# %%
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

# %% [markdown]
# Calculando IC de 95% para a média dos raio:
# 
# $n = 380, \alpha = 0,05, \hat{p} \approxeq 0,13335$
# 
# $IC: 0,13335 \pm z_{0,025} \cdot \sqrt{\frac{0,13335 \cdot (1-0,13335)}{380}} $

# %%
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

# %% [markdown]
# Estamos 95% confiantes de que a proporção populacional verdadeira está no intervalo $[0,0992;~0,1675]$.

# %% [markdown]
# **Planetas cujo a massa se assemelha ao da  Terra**
# 
# Como o massa de cada planeta também está medido em **raios de júpiter**, faremos uma conversão da massa da Terra:
# 
# $M_{Terra} = 5,9722 \cdot 10^{24}~kg = \frac{5,9722 \cdot 10^{24}}{1,898 \cdot 10^{27}} \approx 0,003147$ massas de júpiter

# %%
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

menores = (df_m[coluna] < x).mean() * 100
print(f"Proporção (planetas menos massivo que a Terra): {menores:.2f}%")
print(f"Proporção (planetas mais massivo que a Terra): {100 - menores:.2f}%")
print(f"Proporção com raio médio de todos os planetas: {media/df_filtrado[coluna].mean():.5f}")

# %% [markdown]
# Calculando IC de 95% para a média das massa:
# 
# $n = 380, \alpha = 0,05, \hat{p} \approxeq 0,00605$
# 
# $IC: 0,00605 \pm z_{0,025} \cdot \sqrt{\frac{0,00605 \cdot (1-0,00605)}{380}} $

# %%
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

# %% [markdown]
# Com isso, concluímos que a proporção da massa populacional dos planetas semelhantes a Terra está no intervalo $[-0,0017;~0,0139]$.

# %% [markdown]
# **Planetas cujo a excentridade orbital (achatamento da órbita) se assemelha a da  Terra**
# 
# $e_{Terra} \approx 0,0167$ 

# %%
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

# %% [markdown]
# Calculando IC de 95% para a média das Excentricidades:
# 
# $n = 380, \alpha = 0,05, \hat{p} \approxeq 0,19751$
# 
# $IC: 0,19751 \pm z_{0,025} \cdot \sqrt{\frac{0,19751 \cdot (1-0,19751)}{380}} $

# %%
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

# %% [markdown]
# Com isso, concluímos que a proporção da excentridade populacional dos planetas semelhantes a Terra está no intervalo $[0,1518;~0,2433]$.

# %% [markdown]
# **Planetas cujo o período orbital (tempo de revolução em torno da estrela) se assemelha ao da Terra**
# 
# $P_{Terra} \approx 365,25 \text{ dias (0,25 = +4 horas)}$
# 
# Nesta análise, buscamos identificar exoplanetas que apresentem **períodos orbitais próximos ao da Terra**, isto é, o tempo que levam para dar uma volta completa em torno de sua estrela hospedeira.
# 
# Para isso, consideramos planetas cujo período orbital esteja dentro de uma faixa de tolerância de ±20 dias, ou seja:
# 
# $[345,25 \leqslant P_{exoplaneta} \leqslant 385,25]$
# 
# ### 🔢 Parâmetros utilizados:
# 
# - **Coluna analisada:** `pl_orbper`
# - **Valor de referência (Terra):** $365{,}25$ dias
# - **Tolerância ($\pm$):** 20 dias
# - **Intervalo considerado:** [345,25 ; 385,25] dias
# - **Total de planetas após filtro prévio:** `len(df_filtrado)`
# 
# A seguir, serão calculadas:
# - A **quantidade de planetas** com período semelhante ao da Terra;
# - A **proporção** em relação ao total da amostra;
# - A **média**, **variância** e **desvio padrão** desses planetas;
# - Um **histograma** ilustrando a distribuição dos períodos;
# - E o **intervalo de confiança (95%)** da razão entre a média dos semelhantes e a média global.
# 

# %%
# --------------------- FILTRO PARA PERÍODO ORBITAL ------------------------

# Criando um novo DataFrame apenas com os dados relevantes para a análise do período orbital

df_orbper = df_original[
    (df_original['pl_orbper'].notna()) &                          # período orbital válido
    (df_original['pl_hostname'].str.strip() != '') &             # nome da estrela não vazio
    (df_original['st_teff'].notna())                             # temperatura da estrela válida
]

print(f"Total de planetas com dados suficientes para análise do período orbital: {len(df_orbper)}")


# %%
# ---------------------- PERÍODO ORBITAL -----------------------

# Parâmetros
coluna = "pl_orbper"
x      = 365.25     # valor de referência (dias)
tol    = 20         # tolerância: ±20 dias

# Filtro para planetas com período semelhante ao da Terra
mask_p = (df_orbper[coluna] - x).abs() <= tol
df_p = df_orbper[mask_p]

# Média
media = df_p[coluna].mean()

# Variância amostral
variancia_amostral = df_p[coluna].var(ddof=1)

# Desvio padrão amostral
desvio_amostral = df_p[coluna].std(ddof=1)

print(f"Cerca de {len(df_p[coluna])} planetas possuem período orbital semelhante ao da Terra!")
print(f"Proporção dos planetas encontrados: {(len(df_p)/len(df_orbper)) * 100 :.2f}%")
print(f"Média do período orbital: {media:.7f} dias")
print(f"Variância (amost.): {variancia_amostral:.7f}")
print(f"Desvio-padrão (amost.): {desvio_amostral:.7f}")

# --- plotando histograma ---
plt.figure(figsize=(8, 5))
df_p[coluna].plot.hist(bins=20, color="skyblue", edgecolor="black")
plt.title("Histograma dos Períodos Orbitais")
plt.xlabel("Período Orbital (dias)")
plt.ylabel("Frequência")
plt.grid(alpha=0.7)
plt.show()

# Proporções de planetas menores e maiores que o período da Terra
menores = (df_orbper[coluna] < x).mean() * 100
maiores = (df_orbper[coluna] > x).mean() * 100
print(f"Proporção (planetas com período menor que a Terra): {menores:.2f}%")
print(f"Proporção (planetas com período maior que a Terra): {maiores:.2f}%")
print(f"Proporção com período médio em relação ao total: {media/df_orbper[coluna].mean():.5f}")


# %%
# Intervalo de confiança para média (forma correta para comparação entre médias)
media_total = df_orbper[coluna].mean()
n = len(df_p)

# Erro padrão da média
se = df_p[coluna].std(ddof=1) / math.sqrt(n)

# Parâmetros do IC
alpha = 0.05
z = norm.ppf(1 - alpha / 2)

# Margem de erro e IC
me = z * se
ic_lower = media - me
ic_upper = media + me

print(f"IC 95% para a média do período orbital (em dias): [{ic_lower:.2f}, {ic_upper:.2f}]")


# %% [markdown]
# ## Conclusão
# - O Telescópio Kepler revolucionou nossa compreensão dos exoplanetas e da diversidade dos sistemas planetários.
# - O conjunto de dados disponível oferece uma rica fonte de informações para pesquisas futuras e análises estatísticas.
# - Através do uso de ferramentas como Jupyter Notebooks, podemos explorar e visualizar esses dados, contribuindo para o avanço da astronomia e da astrobiologia.


