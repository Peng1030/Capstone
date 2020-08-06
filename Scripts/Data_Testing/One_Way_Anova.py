#The ANOVA test has important assumptions that must be satisfied in order for the associated p-value to be valid.

#- The samples are independent.
#- Each sample is from a normally distributed population.
#- The population standard deviations of the groups are all equal. This property is known as homoscedasticity.

#If these assumptions are not true for a given set of data, it may still be possible to use the Kruskal-Wallis H-test although with some loss of power.
print("Can one use ANOVA?")
print("  ")
print("Independent: ", independent)
print("Normal: ", normal)
print("StdDevEq: ", StdDevEq)
print("  ")

if independent != True or normal != True or StdDevEq != True:
    print("The assumptions to use ANOVA have not been met.")
    print("")
    ANOVA=False

else:
    F, pval = mstats.f_oneway([Test[col] for col in Test.columns])
    print("F-statistic:", F)
    print("P-Value:", pval)
    print("  ")
    if pval < alpha_value:
        print("Reject NULL hypothesis - Significant differences exist between groups.")
        Sig = True
    if pval > alpha_value:
        print("Accept NULL hypothesis - No significant difference between groups.")
        Sig = False
