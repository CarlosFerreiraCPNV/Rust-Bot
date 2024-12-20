from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://wiki.rustclash.com/building/stone-foundation#tab=destroyed-by")
soup = BeautifulSoup(page_to_scrape.content, "html.parser")

tableau = soup.findAll("table", class_="table w100 olive sorting")

print(tableau)

for donnees in tableau:
    explo = donnees.find('tr', attrs={"data-group":"explosive"})
    cquatre = explo.find('a', attrs={"href":"/item/timed-explosive-charge"})
    print(cquatre)