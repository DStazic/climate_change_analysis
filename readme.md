The goal of this project is to analyse occurrences of extreme weather events in the United States for the 20th century. Moreover, this project includes the analysis of the temperature profile, carbon dioxide emission rates and atmospheric carbon dioxide concentration.
More precisely, the aim is to elaborate whether the annual numbers of extreme weather events have changed over time (1950-2017), if there is any connection to temperature -changes- and if there is any evidence for a HUMAN-MADE problem due to burning of fossil fuels.
More datasets are included to support the analysis. 

Data on extreme weather events and casualties was obtained from the National Climatic Data Center archive:
- https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/
—> the major data set (all sets combined) is included as file: all_storm_events_victims.csv.bz2 

Data on global and US temperatures and atmospheric carbon dioxide concentration was obtained from KAGGLE:
-www.kaggle.com
—> data sets included as files: 1. GlobalLandTemperaturesByState.csv 2. carbon_dioxide_levels.csv

Data on global carbon dioxide emission was obtained from the Carbon Dioxide Information Analysis Center:
-http://cdiac.ornl.gov/CO2_Emission/timeseries/global
—> data set included as file: Global_emission_8192.csv

US census data was obtained from:
-www.populationpyramid.net 
—> data set included as file: census_usa.csv

Data on historic consumer price index (US) was obtained from:
-www.inflationdata.com
—> data set included as file: CPI_usa.csv

Following Python scripts were used to scrape the data:
-scrape_weather_casualties_data.py (for data on extreme weather)
-scrape_census_data.py (for US census data)
-scrape_consumer_price_index.py (for US consumer price index data)

Storm_Data_Export_Format.docx is provided by the National Climatic Data Center and contains a description about each variable in the extreme weather and casualties data set.

