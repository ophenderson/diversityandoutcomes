# Calculating parity for each racial group
# Making shp files for each year and racial group, with graduation rates over each county (ex: Black should have a shp file for each year)
# Showing this graphically: bar graph with parity score on x-axis, graduation rate on y, and each bar representing a different racial group (graphs done by school year)
# Time series graph showing state student teacher parity over time on one line and state graduation rates on the other (x-axis is school year, y-axis in parity, dots represent parity scores and graduation rates)


# Importing
import pandas as pd 

# Reading pickle
merged_df = pd.read_pickle('merged.pkl')

# Calculating parity scores
merged_df['S-T Parity (W)'] = (merged_df['White']/merged_df['Total Number of Students'])/(merged_df['WHITE TEACHERS']/merged_df['TOTAL NUMBER OF TEACHERS'])
merged_df['S-T Parity (B)'] = (merged_df['Black or African-American']/merged_df['Total Number of Students'])/(merged_df['BLACK TEACHERS']/merged_df['TOTAL NUMBER OF TEACHERS'])
merged_df['S-T Parity (H)'] = (merged_df['Hispanic or Latino']/merged_df['Total Number of Students'])/(merged_df['HISPANIC TEACHERS']/merged_df['TOTAL NUMBER OF TEACHERS'])

# Do i need to do anything else for the index?

merged_df.to_pickle('final.pkl')
