#Note - dummies the variables selected
Dummy = Data.loc[:, To_Dummy]
Dummy = pd.get_dummies(Dummy, prefix=None, prefix_sep=' - ')

#Drops those columns and put the dummy variables back in place
Data = Data.drop(list(Data.select_dtypes(include=['O']).columns), axis=1)
Data = pd.concat([Data, Dummy], axis=1, join='inner')
