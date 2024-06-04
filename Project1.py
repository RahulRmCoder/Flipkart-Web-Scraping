import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name=[]
Prices=[]
Description=[]

url='https://www.flipkart.com/search?q=mobiles+under+50k&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_16_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_16_na_na_na&as-pos=4&as-type=RECENT&suggestionId=mobiles+under+50k&requestId=047d982f-a5e2-4731-92bc-21288f3eef4a&as-searchtext=mobiles+under+50k&page='+str(1)
r=requests.get(url)
soup= BeautifulSoup(r.text, "lxml")
box=soup.find('div',class_='DOjaWF gdgoEp')  
names=box.find_all("div",class_='KzDlHZ')
for i in names:
    name=i.text
    Product_name.append(name)
prices=box.find_all('div',class_='Nx9bqj _4b5DiR')
for i in prices:
    price=i.text
    Prices.append(price)
descriptions=box.find_all('ul',class_='G4BRas')
for i in descriptions:
    description=i.text
    Description.append(description)
df = pd.DataFrame({'Product Name': Product_name, 'Price': Prices, 'Product Specification': Description})
print(df) 
df.to_csv('C:/Users/ACER/Documents/STUDIES/Skills/2. Web Scrapping/BeautifulSoup/Flipkart/Products.csv') 
