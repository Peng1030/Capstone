#The Kruskal-Wallis test is a nonparametric (distribution free) test, and is used when the assumptions of ANOVA are not met.
#They both assess for significant differences on a continuous dependent variable by a grouping independent variable (with three or more groups).
#In the ANOVA, we assume that distribution of each group is normally distributed and there is approximately equal variance on the scores for each group.
#However, in the Kruskal-Wallis Test, we do not have any of these assumptions.
#Like all non-parametric tests, the Kruskal-Wallis Test is not as powerful as the ANOVA.




H, pval = mstats.kruskalwallis([Test[col] for col in Test.columns])

print("H-statistic:", H)
print("P-Value:", pval)
print("")

if pval < alpha_value:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
    Sig = True
if pval > alpha_value:
    print("Accept NULL hypothesis - No significant difference between groups.")
    Sig = False
