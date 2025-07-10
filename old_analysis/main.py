import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

df = pd.read_csv('../data/cumulative.csv')

# 1) Estatísticas básicas
score = df['koi_score'].dropna().replace([np.inf, -np.inf], np.nan).dropna()
print("koi_score: média=%.4f  var=%.4f  std=%.4f" %
      (score.mean(), score.var(ddof=1), score.std(ddof=1)))

# 2) Shapiro–Wilk (até 5000 pontos)
shap = score.sample(5000, random_state=42) if len(score) > 5000 else score
W, p_shapiro = stats.shapiro(shap)
print("Shapiro–Wilk: W=%.4f  p-value=%.4f" % (W, p_shapiro))

# 3) t-Student Welch entre CONFIRMED e FALSE POSITIVE
grp1 = df.loc[df.koi_disposition == 'CONFIRMED', 'koi_score'].dropna()
grp2 = df.loc[df.koi_disposition == 'FALSE POSITIVE', 'koi_score'].dropna()
if len(grp1) >= 2 and len(grp2) >= 2 and grp1.var(ddof=1) > 0 and grp2.var(ddof=1) > 0:
    t_stat, p_t = stats.ttest_ind(grp1, grp2, equal_var=False)
    print("t-Student (Welch): t=%.4f  p-value=%.4f" % (t_stat, p_t))
else:
    print("t-test não executado: insuficiência de dados ou variância zero.")

# 4) Plots
sns.set(style="whitegrid", palette="muted")
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Hist + KDE
sns.histplot(score, kde=True, bins=10, ax=axes[0,0], color="skyblue")
axes[0,0].set_title("Histograma e KDE de koi_score")

# QQ-plot
stats.probplot(score, dist="norm", plot=axes[0,1])
axes[0,1].set_title("QQ-plot de koi_score")

# Boxplot
sns.boxplot(
    x='koi_disposition', y='koi_score',
    data=df, ax=axes[1,0],
    color="lightgreen", fliersize=5
)
axes[1,0].set_title("Box-plot: CONFIRMED vs FALSE POSITIVE")
axes[1,0].set_xlabel("")
axes[1,0].set_ylabel("koi_score")

# Barplot
sns.barplot(
    x='koi_disposition', y='koi_score',
    hue='koi_disposition',
    data=df, ax=axes[1,1],
    estimator=np.mean,
    errorbar=("ci", 95),
    dodge=False,
    legend=False,
    capsize=0.1,
    palette=["lightgreen","salmon","skyblue"]
)
axes[1,1].set_title("Média ± 95% CI de koi_score")
axes[1,1].set_xlabel("")
axes[1,1].set_ylabel("koi_score")

plt.tight_layout()
plt.show()
# plt.savefig("koi_score_plots.png", dpi=150)
