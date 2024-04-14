# Defining a function that fetches and cleans teacher diversity files
def fetch_and_clean(repo_owner, repo_name, folder_path, file_name, branch = 'main')
  url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{folder_path}/{file_name}"
  response = requests.get('url')
  if response.status_code == 200
    excel_bytes = response.content
    excel_file = BytesIO(excel_bytes)
    studentdf = pd.read_excel(excel_file)
    studentdf['BEDSCODE'] = Year # the idea for this was that I would replace the BEDSCODE column with the school year that the data is from, not sure how to do this?
    graddf.rename(columns={'BEDSCODE':'YEAR'}, inplace=True)
    keep_cols = ['DISTRICT', 'DISTRICT NAME', 'WHITE MALES', 'WHITE FEMALES', 'WHITE GENDER NOT REPORTED', 'BLACK MALES', 'BLACK FEMALES', 'BLACK GENDER NOT REPORTED','HISPANIC MALES', 'HISPANIC FEMALES', 'HISPANIC GENDER NOT REPORTED')
    totalw = teacherdf['WHITE MALES', "WHITE FEMALES", "WHITE GENDER NOT REPORTED"].sum(axis=1)
    totalb = teacherdf['BLACK MALES', "BLACK FEMALES", "BLACK GENDER NOT REPORTED"].sum(axis=1)
    totalh = teacherdf['HISPANIC MALES', "HISPANIC FEMALES", "HISPANIC GENDER NOT REPORTED"].sum(axis=1)
    teacherdf = teacherdf[keep_cols]
    teacherdf.fillna('N/A')
  else:
    print(f"Failed to fetch and clean file: {response.status_code} - {response.reason}")
    return None 
