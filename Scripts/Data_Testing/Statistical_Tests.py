#The null hypothesis is that all the values were sampled from a Gaussian distribution


print("Comparing Standard Deviations")
print("")
exec(open("../Scripts/Data_Testing/StdDev_Test.py").read())
print("")
print("")

print("Checking for Normality")
print("")
exec(open("../Scripts/Data_Testing/Normality_Test.py").read())
print("")
print("")

if independent == True:
    print("ANOVA Testing")
    print("")
    exec(open("../Scripts/Data_Testing/One_Way_Anova.py").read())

if ANOVA == False:
    print("Kruskal-Wallis Testing")
    print("")
    exec(open("../Scripts/Data_Testing/kruskalwallis.py").read())
