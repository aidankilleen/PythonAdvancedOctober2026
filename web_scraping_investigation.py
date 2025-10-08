# web_scraping_investigaiton.py
# fetch the web page
import csv
from bs4 import BeautifulSoup
import requests

url = "https://www.worldometers.info/geography/flags-of-the-world/"

resp = requests.get(url)
resp.raise_for_status()



# use bs4 to parse the html
soup = BeautifulSoup(resp.text, "lxml")

results = []
# find the a tags
for a in soup.find_all("a", href=True):
    href=a["href"]
    if not href.startswith("/img/flags/"):
        continue
    # extract the url and the alt text
    img = a.find("img")
    src = img.get("src") 
    country = img.get("alt")

    results.append({"country":country, "flag":f"https://www.worldometers.info/{src}" })

# write the results to a csv file
filename = "flags.csv"
with open(filename, "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["country", "flag"])
    writer.writeheader()
    for r in results:
        writer.writerow(r)



