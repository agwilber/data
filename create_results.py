import os
import pandas as pd # pip3 install pandas
import numpy as np
import requests
# pip3 install fuzzywuzzy
from fuzzywuzzy import process # must also have python-Levenshtein installed (pip3 install python-Levenshtein)

path = '/Users/mandy/Projects/NewmarkTest/data' # working directory

from git import Repo
Repo.clone_from('https://github.com/xoba/data.git', path) # pulls necessary files 'addresses.csv' and 'properties.json' as well as readme.md, containing link to County Business Patterns: 2016, from github to location of working directory

os.chdir(path) # changes to working directory defined above

df1 = pd.read_csv('addresses.csv') # reads file 'addresses.csv' in pandas framework

df2 = pd.read_json('properties.json', lines=True) # reads file 'properties.json' in pandas framework, lines = T is necessary for json file

# ISSUE: some addresses are common except for typos, this must be corrected by matching imperfect data

addresses_array=[]
ratio_array=[]
def match_addresses(wrong_addresses,correct_addresses):
    for row in wrong_addresses:
        x=process.extractOne(row, correct_addresses)
        addresses_array.append(x[0])
        ratio_array.append(x[1])
    return addresses_array,ratio_array

# uppercase all characters in strings to eliminate case differences
DF1 = df1.apply(lambda x: x.astype(str).str.upper())

DF2 = df2.apply(lambda x: x.astype(str).str.upper())

wrong_addresses=DF1['address'].dropna().values
correct_addresses=DF2['address'].values

address_match,ratio_match=match_addresses(wrong_addresses,correct_addresses)


# if a new column is necessary:
#DF1['address_match']=pd.Series(address_match) #then need to drop address in DF1 and rename address_match as address
# otherwise
DF1['address']=pd.Series(address_match) # does this? overwrite the column?

df_12 = pd.merge(DF1, DF2, on='address', how='outer') # creates new dataframe when merging DF1 and DF2 based on the column key 'addresses' and showing all addresses (not just those in common) with 'outer'

# pulls files from County Business Patterns: 2016 to borrow info based on states and zip codes
url = 'https://www2.census.gov/programs-surveys/cbp/datasets/2016/cbp16st.zip?#'
r = requests.get(url, allow_redirects=True) # pulls Complete State File from County Business Patterns: 2016
open('cbp16st.zip', 'wb').write(r.content) # writes to .zip

url = 'https://www2.census.gov/programs-surveys/cbp/datasets/2016/zbp16totals.zip?#'
r = requests.get(url, allow_redirects=True) # pulls Complete Zip Code Totals file County Business Patterns: 2016
open('zbp16totals.zip', 'wb').write(r.content) # writes to .zip

from zipfile import ZipFile
with ZipFile('cbp16st.zip') as zipObj:
    zipObj.extractall() # extracts .zip to txt
with ZipFile('zbp16totals.zip') as zipObj:
    zipObj.extractall() # extracts .zip to txt

df3 = pd.read_csv('cbp16st.txt')

df4 = pd.read_csv('zbp16totals.txt')

# now merge some info from df3 based on state
df_123 = pd.merge(df_12, df3, on='common_column', how='outer')
#then merge some info from df4 based on zip code
df_1234 = pd.merg(df_123, df4, on='common_column', how='outer')

#final file

df_1234.to_csv("results.csv")
display('df_1234.head(10)') # displays first ten lines of final dateframe
