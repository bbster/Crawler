import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.vitibet.com/index.php?clanek=quicktips&sekce=fotbal&lang=en')
source = req.text
soup = BeautifulSoup(source, 'html.parser')
top_list = soup.select("#quicktips > table > tbody > tr:nth-child(4) > td:nth-child(2)")
for list in top_list:
    print(list.text)


