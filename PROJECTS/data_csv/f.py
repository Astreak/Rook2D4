import requests
from bs4 import BeautifulSoup

data=requests.get("https://www.myntra.com/tshirt")
print(data)