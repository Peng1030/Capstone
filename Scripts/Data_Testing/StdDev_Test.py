#reminder: the p-value is the probability of observing a certain result from your sample or a result more extreme, assuming the null hypothesis is true

#null hypothesis that all input samples are from populations with equal variances

T, pval = stats.bartlett(*[Test[col] for col in Test.columns])

print("T-statistic:", T)
print("P-Value:", pval)
print("  ")

if np.isnan(pval):
    print("Error")
    StdDevEq = False
if pval < alpha_value:
    print("Reject NULL hypothesis - Significant differences exist between the standard deviations of the groups.")
    StdDevEq = False
if pval > alpha_value:
    print("Accept NULL hypothesis - No significant difference between the standard deviations of the groups.")
    StdDevEq = True
