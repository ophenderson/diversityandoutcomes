# This script is going to be used to clean my data files. Right now, I'm hoping to have student, teacher, and graduation rate input files that show student diversity and teacher diversity by race and school and graduation rates by race and school.

# Importing modules
import pandas as pd

# Cleaning Graduation Rates Data
# Step 1: Read the file
pd.read_excel('OVERALL_GRADRATE2023_2 (2).xlsx')

# Step 2: Get rid of columns you don't need
## All columns except - overall, black, white, hispanic

# Step 3: Get rid of school districts that are not on the most recent census shp file (how to do this?)

# Step 4: Check if you have any missing data

# Step 5: If you have missing data, fill it in with 0? N/A?

# Step 6: Create a column that takes schools within the same district and calculates their graduation rate (not sure how to do this mathematically)

# In the end, you should have a file that has the overall graduation rate for each school district and graduation rates by race for each school district



# Cleaning Teacher Diversity and Student Diversity Data
# Step 1: Read the file
pd.read_excel()

# Step 2: Get rid of columns you don't need

# Step 3: Get rid of school districts that are not on the most recent census shp file (how to do this?)

# Step 4: Check if you have any missing data

# Step 5: If you have missing data, fill it in with 0? N/A?





## Columns to get rid of: gnumerator_overall, gdenominator_overall, same columns for g_percent_gender_m, gender_m, gender_f, race_w, race_b
## Get rid of all columns that are not white, black, hispanic
## is there any way to check to make sure that all data has the same set of schools?
## Filling in missing values
## 
