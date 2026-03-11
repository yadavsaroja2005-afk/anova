import scipy.stats as stats
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# --------------------------
# GROUP DATA
# --------------------------
group1 = [23, 25, 28, 34, 30]
group2 = [19, 20, 22, 15, 23]
group3 = [18, 16, 20, 21, 17]
group4 = [28, 24, 26, 30, 29]

# Combine all data and create group labels
all_data = np.array(group1 + group2 + group3 + group4)
group_labels = (
    ['Group1'] * len(group1) +
    ['Group2'] * len(group2) +
    ['Group3'] * len(group3) +
    ['Group4'] * len(group4)
)

# --------------------------
# ONE-WAY ANOVA
# --------------------------
f_statistic, p_value = stats.f_oneway(group1, group2, group3, group4)

print("One-Way ANOVA Results:")
print(f"F-statistic: {f_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

# --------------------------
# POST-HOC ANALYSIS (Tukey HSD)
# --------------------------
if p_value < 0.05:
    print("\nSignificant difference found! Performing post-hoc analysis...")
    tukey_results = pairwise_tukeyhsd(all_data, group_labels)
    print("\nTukey-Kramer Post-Hoc Test Results:")
    print(tukey_results)
else:
    print("\nNo significant difference found between groups.")
