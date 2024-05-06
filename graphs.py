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
import numpy as np

# Reading pickle file
final = pd.read_pickle('final.pkl')
plt.rcParams['figure.dpi'] = 500

# First Graph - scatterplot, white student-teacher ratio
customw = ('violet', 'plum', 'hotpink', 'lightpink', 'magenta', 'red')
sns.set_palette(customw)
ax = sns.relplot(data = final, x='S-T Parity (W)', y='Graduation Rate - W', kind='scatter', hue ='Year')
plt.ylabel('Graduation Rate')
plt.xlabel('Parity Score')
plt.title('Student-Teacher Parity and Graduation Rates Overtime - W')

# Second Graph - scatterplot, black student-teacher ratio
custom = ('cornflowerblue', 'royalblue', 'blue', 'slateblue', 'dodgerblue', 'darkturquoise')
sns.set_palette(custom)
ax = sns.relplot(data = final, x='S-T Parity (B)', y='Graduation Rate - B', kind='scatter', hue ='Year')
plt.ylabel('Graduation Rate')
plt.xlabel('Parity Score')
plt.title('Student-Teacher Parity and Graduation Rates Overtime - B')
plt.xlim(right = 1.5)
plt.ylim(top = 1.1)

# Third Graph - scatterplot, hispanic student-teacher ratio
custom = ('springgreen', 'lime', 'darkgreen', 'mediumaquamarine', 'chartreuse', 'yellowgreen')
sns.set_palette(custom)
ax = sns.relplot(data = final, x='S-T Parity (H)', y='Graduation Rate - H', kind='scatter', hue ='Year')
plt.ylabel('Graduation Rate')
plt.xlabel('Parity Score')
plt.title('Student-Teacher Parity and Graduation Rates Overtime - H')
plt.xlim(right = 1.5)
plt.ylim(top = 1.1)


#%%

# Fourth and Fifth Graphs - Counties with the highest and lowest parity scores in 2023

# Creating a dataframe that is only 2023 - horizontal bars
final_2023 = final[final['Year'] == '23']
# sorting in descending order
final_parity_w = final_2023.sort_values(by='S-T Parity (W)', ascending = False)
final_parity_b = final_2023.sort_values(by='S-T Parity (B)', ascending = False)
final_parity_h = final_2023.sort_values(by= 'S-T Parity (H)', ascending = False)

#Highest Parity 
## White
highest_parity_w = final_parity_w.head(10)
highest_parity_w.set_index('District').plot(kind='bar', y = 'S-T Parity (W)')
plt.ylabel('Parity Score')
plt.title('Districts with the Highest Parity Scores - W')
for i, parity in enumerate(highest_parity_w['S-T Parity (W)']):
        plt.text(i, parity, f"{parity:.2f}", ha='center', va='bottom', fontsize=10)
plt.tight_layout()

## Black


## Hispanic



# Lowest Parity

## White


## Black


## Hispanic



# Sixth and Seventh Graphs - Counties with the highest and lowest graduation rates in 2023
# sorting in descending order
final_grad_w = final_2023.sort_values(by='Graduation Rate - W', ascending = False)
final_grad_b = final_2023.sort_values(by='Graduation Rate - B', ascending = False)
final_grad_h = final_2023.sort_values(by= 'Graduation Rate - H', ascending = False)

# Visuals
lowest_grad_w = final_grad_w.tail(10)
lowest_grad_w.set_index('District').plot(kind='bar', y = 'Graduation Rate - W')
plt.ylabel('Graduation Rate')
plt.title('Districts with the Lowest Graduation Rates - W')
for i, grad in enumerate(lowest_grad_w['Graduation Rate - W']):
        plt.text(i, parity, f"{grad:.2f}", ha='center', va='bottom', fontsize=10)
plt.tight_layout()


highest_parity_b = final_parity_b.head(10)
highest_parity_b.set_index('District').plot(kind='bar', y = 'S-T Parity (B)')
plt.ylabel('Parity Score')
plt.title('Districts with the Highest Parity Scores - B')
for i, parity in enumerate(highest_parity_b['S-T Parity (B)']):
        plt.text(i, parity, f"{parity:.2f}", ha='center', va='bottom', fontsize=10)
plt.tight_layout()


lowest_grad_b = final_grad_b.tail(10)
lowest_grad_b.set_index('District').plot(kind='bar', y = 'Graduation Rate - B')
plt.ylabel('Graduation Rate')
plt.title('Districts with the Lowest Graduation Rates - B')
for i, grad in enumerate(lowest_grad_b['Graduation Rate - B']):
        plt.text(i, parity, f"{grad:.2f}", ha='center', va='bottom', fontsize=10)








