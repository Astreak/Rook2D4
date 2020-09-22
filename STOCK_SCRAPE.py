# div = MT10
#table tbldata14 bdrtpg
import requests 
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
data=requests.get("https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9")
data=data.content
def make_table(data):
       stocks=[]
       prices=[]
       soup=BeautifulSoup(data,"html.parser")
       Table=soup.find("table",class_="tbldata14 bdrtpg")
       for k in Table.find_all("td",class_="brdrgtgry"):
              if k.a:
                     stocks.append(k.a.get_text())
              else:
                     prices.append(k.get_text())
        
       stock=[]
       last=[]
       change=[]
       percentage=[]
       for i in range(0,len(prices)-3,4):
              last.append(prices[i])
       for i in range(1,len(prices)-2,4):
              change.append(prices[i])
       for k in range(2,len(prices)-1,4):
              percentage.append(prices[k])
       for i in range(0,len(stocks)-1,2):
              stock.append(stocks[i])
       
       dataF=pd.DataFrame({"STOCKS":stock,"Last_price":last,"change":change,"%\nchg":percentage})
       return dataF
       
       
              
                     
     
print(make_table(data))
	

