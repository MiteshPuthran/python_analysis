import pandas as pd
from pandas import Series, DataFrame
r = pd.read_csv('..\\Assignment 3\Data\employee_compensation.csv')  #reading the data from the CSV file

frame = DataFrame(r, columns=['Organization Group', 'Department', 'Total Compensation']) # getting the required columns for processing

frame_agg = frame.groupby(['Organization Group','Department'])['Total Compensation'].first() #grouping by the organization and department
frame_agg11 = frame.groupby(['Organization Group','Department']).agg({'Total Compensation':max}) # using aggregate to findthe max compensation 
g = frame_agg11['Total Compensation'].groupby(level=0, group_keys=False) # grouping by total compensation 
res = g.apply(lambda x: x.sort_values(ascending=False)).head(3) # sorting in the descending order of the total compensation

res.to_csv('compensation.csv') # printing the data into the CSV file

print res