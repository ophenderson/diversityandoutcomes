# Importing
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Reading pickle file
final = pd.read_pickle('final.pkl')
plt.rcParams['figure.dpi'] = 500

# Scatterplot - White Teacher-Student ratio overtime
customw = ('violet', 'plum', 'hotpink', 'lightpink', 'magenta', 'red')
sns.set_palette(customw)
ax = sns.relplot(data = final, x='T-S Parity (W)', y='Graduation Rate - W', kind='scatter', hue ='Year')
plt.ylabel('Graduation Rate')
plt.xlabel('Parity Score')
plt.title('Teacher-Student Parity and Graduation Rates Overtime - W')
plt.savefig('scatterW.png')

# Scatterplot - Black Teacher-Student ratio overtime
custom = ('cornflowerblue', 'royalblue', 'blue', 'slateblue', 'dodgerblue', 'darkturquoise')
sns.set_palette(custom)
ax = sns.relplot(data = final, x='T-S Parity (B)', y='Graduation Rate - B', kind='scatter', hue ='Year')
plt.ylabel('Graduation Rate')
plt.xlabel('Parity Score')
plt.title('Teacher-Student Parity and Graduation Rates Overtime - B')
plt.xlim(right = 1.5)
plt.ylim(top = 1.1)
plt.savefig('scatterB.png')

# Scatterplot - Hispanic Teacher-Student ratio overtime
custom = ('springgreen', 'lime', 'darkgreen', 'mediumaquamarine', 'chartreuse', 'yellowgreen')
sns.set_palette(custom)
ax = sns.relplot(data = final, x='T-S Parity (H)', y='Graduation Rate - H', kind='scatter', hue ='Year')
plt.ylabel('Graduation Rate')
plt.xlabel('Parity Score')
plt.title('Teacher-Student Parity and Graduation Rates Overtime - H')
plt.xlim(right = 1.5)
plt.ylim(top = 1.1)
plt.savefig('scatterH.png')

# Creating a DataFrame that trims 'final' down to only the year 2023
final_2023 = final[final['Year'] == '23']

# Sorting parity scores in descending order
final_parity_w = final_2023.sort_values(by='T-S Parity (W)', ascending = False)
final_parity_b = final_2023.sort_values(by='T-S Parity (B)', ascending = False)
final_parity_h = final_2023.sort_values(by= 'T-S Parity (H)', ascending = False)

# Bar - Top 10 Districts with the Highest Teacher-Student parity (White)
highest_parity_w = final_parity_w.head(10)
highest_parity_w.set_index('District').plot(kind='barh', y = 'T-S Parity (W)')
plt.xlabel('Parity Score')
plt.ylabel('District')
plt.title('Top 10 Districts with the Highest Parity Scores - W')
plt.tight_layout()
plt.legend().remove()
plt.savefig('HparityW.png')

# Bar - Top 10 Districts with the Highest Teacher-Student parity (Black)
highest_parity_b = final_parity_b.head(10)
highest_parity_b.set_index('District').plot(kind='barh', y = 'T-S Parity (B)')
plt.xlabel('Parity Score')
plt.ylabel('District')
plt.title('Districts with the Highest Parity Scores - B')
plt.tight_layout()
plt.legend().remove()
plt.savefig('HparityB.png')

# Bar - Top 10 Districts with the Highest Teacher-Student parity (Hispanic)
highest_parity_h = final_parity_h.head(10)
highest_parity_h.set_index('District').plot(kind='barh', y = 'T-S Parity (H)')
plt.xlabel('Parity Score')
plt.ylabel('District')
plt.title('Districts with the Highest Parity Scores - H')
plt.tight_layout()
plt.legend().remove()
plt.savefig('HparityH.png')

# Bar - Top 10 Districts with the Lowest Teacher-Student parity (White)
lowest_parity_w = final_parity_w.tail(10)
lowest_parity_w.set_index('District').plot(kind='barh', y = 'T-S Parity (W)')
plt.xlabel('Parity Score')
plt.ylabel('District')
plt.title('Districts with the Lowest Parity Scores - W')
plt.tight_layout()
plt.legend().remove()
plt.savefig('LparityW.png')

