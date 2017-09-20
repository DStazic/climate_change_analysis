# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
import gzip
import argparse

def query_site(url):
    '''
        main function to make queries
        
        url: url string
        
        '''
    r = requests.get(url)
    return r.text

url = "https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/"

def download_file(source):
    data = query_site(url)
    soup = BeautifulSoup(data,"lxml")
    
    if source == "event":
        source_type = "StormEvents_details-ftp_v1.0"
        file_generic = "Storm_Event"
        file_directory = "events_data/"
    elif source == "victims":
        source_type = "StormEvents_fatalities-ftp_v1.0"
        file_generic = "Storm_Fatalities"
        file_directory = "victims_data/"
    

    for item in soup.findAll("a"):
        href = item.get("href")
        if source_type in href:
            file_path = url+href
            file_year_re = re.compile(r"_d\d{4}_")
            file_year_match = file_year_re.search(file_path).group()
            
        
            r = requests.get(file_path)
            file_name = "{2}zipfiles/{0}{1}.zip".format(file_year_match,file_generic,file_directory)
            with open(file_name, "wb") as file:
                file.write(r.content)
            with gzip.open(file_name, "r") as file_in:
                with open("{2}{0}{1}.csv".format(file_year_match, file_generic,file_directory), "wb") as file_out:
                    file_out.write(file_in.read())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'download data sets')
    parser.add_argument('source', help='which data source to download (storm_events, fatalities); provide specific identifier to detect and download the corresponding files ("StormEvents_details-ftp_v1.0", "StormEvents_fatalities-ftp_v1.0"  to download all storm events and cognate fatalities data, respectively)')
    #parser.add_argument('file', help='generic file name', type=string)
    args = parser.parse_args()
    download_file(args.source)
