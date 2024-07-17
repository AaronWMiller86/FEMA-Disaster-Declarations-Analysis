import pandas as pd

new_columns = ['State', 'State Code', 'County Code', 'County Name']

df = pd.read_table('county_codes.txt', delimiter='|')
df.drop(df.columns[[3,5,6]], axis=1, inplace=True)
df.columns = new_columns

print(df.head(10))