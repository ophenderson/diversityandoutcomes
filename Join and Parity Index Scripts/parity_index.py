# Importing
import pandas as pd 

# Reading pickle
merged_df = pd.read_pickle('merged.pkl')

# Calculating parity scores
merged_df['T-S Parity (W)'] = (merged_df['WHITE TEACHERS']/merged_df['TOTAL NUMBER OF TEACHERS'])/(merged_df['White']/merged_df['Total Number of Students'])
merged_df['T-S Parity (B)'] = (merged_df['BLACK TEACHERS']/merged_df['TOTAL NUMBER OF TEACHERS'])/(merged_df['Black or African-American']/merged_df['Total Number of Students'])
merged_df['T-S Parity (H)'] = (merged_df['HISPANIC TEACHERS']/merged_df['TOTAL NUMBER OF TEACHERS'])/(merged_df['Hispanic or Latino']/merged_df['Total Number of Students'])

# Do i need to do anything else for the index?

merged_df.to_pickle('final.pkl')
