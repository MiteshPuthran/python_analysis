# Python Final Project

# NYC Vehicle Collision Dataset Analysis with National Oceanic and Atmospheric Administration(NOAA) weather dataset

![](images/nyc.jpg?raw=true)
![](images/NOAA_emblem.png?raw=true)
<br>
<br>
The data for the project analysis were downloaded from the following sites:
* Vehicle collision dataset has been downloaded from [NYC Open Data](https://opendata.cityofnewyork.us/) using **Socrata Open Data API** - **API Request**
* Weather dataset was downloaded from [NOAA Weather Data](https://www.ncdc.noaa.gov/cdo-web/search?datasetid=GHCND) where a selection has to be made for the date range and type of data needed for the analysis. The processing of the data takes 2-3 days depending on the type and size of data you are requesting - **CSV File**
<br>

## Data Collection and Processing

### Fetching the data
* For the vehicle collision data, the data is downloaded using the API token key obtained after registering in their website. The data is in the form of JSON file.
* The weather data is downloaded after recieving a email from NOAA Weather Data with the download link.

### Storing the data
* The downloaded vehicle collision data JSON files are stored according to the different boroughs of NewYork(Manhattan, Queens, etc) and their respective zip codes. You can view the respective folder structure [here](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/ProcessedData).
* The weather dataset has been stored as a CSV file.

### Converting and merging the downloaded data
* The vehicle colision JSON file have been converted into CSV file by checking for each key value pair and are stored [here](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/ProcessedData). 
* The data from both the datasets are merged using Panda dataframes by selecting the common _'DATE'_ column available in both.

### Starting the Analysis:
The following analysis were made using the merged dataset.
<br>
## Analysis 1:
## _Factors that caused maximum collision in whole NYC from 2015-2017_
Finding out the top 10 factors that caused collision in NYC by using factors like Contibuting Factor and Number of Persons killed.
<br>
![](GeneratedImages/factor.png?raw=true)
<br>
#### Steps for the analysis:
1. Reading the raw data from the CSV file.
2. Taking the total count of the persons killed by grouping the factors responsible for collision.
3. Removing unwanted column where factors are not specified.
4. Inserting the data into the dataframe with the factors and the corresponding number of people that were killed by the collision.
5. Saving the data from the dataframe to a CSV file.
6. Plotting a graph to display the factors for the same. 
#### Outputs of Analysis:
1. [CSV File - Factor.csv](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/GeneratedCSV).
2. [Plot Files - Factor.png](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/GeneratedImages).

## Analysis 2:
## _Vehicle type involved in collision and number of people killed at each borough of NYC from 2015-2017_
Finding out the top vehicle types that caused collision in each borough of NYC by using factors like Borough, Vehicle Type and Number of Persons killed.
<br>
![](GeneratedImages/vehicle.png?raw=true)
<br>
#### Steps for the analysis:
1. Reading the raw data from the CSV file.
2. Taking the total count of the persons killed by grouping the vehicle type and borough involved in collision.
3. Selecting the date range for the collisions.
4. Inserting the data into the dataframe with the borough, vehicle type and the corresponding number of people that were killed by the collision.
5. Saving the data from the dataframe to a CSV file.
6. Plotting a graph to display the factors for the same. 
#### Outputs of Analysis:
1. [CSV File - Vehicle.csv](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/GeneratedCSV).
2. [Plot Files - Vehicle.png](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/GeneratedImages).

## Analysis 3:
## _Monthly collisions in Manhattan to that of the whole NYC for the year 2016_
Finding out monthly collisions in Manhattan to the monthly in NYC for the year 2016
<br>
![](GeneratedImages/monthly.png?raw=true)
![](GeneratedImages/percentage.png?raw=true)
<br>
#### Steps for the analysis:
1. Reading the raw data from the CSV file.
2. Taking date and borough data from the dataset.
3. Seperating out month and year from the date using datetime.striptime method.
4. Selecting the whole data for the NYC data and seperating Manhattan using the borough data.
5. Calculating the percentage of accidents in Manhattan to that of NYC.
5. Saving the data from the dataframe to a CSV file.
6. Plotting a bar graph to display the factors for the same and a pie chart to display the percentages of collision each month. 
#### Outputs of Analysis:
1. [CSV File - Monthly.csv](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/GeneratedCSV).
2. [Plot Files - Monthly.png](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/GeneratedImages).

## Analysis 4:
## _Snowfall and Rainfall in inches causing injury to people in NYC from 2015-2017_
Finding out the highest snowfall and rainfall in inches which caused maximum number of injuries  from collision to the people of NYC
<br>
![](GeneratedImages/snowinjury.png?raw=true)
![](GeneratedImages/raininjury.png?raw=true)
<br>
#### Steps for the analysis:
1. Reading the raw data from the CSV file.
2. Taking the total count of the persons killed by grouping the vehicle type and borough involved in collision.
3. Selecting the date range for the collisions.
4. Inserting the data into the dataframe with the borough, vehicle type and the corresponding number of people that were killed by the collision.
5. Saving the data from the dataframe to a CSV file.
6. Plotting a graph to display the factors for the same. 
#### Outputs of Analysis:
1. [CSV File - Vehicle.csv](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/GeneratedCSV).
2. [Plot Files - Vehicle.png](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/GeneratedImages).
