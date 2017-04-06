import pandas as pd
from pandas import Series, DataFrame
a = pd.read_csv('..\\Assignment 3\Data\\vehicle_collisions.csv')  #reading the CSV file
a['DATE'] = pd.to_datetime(a['DATE']) #getting the date column from the data frame
nycjan = a[(a['DATE'] > '2016-01-01') & (a['DATE'] < '2016-01-31')]  #getting all the january data for NYC
nycfeb = a[(a['DATE'] > '2016-02-01') & (a['DATE'] < '2016-02-28')]
nycmar = a[(a['DATE'] > '2016-03-01') & (a['DATE'] < '2016-03-31')]
nycapr = a[(a['DATE'] > '2016-04-01') & (a['DATE'] < '2016-04-30')]
nycmay = a[(a['DATE'] > '2016-05-01') & (a['DATE'] < '2016-05-31')]
nycjun = a[(a['DATE'] > '2016-06-01') & (a['DATE'] < '2016-06-30')]
nycjul = a[(a['DATE'] > '2016-07-01') & (a['DATE'] < '2016-07-31')]
nycaug = a[(a['DATE'] > '2016-08-01') & (a['DATE'] < '2016-08-30')]
nycsep = a[(a['DATE'] > '2016-09-01') & (a['DATE'] < '2016-09-30')]
nycoct = a[(a['DATE'] > '2016-10-01') & (a['DATE'] < '2016-10-31')]
nycnov = a[(a['DATE'] > '2016-11-01') & (a['DATE'] < '2016-11-30')]
nycdec = a[(a['DATE'] > '2016-12-01') & (a['DATE'] < '2016-12-31')]

b = a.loc[a['BOROUGH']=='MANHATTAN']  #selecting manhattan from the dataframe
manjan = b[(b['DATE'] > '2016-01-01') & (b['DATE'] < '2016-01-31')] #getting all the january data for Manhattan
manfeb = b[(b['DATE'] > '2016-02-01') & (b['DATE'] < '2016-02-28')]
manmar = b[(b['DATE'] > '2016-03-01') & (b['DATE'] < '2016-03-31')]
manapr = b[(b['DATE'] > '2016-04-01') & (b['DATE'] < '2016-04-30')]
manmay = b[(b['DATE'] > '2016-05-01') & (b['DATE'] < '2016-05-31')]
manjun = b[(b['DATE'] > '2016-06-01') & (b['DATE'] < '2016-06-30')]
manjul = b[(b['DATE'] > '2016-07-01') & (b['DATE'] < '2016-07-31')]
manaug = b[(b['DATE'] > '2016-08-01') & (b['DATE'] < '2016-08-30')]
mansep = b[(b['DATE'] > '2016-09-01') & (b['DATE'] < '2016-09-30')]
manoct = b[(b['DATE'] > '2016-10-01') & (b['DATE'] < '2016-10-31')]
mannov = b[(b['DATE'] > '2016-11-01') & (b['DATE'] < '2016-11-30')]
mandec = b[(b['DATE'] > '2016-12-01') & (b['DATE'] < '2016-12-31')]

processeddata = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], 
                 'Manhattan': [len(manjan), len(manfeb), len(manmar), len(manapr), len(manmay),len(manjun),len(manjul),len(manaug),len(mansep),len(manoct),len(mannov),len(mandec)],
                 'NYC': [len(nycjan), len(nycfeb), len(nycmar), len(nycapr), len(nycmay),len(nycjun),len(nycjul),len(nycaug),len(nycsep),len(nycoct),len(nycnov),len(nycdec)],
                 'Percentage': [(len(manjan)/len(nycjan)),(len(manfeb)/len(nycfeb)),(len(manmar)/len(nycmar)),(len(manapr)/len(nycapr)),(len(manmay)/len(nycmay)),(len(manjun)/len(nycjun)),
                 (len(manjul)/len(nycjul)),(len(manaug)/len(nycaug)),(len(mansep)/len(nycsep)),(len(manoct)/len(nycoct)),(len(mannov)/len(nycnov)),(len(mandec)/len(nycdec))]}

# getting the total number of accidents in nyc and manhattan and finding out the percentage of accidents happened in manhattan with the total accidents happened in new york.

frame = DataFrame(processeddata,columns=['Month', 'Manhattan', 'NYC','Percentage']).head(3) #printing all the data into the dataframe

frame.to_csv('percentage.csv') #printing the data into the CSV file

print frame