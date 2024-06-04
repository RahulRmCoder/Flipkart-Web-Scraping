import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name=[]
Prices=[]
Description=[]
Reviews=[]

for i in range(2,10):
  url='https://www.flipkart.com/search?q=mobiles+under+50k&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_16_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_16_na_na_na&as-pos=4&as-type=RECENT&suggestionId=mobiles+under+50k&requestId=047d982f-a5e2-4731-92bc-21288f3eef4a&as-searchtext=mobiles+under+50k&page='+str(i)
  r=requests.get(url)
  soup= BeautifulSoup(r.text, "lxml")
  box=soup.find('div',class_='DOjaWF gdgoEp')  # Assuming this points to a single product container
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
  reviews=box.find_all('div',class_='XQDdHH')
  for i in reviews:
      if i.text=='':  # Check for empty review text
          Reviews.append(0)
      else:
          review=i.text
          Reviews.append(review)
# Truncate lists to the length of the shortest list
min_length = min(len(Product_name), len(Prices), len(Description),len(Reviews))

Product_name = Product_name[:min_length]
Prices = Prices[:min_length]
Description = Description[:min_length]

# Create the DataFrame
df = pd.DataFrame({'Product Name': Product_name, 'Price': Prices, 'Product Specification': Description,'Rating':Reviews})
print(df)
df.to_csv('C:/Users/ACER/Documents/STUDIES/Skills/2. Web Scrapping/BeautifulSoup/Flipkart/Products1.1.csv') 
