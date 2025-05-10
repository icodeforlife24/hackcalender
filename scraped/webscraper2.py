import requests
from bs4 import BeautifulSoup
import csv
from scraped.models import Contest
def run2():
    url = "https://atcoder.jp/contests/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = BeautifulSoup(response.text, "html.parser")
        table = data.find("div", id="contest-table-upcoming")

        if table:
            rows = table.find("tbody").find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                if len(cols) >= 3:
                    start_time = cols[0].text.strip()
                    name = cols[1].text.strip()
                    duration = cols[2].text.strip()
                    contest= Contest(
                        name=name,
                        start_time=start_time.split()[0],
                        duration=duration,
                        link=url)
                    contest.save()
                    
        else:
            print("Could not find upcoming contests table.")
    else:
        print(f" Failed Status code: {response.status_code}")
        
run2()
