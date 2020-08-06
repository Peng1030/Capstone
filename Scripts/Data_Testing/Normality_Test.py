#The null hypothesis is that all the values were sampled from a Gaussian distribution


k, norm = mstats.normaltest([Test[col] for col in Test.columns], 1)
print("P-value:", norm[1])
print("  ")

if norm[1] < alpha_value:
    print("Reject NULL hypothesis - Not normal distribution")
    normal = False
if norm[1] > alpha_value:
    print("Accept NULL hypothesis - A Normal distribution")
    normal = True
