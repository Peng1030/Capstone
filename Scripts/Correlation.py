#Spearman Correlation

Rho,Pval = stats.spearmanr(Data)

sns.heatmap(pd.DataFrame(Rho), xticklabels=list(Data), yticklabels=list(Data))

sns.heatmap(pd.DataFrame(Pval), xticklabels=list(Data), yticklabels=list(Data))

Rho = pd.DataFrame(Rho, index=list(Data), columns=list(Data))
PVal = pd.DataFrame(Pval, index=list(Data), columns=list(Data))

Target = pd.concat([Rho.loc[:,target], PVal.loc[:,target]], axis=1,  join='inner')
Target.columns = ["Rho", "PValue"]

Target = Target.loc[lambda Target: Target.PValue < alpha_value, :].sort_values(by='Rho', ascending=0)
print(Target)
regvar = Target.index.values.tolist()
