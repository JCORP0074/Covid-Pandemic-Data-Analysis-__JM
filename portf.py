import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/'

covid_data = requests.get(url)

#print(covid_data)

soup = BeautifulSoup(covid_data.content,'html.parser')

c_table = soup.find('table', id = "main_table_countries_today")

if c_table:
    ct_body = c_table.find('tbody')

    if ct_body:
        covid_list = []
        c_rows = ct_body.find_all('tr')

        header_row = c_table.find('tr')
        header_cells = header_row.find_all('th')
        column_names = [cell.text.strip() for cell in header_cells]
        covid_list.append(column_names)

        for row in c_rows:
            c_cells = row.find_all('td')
            c_row_data = [cell.text.strip() for cell in c_cells]
            covid_list.append(c_row_data)
        file_path = r'C:\Users\Desktop-PC\Desktop\covid_analysis_popu.csv'    

        covid_df = pd.DataFrame(covid_list[1:], columns= covid_list[0])
        #print('Successful')



    else:
        print('Table body not found')

else:
    print('Table not found')



#print(covid_df.head())

database = pd.DataFrame(covid_list[1:], columns= covid_list[0])
#print(database)

columns_needed = ['#','Country,Other','TotalCases','TotalTests','TotalRecovered','Population','TotalDeaths']

database1 = database[columns_needed]
#print(database1)

database1 = database1.drop(index=[0,1,2,3,4,5,6,7])
database1 = database1.reset_index(drop=True)
database1 = database1.replace('',0).replace('N/A',0)
database1['Population'] = database1['Population'].replace(',','',regex=True).astype(int)
database1['TotalCases'] = database1['TotalCases'].replace(',','',regex=True).astype(int)
database1['TotalTests'] = database1['TotalTests'].replace(',','',regex=True).astype(int)
database1['TotalDeaths'] = database1['TotalDeaths'].replace(',','',regex=True).astype(int)
database1['TotalCases - PopulationRatio'] = database1['TotalCases'] / database1['Population']
database1['TotalDeaths - PopulationRatio'] = database1['TotalDeaths'] / database1['Population']
database1['TotalTests - PopulationRatio'] = database1['TotalTests'] / database1['Population']
database1 = database1.replace(np.inf,0).replace(np.nan,0)
#file_path1 = r'C:\Users\Desktop-PC\Desktop\cleaned_covid_data_analysis'
#database1.to_csv(file_path1, index=False)
#print('successfully saved the cleaned data')
#print(database1)


#List the Top 5 countries with most deaths. Save it as different data frame

deaths = database[columns_needed]
deaths = deaths[~deaths['Country,Other'].str.contains("World|Asia|Europe|North America|South America|Oceania|Africa|''|Total")]
#print(deaths)
deaths['TotalDeaths'] = deaths['TotalDeaths'].replace(',','',regex=True).replace('',0).replace('N/A',0).astype(int)

Top_deaths = deaths.sort_values(by='TotalDeaths', ascending=False)
Top5 = Top_deaths.head().reset_index(drop=True)

#death_file = r'C:\Users\Desktop-PC\Desktop\top5_death_covid'
#Top5.to_csv(death_file, index=False)
#print('Successfully saved: Death File')
#print(Top5)

#List the Top 3 countries with most testing done. Save it as different data frame

testing_covid = database[columns_needed]
testing_covid = testing_covid[~testing_covid['Country,Other'].str.contains("World|Asia|Europe|North America|South America|Oceania|Africa|''|Total")]
#print(deaths)
testing_covid['TotalTests'] = testing_covid['TotalTests'].replace(',','',regex=True).replace('',0).replace('N/A',0).astype(int)

Top3_tests = testing_covid.sort_values(by='TotalTests', ascending=False)
Top3_countries = Top3_tests.head().reset_index(drop=True)

#test_file = r'C:\Users\Desktop-PC\Desktop\top3_tested_countries'
#Top3_countries.to_csv(test_file, index=False)
#print('Successfully saved: Top 3 tested Countries')
print(Top3_countries)


#List the Top 5 countries with most cases of covid. Save it as different data frame
Covid_cases = database[columns_needed]
Covid_cases = Covid_cases[~Covid_cases['Country,Other'].str.contains("World|Asia|Europe|North America|South America|Oceania|Africa|''|Total")]
#print(deaths)
Covid_cases['TotalCases'] = Covid_cases['TotalCases'].replace(',','',regex=True).replace('',0).replace('N/A',0).astype(int)

Top_Cases = Covid_cases.sort_values(by='TotalCases', ascending=False)
Top5_case = Top_Cases.head().reset_index(drop=True)
Cases_file = r'C:\Users\Desktop-PC\Desktop\top5Covidcases.csv'
#Top5_case.to_csv(Cases_file, index=False)
#print('Successfully saved: Covid Cases Top 5')
#print(Top5_case)


#List the top 5 countries with highest Total cases – Population Ratio.


cleaned_database = pd.read_csv('cleaned_covid_data_project.csv')

#print(cleaned_database)

Case_pop = cleaned_database
Case_pop = cleaned_database.replace('inf',0).replace(np.inf,0).replace(np.nan,0)
Top5_Ratio = Case_pop.sort_values(by='TotalCases - PopulationRatio', ascending=False)
Top5_pop_ratio = Top5_Ratio.head().reset_index(drop=True)
#print(Top5_pop_ratio[['Country,Other','TotalCases - PopulationRatio']])
#pop_ratio_file = r'C:\Users\Desktop-PC\Desktop\Top5_pop_ratio'
#Top5_pop_ratio.to_csv(pop_ratio_file,index=False)
#print('Successfully saved')



#List the top 5 countries with highest Total Deaths-Population Ratio.
Death_pop = cleaned_database
Death_pop = cleaned_database.replace('inf',0).replace(np.inf,0).replace(np.nan,0)
Death_pop = Death_pop['TotalDeaths - PopulationRatio'].astype(float)
Top5_DeathRatio = Case_pop.sort_values(by='TotalDeaths - PopulationRatio', ascending=False)
Top5_Death_PopRatio = Top5_DeathRatio.head().reset_index(drop=True)
#print(Top5_Death_PopRatio[['Country,Other','TotalDeaths - PopulationRatio']])
#Deathratio_file = r'C:\Users\Desktop-PC\Desktop\deathpopratio_file.csv'
#Top5_Death_PopRatio.to_csv(Deathratio_file,index=False)
#print('Successfully saved')

#List the top 5 countries with highest Total tests – Population Ratio.
Test_pop = cleaned_database
Test_pop = cleaned_database.replace('inf',0).replace(np.inf,0).replace(np.nan,0)
Test_pop = Test_pop['TotalTests - PopulationRatio'].astype(float)
Top5_testpop = Case_pop.sort_values(by='TotalTests - PopulationRatio', ascending=False)
Top5_testratio = Top5_testpop.head().reset_index(drop=True)
#testratiofile = r'C:\Users\Desktop-PC\Desktop\testratiofile.csv'
#Top5_testratio.to_csv(testratiofile,index=False)
#print(Top5_testratio[['Country,Other','TotalTests - PopulationRatio']])
#print('Successfully saved')



