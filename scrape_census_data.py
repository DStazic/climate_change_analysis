# -*- coding: utf-8 -*-

import requests
import re
import ast
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd
import argparse


def query_site(url):
    '''
        main function to make queries
        
        url: url string
        
        '''
    r = requests.get(url)
    return r.text

url = "https://www.populationpyramid.net/united-states-of-america/"

def scrape_census_data():
    '''
       function takes a range in years to retrive census data for each year
        
       from_year: lower limit in year range
       to_year: upper limit in year range
       by: defines the increment of the range
      
    '''
    
    # census data for all age groups is available only from year 1990 onwards
    years = range(1990, 2018, 1)
    summary_census = []
    for year in years:
        url_specific_year = url+str(year)
        data = query_site(url_specific_year)
        soup = BeautifulSoup(data,"lxml")
        # return script tag and convert to string
        table_entries = soup.find("script", attrs={'type':'application/javascript'})
        table_entries_string = table_entries.string
        # use regex to match dictionary "var json", which contains the relevant census information
        # use groups to return only the dictionary with content (group 2) without the "var json" variable (group 1)
        pattern = re.compile(r"(var json = )({.*})")
        match = pattern.search(table_entries_string).group(2)
        # var json keys are specified with single quotes but json.loads() accepts only double quotes!!
        # either substitute single to double quotes or use ast.literal_eval() function from ast module.
        # This will simply evaluate the input string and return the corresponding Python literal structure encoded
        # inside the string (here a dictionary).
        json_object = ast.literal_eval(match)
        # define custom census groups
        census_groups = {"0_to_19":["0-4", "5-9", "10-14", "15-19"],
                         "20_to_39":["20-24", "25-29", "30-34", "35-39"],
                         "40_to_59":["40-44", "45:49", "50-54", "55-59"],
                         "60_to_79":["60-64", "65-69", "70-74", "75-79"],
                         "80_to_89":["80-84", "85-89"],
                         "90_plus":["90-94", "95-99", "100+"]}
        
        total_population = json_object["population"]
        
        census_data = defaultdict(int)
        for group in census_groups:
            for age_group in json_object["female"]:
                if age_group["k"] in census_groups[group]:
                    census_data[group] += (age_group["v"]/total_population)*100
            
            for age_group in json_object["male"]:
                if age_group["k"] in census_groups[group]:
                    census_data[group] += (age_group["v"]/total_population)*100
        
        # convert census data for each year to pandas Series and append to summary_census list
        # this makes it easy to make a final data frame that stores census data for every year
        census_data_Series = pd.Series(census_data.values(), index = census_data.keys())
        summary_census.append(census_data_Series)
    
    summary_census_df = pd.DataFrame(summary_census, index = years)
    summary_census_df.to_csv("census_usa", index_label = "Year")
    

if __name__ == "__main__":
    scrape_census_data()
