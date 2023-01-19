# Project3-Census

* Topic

* Dataset
** API call 1 : Insurance data by county (2 years) (https://www.census.gov/data/developers/data-sets/Health-Insurance-Statistics.html) 
*** API information: api.census.gov/data/timeseries/healthins/sahie.html
*** Geography: api.census.gov/data/timeseries/healthins/sahie/geography.html
*** Variables: api.census.gov/data/timeseries/healthins/sahie/variables.html

** API Call 2: Population data by county (corresponding to 2 years in API call 1)

** API Call 3: Income data by county (corresponding to 2 years in API call 1)

** API Call 4: Death rate by county (corresponding to 2 years in API call 1)

Inspiration

Visuals


Proposal
- Database (MongoDB)
- param_config_file
    - Capture the mongodb db name
    - endpoints
    - flask site port
- Initialize database with api calls to feed the starter data 
- ETL routines to clean up and merge data for rendering
- Build a Python flask service layer to initialize the map rendering with dataset from mongoDB
- Incorporate leaflets / plotly to enable user interaction with the data visualization


