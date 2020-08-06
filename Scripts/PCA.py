#Requires a number for PCA var


#Clean the data
fill_NaN = Imputer(missing_values=np.nan, strategy='mean', axis=1)
imputed_DF = pd.DataFrame(fill_NaN.fit_transform(Data))
imputed_DF.columns = Data.columns
imputed_DF.index = Data.index
imputed_DF = imputed_DF.drop(target, 1)

pca = decomposition.PCA(n_components=PCAvar)
pca.fit(imputed_DF)
PCA = pd.DataFrame(pca.transform(imputed_DF))
PCA.index = Data.index

Data = pd.concat([Data[target], PCA], axis=1, join='inner')
