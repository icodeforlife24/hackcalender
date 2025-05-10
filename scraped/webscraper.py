import cloudscraper
from bs4 import BeautifulSoup
import csv
import requests
from scraped.models import Contest
from datetime import datetime
def timeconvert(date_str):
    date_obj = datetime.strptime(date_str, "%b/%d/%Y") 
    formatted_date = date_obj.strftime("%Y-%m-%d")
    return formatted_date
def run():
    
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
            contest_date = timeconvert(cols[2].get_text(strip=True).split()[0])
            contest_duration = cols[3].get_text(strip=True)
            contest= Contest(
                name=contest_name,
                start_time=contest_date,
                duration=contest_duration,
                link=url
            )
            contest.save()
run()