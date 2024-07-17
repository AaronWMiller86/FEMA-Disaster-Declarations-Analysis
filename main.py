import requests, pandas as pd


# FEMA Disaster API URL
url = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"

# API call function using 'requests' python library for data retrieval
def call_api():
    response = requests.get(url)

    # if/else statment that checks to make sure the api call is functioning correctly and returns an error if not
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Error: {response.status_code}"

# json to pandas conversion function using .json_normalize    
def convert_to_pandas():
    df = pd.json_normalize(call_api(), 'DisasterDeclarationsSummaries')
    return df

# DataFrame cleanup function that drops unneeded columns, renames columns, and drops unneeded trailing date data
def clean_df():
    column_names = ['Disaster ID', 'State', 'Declaration Type', 'Declaration Date', 'Incident Type', 'Declaration Title', 'Begin Date', 'End Date', 'Close Out Date', 'State Code', 'County Code', 'Designated Area' ]
    df = convert_to_pandas()
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

print(clean_df().head(20))