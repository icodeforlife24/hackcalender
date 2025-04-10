import requests
from bs4 import BeautifulSoup
import csv

def run2():
    url = "https://atcoder.jp/contests/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = BeautifulSoup(response.text, "html.parser")
        table = data.find("div", id="contest-table-upcoming")

        if table:
            rows = table.find("tbody").find_all("tr")
            with open(r"C:\Users\shudd\OneDrive\Desktop\convener assignment\question2\scraped\hackathon.csv", mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                for row in rows:
                    cols = row.find_all("td")
                    if len(cols) >= 3:
                        start_time = cols[0].text.strip()
                        name = cols[1].text.strip()
                        duration = cols[2].text.strip()
                        writer.writerow([name, start_time, duration])
        else:
            print("Could not find upcoming contests table.")
    else:
        print(f" Failed Status code: {response.status_code}")
        
run2()
