## Created by Ben Zhao
## 7 April 2022
## Used for Creating spreadsheets for Carleton College Varsity Letter Tracking for 2021-2022 Season 

import pandas as pd

## Load Master Spreadsheet with all Varsity Athletes Information and Letter Tracking 
df = pd.read_excel("/Users/benzhao/Desktop/Python/Rosters/books.xlsx")

#Sort Information by Athlete Last Name 
x = df.sort_values(by = 'LastName')
x.to_excel("Carleton College Lettering"+".xlsx")