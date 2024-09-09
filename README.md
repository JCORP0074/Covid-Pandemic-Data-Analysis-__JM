# Covid Data Analysis
This Data Analysis provides insights into the Covid pandemic 3 years ago from 2020 to 2023.

## Steps Followed:
The process in this data analysis is as follows:
1. Python Web Scraping. I used Python programming to gather the data from the website https://www.worldometers.info/coronavirus/
2. Data Cleaning and Transformation. I cleaned the data by removing unnecessary columns and creating new columns with aggregations through the Python pandas module. Afterwards, I performed the cleaning through the use of numpy and pandas modules. Lastly, I loaded the data into csv files and double-checked the data to ensure that it was thoroughly cleaned.
3. I put the data into one csv file and loaded the data to PowerBI for the data visualization and analysis.
4. Data Visualization through PowerBI
5. Analyzed the data in PowerBI

## Foreword
I'm quite actually new to data scraping using Python. Nevertheless, my background in web development helped me a lot in doing it successfully and the training I recently had with Python programming for Data Analysis. Also, the website that I used for web scraping is quite manageable to work with for web scraping through Python since it already contains the structured data that I need and its HTML code is quite really easy to read as well. Although I encountered a bit of a problem in doing some aggregations using Python due to the messy structure of the data once converted to DataFrame, I simply did the transformation of the data types of the columns that needed to be aggregated to form new columns through the use of numpy and pandas modules in python. As far as my coach's advice, It's best mostly to change the blank values or nan into 0 rather than replace it with average. Therefore, in the dataframe, I replaced the blank values with 0 instead of getting the average as the data that I have is not something that pertains to monetary.




