# Defining a function that fetches and cleans student diversity files
def fetch_and_clean(repo_owner, repo_name, folder_path, file_name, branch = 'main')
  url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/{branch}/{folder_path}/{file_name}"
  response = requests.get('url')
  if response.status_code == 200
    excel_bytes = response.content
    excel_file = BytesIO(excel_bytes)
    studentdf = pd.read_excel(excel_file)
    studentdf['YEAR'] = YEAR # once again, not sure how to make sure this is done differently for each file
    keep_cols = ['District', 'District Name', 'Total # Actively Enrolled Students', 'Black or African American', 'Hispanic or Latino', 'White') 
    studentdf = studentdf[keep_cols]
    studentdf.fillna('N/A')
  else:
    print(f"Failed to fetch and clean file: {response.status_code} - {response.reason}")
    return None 