# Bar - Top 10 Districts with the Lowest Teacher-Student parity (Black)
lowest_parity_b = final_parity_b.tail(10)
lowest_parity_b.set_index('District').plot(kind='barh', y = 'T-S Parity (B)')
plt.xlabel('Parity Score')
plt.ylabel('District')
plt.title('Districts with the Lowest Parity Scores - B')
plt.tight_layout()
plt.legend().remove()
plt.savefig('LparityB.png')

# Bar - Top 10 Districts with the Lowest Teacher-Student parity (Hispanic)
# Original 10 had parity scores of 0, meaning they have 0 hispanic teachers
lowest_parity_h = final_parity_h[final_parity_h != 0].dropna().tail(10)
# Original 10 had parity scores of 0, meaning they have 0 hispanic teachers, skipped these to get to the 10 lowest with values bigger than 0
lowest_parity_h.set_index('District').plot(kind='barh', y = 'T-S Parity (H)')
plt.xlabel('Parity Score')
plt.ylabel('District')
plt.title('Districts with the Lowest Parity Scores - H')
plt.tight_layout()
plt.legend().remove()
plt.savefig('LparityH.png')

# Sorting graduation rates in descending order
final_grad_w = final_2023.sort_values(by='Graduation Rate - W', ascending = False)
final_grad_b = final_2023.sort_values(by='Graduation Rate - B', ascending = False)
final_grad_h = final_2023.sort_values(by= 'Graduation Rate - H', ascending = False)

# Bar - Top 10 Districts with the Lowest Graduation Rates (White)
lowest_grad_w = final_grad_w.tail(10)
lowest_grad_w.set_index('District').plot(kind='barh', y = 'Graduation Rate - W')
plt.xlabel('Graduation Rate')
plt.ylabel('District')
plt.title('Districts with the Lowest Graduation Rates - W')
plt.tight_layout()
plt.legend().remove()
plt.savefig('LgradW.png')

# Bar - Top 10 Districts with the Lowest Graduation Rates (Black)
lowest_grad_b = final_grad_b.tail(10)
lowest_grad_b.set_index('District').plot(kind='barh', y = 'Graduation Rate - B')
plt.xlabel('Graduation Rate')
plt.ylabel('District')
plt.title('Districts with the Lowest Graduation Rates - B')
plt.tight_layout()
plt.legend().remove()
plt.savefig('LgradB.png')

# Bar - Top 10 Districts with the Lowest Graduation Rates (Hispanic)
## Makes a mini dataframe of the 10 lowest values, for this one I had to dropna because the first 24 values are all missing
lowest_grad_h = final_grad_h.dropna().tail(10)
lowest_grad_h.set_index('District').plot(kind='barh', y = 'Graduation Rate - H')
plt.xlabel('Graduation Rate')
plt.ylabel('District')
plt.title('Districts with the Lowest Graduation Rates - H')
plt.tight_layout()
plt.legend().remove()
plt.savefig('LgradH.png')

# Bar - Top 10 Districts with the Highest Graduation Rates (White)
highest_grad_w = final_grad_w.head(10)
highest_grad_w.set_index('District').plot(kind='barh', y = 'Graduation Rate - W')
plt.xlabel('Graduation Rate')
plt.ylabel('District')
plt.title('Districts with the Highest Graduation Rates - W')
plt.tight_layout()
plt.legend().remove()
plt.savefig('HgradW.png')

# Bar - Top 10 Districts with the Highest Graduation Rates (Black)
highest_grad_b = final_grad_b.head(10)
highest_grad_b.set_index('District').plot(kind='barh', y = 'Graduation Rate - B')
plt.xlabel('Graduation Rate')
plt.ylabel('District')
plt.title('Districts with the Highest Graduation Rates - B')
plt.tight_layout()
plt.legend().remove()
plt.savefig('HgradB.png')

# Bar - Top 10 Districts with the Highest Graduation Rates (Hispanic)
highest_grad_h = final_grad_h.head(10)
highest_grad_h.set_index('District').plot(kind='barh', y = 'Graduation Rate - H')
plt.xlabel('Graduation Rate')
plt.ylabel('District')
plt.title('Districts with the Highest Graduation Rates - H')
plt.tight_layout()
plt.legend().remove()
plt.savefig('HgradH.png')




