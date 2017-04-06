import pandas as pd
from pandas import Series, DataFrame
r = pd.read_csv('..\\Assignment 3\Data\employee_compensation.csv') #reading the data from the CSV file

cal = r.loc[r['Year Type'] == 'Calendar'] #selecting only those columns which are of the tpe calendar
for col in cal:
    cal[col].unique() #selecting only the unique rows with calendar

frame = DataFrame(cal, columns=['Job Family', 'Total Benefits', 'Total Compensation']) # selecting only the required columns from the dataframe
frame['Percent_Total_Benefit'] = (frame['Total Benefits']/frame['Total Compensation'])*100 #calculating the percentage for the same
frame2 = frame.head(5)

frame2.to_csv('compensationbenefits.csv') # printing the data into the CSV file

print frame2