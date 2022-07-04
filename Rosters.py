## Created by Ben Zhao
## 29 March 2022
## Used for Creating spreadsheets for Carleton College Varsity Rosters for 2021-2022 Season 

import pandas
  
## Load Master Spreadsheet with all Varsity Athletes Information
## Can load either spreadsheet data from Mens or Womens Sports by replacing next line
data = pandas.read_excel("/Users/benzhao/Desktop/Python/Rosters/WomenSports.xlsx")

## Get Unique Sports from Sport Column and create object for each one 
rostersData = data["Sport1"].unique()
  
## Iterate over each roster object and return information of each student for a given sport roster in a new excel file 
for i in rostersData:
    x = data[data["Sport1"].str.contains(i)]
    x.to_excel(i+"W"+".xlsx")
