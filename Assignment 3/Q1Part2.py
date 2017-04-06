import pandas as pd
from pandas import Series, DataFrame
a = pd.read_csv('..\\Assignment 3\Data\\vehicle_collisions.csv')  #reading the CSV file

frame2 = DataFrame(a, columns=['BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE','VEHICLE 4 TYPE', 'VEHICLE 5 TYPE'])  # getting the required columns for processing

frame2 = frame2.rename(columns={'VEHICLE 1 TYPE': 'One_Vehicle_Involved', 'VEHICLE 2 TYPE': 'Two_Vehicle_Involved','VEHICLE 3 TYPE': 'Three_Vehicle_Involved',
	'VEHICLE 4 TYPE': 'Four_Vehicle_Involved','VEHICLE 5 TYPE': 'Five_Vehicle_Involved'})  #renaming the columns as needed

frame2.groupby('BOROUGH')['One_Vehicle_Involved','Two_Vehicle_Involved','Three_Vehicle_Involved','Four_Vehicle_Involved','Five_Vehicle_Involved'].count() # using groupby to get the total count of vehicles involved in each category

frame2.to_csv('vehicle.csv') #printing the data into the CSV file

print frame2