import requests
from bs4 import BeautifulSoup
import html5lib
import pandas as pd
import numpy as np
from newspaper import Article
import nltk
nltk.download("punkt")
PARSE=["https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen",
		"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTENCQVNNd29JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1HZG1jSE16S2dzU0NTOXRMekJuWm5Cek15Z0EqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURsek1XWVNCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
		"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiYENCQVNRZ29JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1EbDVOSEJ0S2hvS0dBb1VUVUZTUzBWVVUxOVRSVU5VU1U5T1gwNUJUVVVnQVNnQSouCAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAVAB?hl=en-IN&gl=IN&ceid=IN%3Aen",
		"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiXENCQVNQd29JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1ERjBjWEpyS2hjS0ZRb1JTazlDVTE5VFJVTlVTVTlPWDA1QlRVVWdBU2dBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
		"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiTENCQVNNd29JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJUENBUWFDd29KTDIwdk1ERjVObU54S2dzU0NTOXRMekF4ZVRaamNTZ0EqLggAKioICiIkQ0JBU0ZRb0lMMjB2TURsek1XWVNCV1Z1TFVkQ0dnSkpUaWdBUAFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen",
		"https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB/sections/CAQiSkNCQVNNUW9JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlJT0NBUWFDZ29JTDIwdk1ESnVkM0VxQ2hJSUwyMHZNREp1ZDNFb0FBKi4IACoqCAoiJENCQVNGUW9JTDIwdk1EbHpNV1lTQldWdUxVZENHZ0pKVGlnQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"]



def Main_news(URLS):
	links=[]
	articles_title=[]
	articles_summary=[]
	publish_date=[]
	urls=[]
	for  i in URLS:
		data=requests.get(i).content
		soup=BeautifulSoup(data,"html5lib")
		#for a in soup.find_all("article",class_=" MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne"):
		for k in soup.find_all("a",class_="VDXfz"):	
			links.append(k.get("href",None))
		for j in links:

			urls.append(j)
			articles=Article("https://news.google.com/"+j,language="en")
			try:
				articles.download()
				articles.parse()
				articles.nlp()
				articles_title.append(articles.title)
				articles_summary.append(articles.summary)
				publish_date.append(articles.publish_date)
			except:
				continue
	dataF=pd.DataFrame({"Main_NEWS_TITLE":articles_title,"Main_NEWS_SUMMARY":articles_summary,"PUBLISH-DATE":publish_date,"URLS":urls})
	dataF.to_csv("Main_Articles.csv",sep=",")

	return dataF


def Sub_News(URLS):
	links=[]
	articles_title=[]
	articles_summary=[]
	publish_date=[]
	urls=[]
	for  i in URLS:
		data=requests.get(i).content
		soup=BeautifulSoup(data,"html5lib")
		#for h in soup.find_all("article",class_="MQsxIb xTewfe tXImLc R7GTQ keNKEd keNKEd  dIehj EjqUne"):
		for a in soup.find_all("a",class_="VDXfz"):
			links.append(a.get("href",None))
		for j in links:
			urls.append(j)
			print(j)
			articles=Article("https://news.google.com/"+j,language="en")
			articles.download()
			articles.parse()
			articles.nlp()
			articles_title.append(articles.title)
			articles_summary.append(articles.summary())
			publish_date.append(articles.publish_date)


	dataF=pd.DataFrame({"SUB_NEWS_TITLE":articles_title,"SUB_NEWS_SUMMARY":articles_summary,"PUBLISH-DATE":publish_date,"URLS":urls})
	dataF.to_csv("Sub_ARTICLES.csv",sep=",")

	return dataF












print(Main_news(PARSE))
Sub_News(PARSE)



