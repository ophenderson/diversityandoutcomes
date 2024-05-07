# Importing and reading pickle file
import pandas as pd
final = pd.read_pickle('final.pkl')

# Displaying all columns that you ask for instead of "..."
pd.set_option('display.max.columns', None)

# Table of Parity and Outcomes for Spartanburg County School District 1
final[final['District'] == 'SPARTANBURG 1'][['Year', 'District', 'Graduation Rate - W', 'Graduation Rate - B', 
                                             'Graduation Rate - H', 'T-S Parity (W)', 'T-S Parity (B)', 'T-S Parity (H)']]

