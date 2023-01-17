import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
htmlDoc = requests.get(url)
# print(htmlDoc.text)

# Parser

soup = BeautifulSoup(htmlDoc.text, "lxml")
# print(soup.prettify)

# Access h1 tag
# print(soup.h1)

# Access header tag
# print(soup.header)

# Access div tag
# print(soup.div)

# Access string from nested tags
# print(soup.header.p)
# print(soup.header.p.string)

# Access a tag in header
# check1 = soup.header.a
# check1.attrs
# print(check1.attrs["data-target"])

# check1["new-target"] = "This is the new attribute"
# print(check1.attrs)

# Searching specific attribute

# price = soup.find("h4", class_="pull-right price")
# price = soup.find_all("h4", class_="pull-right price")[2:5]

# price = soup.find_all(["h4","a","p"])
# price =soup.find_all(["header", "div"])
# price =soup.find_all(id=True)
# print(price)

# Data Collection

name = soup.find_all("a", class_="title")
price = soup.find_all("h4", class_="pull-right price")
reviews = soup.find_all("p", class_="pull-right")
description = soup.find_all("p", class_="description")


# price = soup.find("h4", class_="pull-right price")
# print(price.text)

# Creating loop to make string from find_all list
productNameList = []
for i in name:
    name = i.text
    productNameList.append(name)

productPriceList = []
for i in price:
    price = i.text
    productPriceList.append(price)

productReviewsList = []
for i in reviews:
    reviews = i.text
    productReviewsList.append(reviews)

productDescriptionList = []
for i in description:
    description = i.text
    productDescriptionList.append(description)

# Creating data frame
table = pd.DataFrame({"Product Name": productNameList, "Product Price": productPriceList, "Product Reviews": productReviewsList, "Product Description": productDescriptionList})

# Exporting to csv
# table.to_csv("Price.csv", index=False)

# Read CSV
tabel2 = pd.read_csv("Price.csv")
print(tabel2)