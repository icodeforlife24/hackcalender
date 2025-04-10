import cloudscraper
from bs4 import BeautifulSoup
import csv
import requests

def run():
    with open(r"C:\Users\shudd\OneDrive\Desktop\convener assignment\question2\scraped\hackathon.csv", "w") as file:
        a = csv.writer(file)
        a.writerow(["Contest Name", "Contest Date", "Contest Duration"])


    url = "https://codeforces.com/contests"
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)

    if response.status_code == 200:
        data = BeautifulSoup(response.text, "html.parser")
        first_table = data.select(".contestList .datatable")[0]
        rows = first_table.select("tr")[1:]
    for row in rows:
        cols = row.find_all("td")
        if cols:
            contest_name = cols[0].get_text(strip=True)
            contest_date = cols[2].get_text(strip=True)
            contest_duration = cols[3].get_text(strip=True)
            with open(r"C:\Users\shudd\OneDrive\Desktop\convener assignment\question2\scraped\hackathon.csv", "a") as file:
                a = csv.writer(file)
                a.writerow([contest_name, contest_date, contest_duration])

    else:
        print(f"Failed, status code: {response.status_code}")
run()