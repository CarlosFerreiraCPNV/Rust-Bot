from bs4 import BeautifulSoup
import requests

url = "https://wiki.rustclash.com/building/stone-foundation#tab=destroyed-by"
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    print(html)
else:
    print("Erreur :" + str(response.status_code))