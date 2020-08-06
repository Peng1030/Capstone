
#Added, Age, Years Played, Country of Birth, First and Last Names, Weight, Height, Bat Hand, Throwing Hand

Trim_Master = Master[['playerID','birthYear', 'birthCountry', 'weight','height','bats','throws','debut']]
Data = Salaries.merge(Trim_Master,how='left', left_on='playerID', right_on='playerID')
Data['age'] = Data['yearID'] - Data['birthYear']
Data['debut'] = pd.to_datetime(Data['debut'])
Data['debutYear'] = pd.DatetimeIndex(Data['debut']).year
Data['yearsPlayed'] = Data['yearID'] - Data['debutYear']
Data = Data.drop(['birthYear', 'debut', 'debutYear'], axis=1)


#Adding in the appearance chart
Data = pd.merge(Data, Appearances,  how='left', left_on=['yearID','teamID', 'playerID', 'lgID'], right_on = ['yearID','teamID','playerID','lgID'])
Data = Data.drop(['G_batting', 'G_defense'], axis=1)


#Remove the pitchers and catchers
Data = Data[Data["G_p"] == 0]
Data = Data[Data["G_c"] == 0]
Data = Data.drop(["G_p", "G_c"], axis=1)


#Combining postions to groups
Data['Outfield'] = Data['G_lf'] + Data['G_cf'] + Data['G_rf']
Data['Infield'] = Data['G_1b'] + Data['G_2b'] + Data['G_ss'] + Data['G_3b']
Data['Pinch'] = Data['G_ph'] + Data['G_pr']
Data['DH'] = Data['G_dh']

Data = Data.drop(['G_lf', 'G_cf', 'G_rf', 'G_1b', 'G_2b', 'G_ss', 'G_3b', 'G_ph', 'G_pr', 'G_dh', 'G_of' ], axis=1)


#Baseline to games
Data['Outfield'] = Data['Outfield']/Data['G_all']
Data['Infield'] = Data['Infield']/Data['G_all']
Data['Pinch'] = Data['Pinch']/Data['G_all']
Data['DH'] = Data['DH']/Data['G_all']

#Add fielding stats
Data = pd.merge(Data, Fielding,  how='left', left_on=['yearID','teamID', 'playerID', 'lgID'], right_on = ['yearID','teamID','playerID','lgID'])
Data = Data.drop(['stint', 'POS', 'PB', 'WP', 'SB', 'CS', 'ZR', 'GS_y'], axis=1)

#Converting to the stats to per game
Data['Games'] = Data['InnOuts']/3/9
Data[['POg','Ag', 'Eg', 'DPg']] = Data[['PO','A', 'E', 'DP']].divide(Data.Games, axis=0).fillna(0)
Data = Data.drop(['InnOuts', 'PO','A', 'E', 'DP'], axis=1)


#Add Batting stats
Data = pd.merge(Data, Batting,  how='left', left_on=['yearID','teamID', 'playerID', 'lgID'], right_on = ['yearID','teamID','playerID','lgID'])
Data = Data.drop(['stint', 'G_y'], axis=1)

#Adding Calc Stats
Data['1B'] = Data['H'].subtract(Data['2B'].subtract(Data['3B'].subtract(Data['HR'])))
Data['SLG'] = (Data['1B'].add(Data['2B']*2).add(Data['3B']*3).add(Data['HR']*4)).divide(Data['AB'])
Data['OBP'] = (Data['H']+Data['BB']+Data['HBP'])/(Data['AB']+Data['BB']+Data['HBP']+Data['SF'])
Data['OPS'] = Data['SLG'] + Data['OBP']


#Dropping stats used in SLG, OBP, and OPS
Data = Data.drop(['R', 'H', '2B', '3B', 'HR', 'RBI', 'SB','CS', 'BB', 'SO', 'IBB', 'HBP', 'SH', 'SF', 'GIDP'], axis=1)
Data = Data.drop(['AB', '1B'], axis=1)

#SLG and OBP are highly corrolated to OPS.
Data = Data.drop(['SLG', 'OBP'], axis=1)

#Too Many Games
Data = Data.drop(['GS_x', 'G_all', 'G_x'], axis=1)


#Remove infs and Nans
Data = Data.replace(np.inf, np.nan)
Data = Data.replace(np.nan, 0)
