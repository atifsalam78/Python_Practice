from pynotifier import Notification
import requests
from bs4 import BeautifulSoup
# import urllib.request
import pandas as pd


# def notifyMe(title,  description):
# 	Notification(
# 	title=title,
# 	description=description,
# 	icon_path='/home/atif/PycharmProjects/pythonProject/Corona Notification/corona-icon.png' 
# 	# duration=3,                                   
# 	# urgency='normal'
# ).send()

def getData(url):
	r = requests.get(url)
	return r.text 

# def url_get_contents(url):
# 	req = urllib.request.Request(url=url)
# 	f = urllib.request.urlopen(req)
# 	return
#  f.read()

if __name__=="__main__":
	# notifyMe("Atif Salam","Lets do something new!")

	htmlData = getData('https://www.worldometers.info/coronavirus/')

	soup = BeautifulSoup(htmlData, "html.parser")
	table1 = soup.find("table", id="main_table_countries_today")
	# print(table1)
	header = []
	for i in table1.find_all("th"):
		title = i.text
		header.append(title)
	# print(header)
	mydata = pd.DataFrame(columns = header)
	# print(mydata)
	for j in table1.find_all("tr")[1:]:
		row_data = j.find_all("td")
		row = [i.text for i in row_data]
		length = len(mydata)
		mydata.loc[length] = row
	# print(mydata)

	mydata.drop(mydata.index[0:7], inplace=True)
	mydata.drop(mydata.index[222:229], inplace=True)
	mydata.reset_index(inplace=True, drop=True)
	# Drop “#” column
	mydata.drop("#", inplace=True, axis=1)
	print(mydata)

	# Export to csv
	mydata.to_csv("covid_data.csv", index=False)
	# Try to read csv
	mydata2 = pd.read_csv("covid_data.csv")

# https://medium.com/analytics-vidhya/how-to-scrape-a-table-from-website-using-python-ce90d0cfb607