#Clean the data for the splitting
fill_NaN = Imputer(missing_values=np.nan, strategy='mean', axis=1)
imputed_DF = pd.DataFrame(fill_NaN.fit_transform(Data))
imputed_DF.columns = Data.columns
imputed_DF.index = Data.index


Xvar = imputed_DF.drop(target, axis=1)
Yvar = imputed_DF.loc[:, target]

#Split it
samplesize = int(np.floor(Xvar.shape[0]/2))

train_sample = np.random.choice(Xvar.shape[0], replace=False, size=samplesize)
test_sample = np.random.choice(Xvar.loc[~Xvar.index.isin(train_sample)].shape[0], replace=False, size=samplesize)

X_train = Xvar.loc[train_sample]
Y_train = Yvar.loc[train_sample]
X_test = Xvar.loc[test_sample]
Y_test = Yvar.loc[test_sample]

#In case there are issues
#X_train.head(10)
#Y_train.head(10)
#X_test.head(10)
#Y_test.head(10)
