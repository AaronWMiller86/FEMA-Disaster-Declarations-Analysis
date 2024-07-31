import pandas as pd, requests, requests_cache
from sqlalchemy import create_engine

# FEMA Disaster API URL
fema_api_url = 'https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries?'

# API call using 'requests_cached' python library for data retrieval and cacheing
requests_cache.install_cache('api_cache', expire_after=3600)
# First API call accesses the metadata to determine the total number (count) of rows in the dataset
metadata_call = requests.get(fema_api_url + '$inlinecount=allpages&$select=id&$top=1')
row_count = metadata_call.json()['metadata'].get('count')

# Attempt to perform API call and dataframe concatination using a while loop.
"""
def api_paging_loop():
    skip = 0
    top = 10000
    calls = (int(row_count) / top) + 1
    i = 0
    while(i < calls):
        loop_url = fema_api_url + '&$inlinecount=allpages&$skip=' + str(skip) + "&$top=" + str(top)
        result = pd.concat([pd.json_normalize(requests.get(loop_url).json(), 'DisasterDeclarationsSummaries')])
        i += 1
        skip = i * top
    return result
"""

# Function to call the FEMA API, convert the calls into dataframes and concat the dataframes into one
def fema_api_call():

    # The 'top' signifies the total rows per call (max 10,000) and the 'skip' jumps to the next uncalled row
    first_api_call = requests.get(fema_api_url + '$inlinecount=allpages&$skip=0&$top=10000').json()
    second_api_call = requests.get(fema_api_url + '$inlinecount=allpages&$skip=10000&$top=10000').json()
    third_api_call = requests.get(fema_api_url + '$inlinecount=allpages&$skip=20000&$top=10000').json()
    forth_api_call = requests.get(fema_api_url + '$inlinecount=allpages&$skip=30000&$top=10000').json()
    fifth_api_call = requests.get(fema_api_url + '$inlinecount=allpages&$skip=40000&$top=10000').json()
    sixth_api_call = requests.get(fema_api_url + '$inlinecount=allpages&$skip=50000&$top=10000').json()
    seventh_api_call = requests.get(fema_api_url + '$inlinecount=allpages&$skip=60000&$top=10000').json()

    # Converts the json data to a pandas dataframe
    df1 = pd.json_normalize(first_api_call, 'DisasterDeclarationsSummaries')
    df2 = pd.json_normalize(second_api_call, 'DisasterDeclarationsSummaries')
    df3 = pd.json_normalize(third_api_call, 'DisasterDeclarationsSummaries')
    df4 = pd.json_normalize(forth_api_call, 'DisasterDeclarationsSummaries')
    df5 = pd.json_normalize(fifth_api_call, 'DisasterDeclarationsSummaries')
    df6 = pd.json_normalize(sixth_api_call, 'DisasterDeclarationsSummaries')
    df7 = pd.json_normalize(seventh_api_call, 'DisasterDeclarationsSummaries')

    # Combines the resulting dataframes and returns the result
    return pd.concat([df1, df2, df3, df4, df5, df6, df7])

# (FEMA) DataFrame cleanup function that drops unneeded columns, renames columns, and drops unneeded trailing date data
def clean_fema_df():
    column_names = ['Disaster ID', 'State', 'Declaration Type', 'Declaration Date', 'Incident Type', 'Declaration Title', 'Begin Date', 'End Date', 'Close Out Date', 'State Code', 'County Code', 'Designated Area' ]
    """df = api_paging_loop()"""
    df = fema_api_call()
    # Drop unneeded columns
    df.drop(df.columns[[0,5,8,9,10,11,15,18,20,21,22,23,24]],axis=1, inplace=True)
    # Rename Columns
    df.columns = column_names
    # Remove unneccisary trailing date data
    df['Declaration Date'] = df['Declaration Date'].str[:-14]
    df['Begin Date'] = df['Begin Date'].str[:-14]
    df['End Date'] = df['End Date'].str[:-14]
    df['Close Out Date'] = df['Close Out Date'].str[:-14]
    return df

# Function that loads StateCensusData.csv as a dataframe
def state_pop_df():
    df = pd.read_table('StateCensusData.csv', delimiter=',', thousands=',')
    return df

# Function that loads county_codes.txt as a dataframe, drops unneeded columns, and renames the remaining columns
def county_list_df():
    new_columns = ['State', 'State Code', 'County Code', 'County Name']
    df = pd.read_table('county_codes.txt', delimiter='|')
    df.drop(df.columns[[3,5,6]], axis=1, inplace=True)
    df.columns = new_columns
    return df

# Function to convert the dataframes to an SQL database using the sqlalchemy python library
def df_to_sql():
    # Variable created to name the database and establish the connection (con)
    engine = create_engine('sqlite:///database.db')
    # Converts the dataframes to SQL tables inside the connected database and replaces the tables if they already exist.
    clean_fema_df().to_sql('Disaster Declarations', con=engine, index=False, if_exists='replace')
    state_pop_df().to_sql('State Population', con=engine, index=False, if_exists='replace')
    county_list_df().to_sql('County List', con=engine, index=False, if_exists='replace') 

def api_status_check():
# If/else statment that checks to make sure the api call is functioning correctly and returns an error if not.
    if metadata_call.status_code == 200:
        print("Performing API Calls on " + str(row_count) + " rows of FEMA data and creating a SQL Database.")
        # Calls the function to start the API call and SQL conversion.
        df_to_sql()
    else:
        print(f"Error: {metadata_call.status_code}")

api_status_check()