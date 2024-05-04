# Calculating parity for each racial group
# Making shp files for each year and racial group, with graduation rates over each county (ex: Black should have a shp file for each year)
# Showing this graphically: bar graph with parity score on x-axis, graduation rate on y, and each bar representing a different racial group (graphs done by school year)
# Time series graph showing state student teacher parity over time on one line and state graduation rates on the other (x-axis is school year, y-axis in parity, dots represent parity scores and graduation rates)


# Importing
import pandas as pd 

# Reading pickle
grads = pd.read_pickle('grad.pkl')
teachers = pd.read_pickle('teacher.pkl')
students = pd.read_pickle('student.pkl')
merged_df = pd.read_pickle('merged.pkl')


