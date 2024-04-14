# Importing
import pandas as pd
import requests


pd.read_excel('Grad Rate 202-2023.xlsx')


# Defining a function but IDK
repo_url = https://github.com/ophenderson/diverstiyandoutcomes.git
folder_path = 'diverstyandoutcomes'/2022-2023
file_name = 'Grad Rate 2022-2023.xlsx'
def fetch_github_file(repo_url,folder_path,file_name):

# Fetching the file
raw_file= f"{https://github.com/ophenderson/diversityandoutcomes.git}/raw/main/{folder_path}/{file_name}
response = requests.get(raw_file)
# Turning it into a dataframe?
df = pd.read_excel(response.content)
df = pd.DataFrame(df)
# Dropping unneeded columns - there has to be a way to do this without listing out every column that needs to be dropped
def drop_columns_containing(df,words)
columns_to_drop = [col for col in df.columns if any(word in col for word in words)]
df = df.drop(columns=columns_to_drop)
return df
if __name__ == "__main__":
words_to_drop = ['BEDS','GENDER', 'DISABLED']

# Grouping by district


# Look at the file, does anymore cleaning need to be done?