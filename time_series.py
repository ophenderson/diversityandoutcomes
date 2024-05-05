# Graphs I want
# Summary graphs
# Counties with: highest and lowest graduation rates, highest and lowest parity ratios

# County examples
# Pick a county - put the parity index on the x axis and graduation rates on y (make one for each school year)
# I want to create a line graph that shows the relationship between parity scores and grad rates

# Time series graph
# Pick one county - and make a graph that looks like this
# http://freerangestats.info/blog/2016/08/18/dualaxes 

# Could be cool to use random generator to pick a county

# Time series graph showing state student teacher parity over time on one line and state graduation rates on the other (x-axis is school year, y-axis in parity, dots represent parity scores and graduation rates)



# Importing
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True)
from itables import show



# Reading pickle file
final = pd.read_pickle('final.pkl')

# First Graph - scatterplot, white student-teacher ratio
plt.rcParams['figure.dpi'] = 500
customw = ('violet', 'plum', 'hotpink', 'lightpink', 'magenta', 'red')
sns.set_palette(customw)
ax = sns.relplot(data = final, x='S-T Parity (W)', y='Graduation Rate - W', kind='scatter', hue ='Year')
plt.ylabel('Graduation Rate')
plt.xlabel('Parity Score')
plt.title('Student-Teacher Parity and Graduation Rates Overtime - W')

## Couple of graduation rates above 1??
## Line at the bottom, no graduation rate -- missing data

# Second Graph - scatterplot, black student-teacher ratio
plt.rcParams['figure.dpi'] = 500
custom = ('cornflowerblue', 'royalblue', 'blue', 'slateblue', 'dodgerblue', 'darkturquoise')
sns.set_palette(custom)
ax = sns.relplot(data = final, x='S-T Parity (B)', y='Graduation Rate - B', kind='scatter', hue ='Year')
plt.ylabel('Graduation Rate')
plt.xlabel('Parity Score')
plt.title('Student-Teacher Parity and Graduation Rates Overtime - B')


# Third Graph - scatterplot, hispanic student-teacher ratio
plt.rcParams['figure.dpi'] = 500
custom = ('springgreen', 'lime', 'darkgreen', 'mediumaquamarine', 'chartreuse', 'yellowgreen')
sns.set_palette(custom)
ax = sns.relplot(data = final, x='S-T Parity (H)', y='Graduation Rate - H', kind='scatter', hue ='Year')
plt.ylabel('Graduation Rate')
plt.xlabel('Parity Score')
plt.title('Student-Teacher Parity and Graduation Rates Overtime - H')

# Problems: x-axis (want to change the range)
# some of the graduation rates are not calculated correctly
## White - Barnwell 48 in 2022, Ornageburg in 2018 and 2019
## Black - Bamberg 3 in all, Barnwell 48 in all, 


#%%
# Fourth and Fifth Graphs - Counties with the highest and lowest parity scores in 2023

# Creating a dataframe that is only 2023
final_2023 = final[final['Year'] == '23']
# sorting in descending order
final_parity_w = final_2023.sort_values(by='S-T Parity (W)', ascending = False)
final_parity_b = final_2023.sort_values(by='S-T Parity (B)', ascending = False)
final_parity_h = final_2023.sort_values(by= 'S-T Parity (H)', ascending = False)

highest_parity_w = final_parity_w.head(10)
highest_parity_w.set_index('District').plot(kind='bar', y = 'S-T Parity (W)')
plt.ylabel('Parity Score')
for i, parity in enumerate(highest_parity_w['S-T Parity (W)']):
        plt.text(i, parity, f"{parity:.2f}", ha='center', va='bottom', fontsize=10)
plt.tight_layout()



# Sixth and Seventh Graphs - Counties with the highest and lowest graduation rates in 2023
# sorting in descending order
final_grad_w = final_2023.sort_values(by='Graduation Rate - W', ascending = False)
final_grad_b = final_2023.sort_values(by='Graduation Rate - B', ascending = False)
final_grad_h = final_2023.sort_values(by= 'Graduation Rate - H', ascending = False)

lowest_grad_w = final_grad_w.tail(10)
lowest_grad_w.set_index('District').plot(kind='bar', y = 'Graduation Rate - W')
plt.ylabel('Graduation Rate')
for i, grad in enumerate(lowest_grad_w['Graduation Rate - W']):
        plt.text(i, parity, f"{grad:.2f}", ha='center', va='bottom', fontsize=10)
plt.tight_layout()

# Eighth visualization - Table







