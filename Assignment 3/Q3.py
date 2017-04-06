import pandas as pd
from pandas import Series, DataFrame
a = pd.read_csv('..\\Assignments\Assignment 3\Data\\cricket_matches.csv') #reading the data from the CSV file

frame = DataFrame(a, columns=['home', 'winner', 'innings1', 'innings1_runs','innings2', 'innings2_runs']) #selecting only those columns which are required

frame2 = frame.loc[frame['home'] == frame['winner']] # selecting rows where home team and winner is the same

frame2['scores'] = frame2['innings1_runs'].where(frame2['innings1'] == frame2['home'], frame2['innings2_runs']) #getting the scores where the home team plays innings1 or innings 2

frame3=frame2.groupby('home')['scores'].mean().head(5) #grouping by home

frame3.to_csv('scores.csv') #printing the data into the CSV file

print frame3