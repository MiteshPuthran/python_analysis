import pandas as pd
from ipykernel import kernelapp as app
from pandas import Series, DataFrame
a = pd.read_csv('..\\Assignment 3\Data\\movies_awards.csv') #reading the data from the CSV file

frame = DataFrame(a, columns=['Awards']) # selecting the column needed for processing

#frame['AwardsWon'] = frame[frame['Awards'].str.contains("win")]
frame['AwardsWon'] = frame['Awards'].str.extract('(\d+) win', expand=True) # extracting the required keyword from the string for further processing using the extract method
frame['AwardsNominated'] = frame['Awards'].str.extract('(\d+) nomination', expand=True)
frame['PrimeAwardsWon']= frame['Awards'].str.extract('Won (\d+) Primetime', expand=True)
frame['PrimeAwardsNominated']= frame['Awards'].str.extract('Nominated for (\d+) Primetime', expand=True)
frame['BaftaAwardsWon']= frame['Awards'].str.extract('Won (\d+) BAFTA', expand=True)
frame['BaftaAwardsNominated']= frame['Awards'].str.extract('Nominated for (\d+) BAFTA', expand=True)
frame['OscarAwardsWon']= frame['Awards'].str.extract('Won (\d+) Oscar', expand=True)
frame['OscarAwardsNominated']= frame['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True)
frame['GoldenGlobeAwardsWon']= frame['Awards'].str.extract('Won (\d+) Golden Globe', expand=True)
frame['GoldenGlobeAwardsNominated']= frame['Awards'].str.extract('Nominated for (\d+) Golden Globe', expand=True)

frame2 = frame.fillna(0) #replacing all the NaN values with 0

frame2['AwardsWon'] = frame2['AwardsWon'].astype(str).astype(int) # converting the values into string or integer as required
frame2['AwardsNominated'] = frame2['AwardsNominated'].astype(str).astype(int) 
frame2['PrimeAwardsWon'] = frame2['PrimeAwardsWon'].astype(str).astype(int)
frame2['PrimeAwardsNominated'] = frame2['PrimeAwardsNominated'].astype(str).astype(int)
frame2['BaftaAwardsWon'] = frame2['BaftaAwardsWon'].astype(str).astype(int) 
frame2['BaftaAwardsNominated'] = frame2['BaftaAwardsNominated'].astype(str).astype(int)
frame2['OscarAwardsWon'] = frame2['OscarAwardsWon'].astype(str).astype(int) 
frame2['OscarAwardsNominated'] = frame2['OscarAwardsNominated'].astype(str).astype(int) 
frame2['GoldenGlobeAwardsWon'] = frame2['GoldenGlobeAwardsWon'].astype(str).astype(int) 
frame2['GoldenGlobeAwardsNominated'] = frame2['GoldenGlobeAwardsNominated'].astype(str).astype(int)

frame2['TotalAwardsWon'] = frame2['AwardsWon']+frame2['PrimeAwardsWon']+frame2['BaftaAwardsWon']+frame2['OscarAwardsWon']+frame2['GoldenGlobeAwardsWon'] #calculating the total awards recieved by adding all the necessary columns
frame2['TotalAwardsNominated'] = frame2['AwardsNominated']+frame2['PrimeAwardsNominated']+frame2['BaftaAwardsNominated']+frame2['OscarAwardsNominated']+frame2['GoldenGlobeAwardsNominated'] # calculating the total nomination from the coulmns
frame3 = frame2.loc[~frame2.apply(lambda row: (row==0).all(), axis=1)] # eliminating all the rows from the data frame wherewe have all 0 values

frame4 = frame3.head(5).to_csv('awards.csv') # printing all the data into the CSV file
print frame4