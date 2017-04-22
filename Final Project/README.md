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

### Analysis 1:
#### Factors that caused maximum collision in whole NYC from 2015-2017
Finding out the top 10 factors that caused collision in NYC by using factors like Contibuting Factor and Number of Persons killed.
<br>
![](GeneratedImages/factor.png?raw=true)
<br>
#### Steps for the analysis:
1. Reading the raw data from the CSV file.
2. Taking the total count of the persons killed by grouping the factors responsible for collision.
3. Removing unwanted column where factors are not specified.
4. Inserting the data into the dataframe with the facorts and the corresonding number of people that were killed by the collision.
5. Saving the data from the datframe to a CSV file.
6. Plotting a graph to display the factors for the same. 
#### Outputs of Analysis:
1. [CSV Files](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/GeneratedCSV).
2. [Plot Files](https://github.com/MITESHPUTHRANNEU/puthran_mitesh_spring2017/tree/master/Final%20Project/GeneratedImages).


