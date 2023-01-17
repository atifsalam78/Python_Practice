import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

#Creating an url
url = "https://www.worldometers.info/coronavirus/"

#Creating an object
page = requests.get(url)

#Check wheter server allows us to scrape or not if response is 200 means yes
# print(page.status_code)

#obtain page information
soup = BeautifulSoup(page.text,"lxml")
# print(soup.prettify)

#Obtain information from table
table1 = soup.find("table", id="main_table_countries_today")
# print(table1)

#Obtain every title of columns with tag <th>

headers = []
for i in table1.find_all("th"):
    title = i.text
    headers.append(title)
# print(headers)

#Convert wrapped texts in column 13 into one line text
headers[13] = "Tests/1M pop"
# print(headers)

#Creating Data Frame
mydata = pd.DataFrame(columns = headers)

#Creating for loop to fill mydata
for j in table1.find_all("tr")[1:]:
    row_data = j.find_all("td")
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row



# Drop and Cleaning uncessary rows
# Note: more cleaning is required

mydata.drop(mydata.index[0:7], inplace=True)
mydata.drop(mydata.index[222:229], inplace=True)
mydata.reset_index(inplace=True, drop=True)

#Drop # Column

mydata.drop("#",inplace=True, axis=1)

# print(mydata.to_string)

# Exporting to csv
mydata.to_csv("covid_data.csv", index=False)

# Reading CSV

mydata2 = pd.read_csv("covid_data.csv")
print(mydata2)








