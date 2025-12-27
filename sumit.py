import pandas as pd 
import requests
from bs4 import BeautifulSoup

Product_name=[]
Prices=[]
Description=[]
Reviews=[]

for i in range(2,12):
  url ="https://www.flipkart.com/search?q=5000+phone+5g&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=5000+phone+5g%7CMobiles&requestId=14fe069e-6ad3-478a-8490-7856ac3cc08d&as-searchtext=5000&page="+str(i)

  r= requests.get(url)
# print(r)
  soup =BeautifulSoup(r.text , "lxml")

  box=soup.find("div",class_="QSCKDh dLgFEE")


  names=box.find_all("div",class_="RG5Slk")

  for i in names:
    name=i.text
    Product_name.append(name)
# print(Product_name)


  prices=box.find_all("div",class_="hZ3P6w DeU9vF")

  for i in prices:
    name=i.text
    Prices.append(name)
# print(Prices)

  des=box.find_all("ul",class_="HwRTzP")

  for i in des:
    name=i.text
    Description.append(name)
# print(Description)
     

  rev=box.find_all("div",class_="MKiFS6")

  for i in rev:
    name=i.text
    Reviews.append(name)
# print(Reviews)

df=pd.DataFrame({"Product name":Product_name,"Price":Prices,"Description":Description,"Review":Reviews})

# print(df)


df.to_excel("C:/Data science/Web scraping/python/Flipkart_under_Rs_50000_mobiles.xlsx",index=True)





























# print(soup)
# while True:
        # np = soup.find("a",class_="jgg0SZ").get("href")
        # cnp ="https://www.flipkart.com"+np

        # print(cnp)

#   url=cnp
#   r=requests.get(url)
#   soup=BeautifulSoup(r.text,"lxml")