# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup

def query_site(url):
    '''
        main function to make queries
        
        url: url string
        
        '''
    r = requests.get(url)
    return r.text

url = "https://inflationdata.com/Inflation/Consumer_Price_Index/HistoricalCPI.aspx?reloaded=true"


def scrape_cpi():
    data = query_site(url)
    soup = BeautifulSoup(data,"lxml")
    # td elements store table data
    table_entries = soup.findAll("td")
    
    years = []
    rates = []
    for i in range(len(table_entries)):
        if i%14 == 0:
            years.append(table_entries[i].text)
        if (i+1)%14 == 0:
            rates.append(table_entries[i].text)
          
    with open("CPI_usa", "wb") as file_out:
        fieldnames = ["Year", "Price"]
        writer = csv.DictWriter(file_out, fieldnames)
        writer.writeheader()
        
        for i in range(len(years)):
            # encode unicode representation in byte-format
            writer.writerow({"Year" : years[i].encode("utf-8"), "Price" : rates[i].encode("utf-8")})

if __name__ == "__main__":
    scrape_cpi()