# Project3-Census

# Topic

# Dataset
* [API call 1 - : Insurance data by county 2 years](https://www.census.gov/data/developers/data-sets/Health-Insurance-Statistics.html) 
* [API information](api.census.gov/data/timeseries/healthins/sahie.html)
* [Geography](api.census.gov/data/timeseries/healthins/sahie/geography.html)
* [Variables](api.census.gov/data/timeseries/healthins/sahie/variables.html)

* [API Call 2: Population data by county (corresponding to 2 years in API call 1)](http://)

## API Call 3: Income data by county (corresponding to 2 years in API call 1)

## API Call 4: Death rate by county (corresponding to 2 years in API call 1)

## Geo-coding of state-county
* [Geo-Coding data](https://eric.clst.org/tech/usgeojson/)
## Explore to gather data in geo-json format. If not convert api data to geo json

Inspiration

Visuals

Proposal
- param_config_file
    - Capture the mongodb db name
    - endpoints
    - flask site port

- Geo coding data for (State,county)
- INSU_DATA / API Call 1 ("Insured","Un-insured","State","County" "Year", "lat","lon")
- POP_DATA / API Call 2 ("Population_Count","State","County","Year","lat","lon")
- INCO_DATA / API Call 3 ("Income","State","County","Year","lat","lon")
- DEATH_DATA / API Call 4 ("Death_count","State","County","Year","lat","lon")
- Database (MongoDB) (for each dataset) (refer to module 12-1)
- ETL routines to clean up and merge data for rendering into starter database
- Initialize database with api calls to feed the starter database
- Build a Python flask service layer to initialize the map rendering with dataset from mongoDB (refer to module 10-3 flask)
- Incorporate leaflets / plotly to enable user interaction with the data visualization


