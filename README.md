# Diversity and Outcomes
## What's does this repository do? (B.L.U.F.)
 
 This repository conducts an analysis of student-teacher parity and its impact on graduation rates for the state of South Carolina between 2018-2023. Scripts allow users to process and visualize data. My hope for this repository is that it provide school districts, education analysts, and anyone else interested in education topics with a method to take a state of their choosing and measure the impact of student-teacher parity (or the lack thereof) on student outcomes, specifically graduation rates.

 ## What's my Why?

 For the purposes of my own analysis, I hypothesize that the state of South Carolina, which I use as a model, will:
1. Have more disparity among Black and Hispanic students and teachers than White students and teachers.
2. Have a negative relationship between student-teacher parity and graduation rates for Black and Hispanic students and no relationship between student-teacher parity and graduation rates for White students.


The Brookings Institution published an article in 2017 titled ["4 ways to measure diversity among public school teachers"](https://www.brookings.edu/articles/four-ways-to-measure-diversity-among-public-school-teachers/).

 In this article, the authors discuss the student-teacher diversity gap, diversity gaps based on the adult population, target-based diversity gaps, and the student-teacher parity ratio as different ways to measure teacher diversity. I found the student-teacher parity ratio to be the most interesting because it seems to capture the context of disparities better than a percentage point (p.p.) gap. For example, let's say District A has 20% teachers of color and 40% students of color. That's a 20 p.p. difference. District B, on the other hand, had 40% teachers of color and 60% students of color. There is still a 20 p.p. difference. However, the student-teacher diversity gap ignores context. A parity ratio will give us the share of X students to the share of X teachers (X being "race") and will allow us better understand the student-ratio and compare it against graduation rates. 

## Input Data

The data includes:
1. [Graduation Rates](https://screportcards.com/)
- Graduation Rates are pulled from SC Report Cards, which partners with the South Carolina Education Oversight Committee to collect this data. The data is distributed by a number of different identifiers including race, gender, and disability status. In order to complete this analysis, you will need to download graduation rates from your state of choice's Department of Education website or another reliable education data source. 
2. [180-Day Active Student Headcounts](https://ed.sc.gov/data/other/student-counts/active-student-headcounts/)
- School districts in South Carolina are required to establish a calendar with a minimum of 180 days of instruction. Therefore, I pulled data from the South Carolina Department of Education that includes a student headcount from the 180th day of the school year. The data is also distributed by race, gender, and pupils in poverty/eligible for free lunch. In order to complete this analysis, you will need to download student headcount data, preferably accounting for the minimum number of instruction days required. 
3. [Teacher Counts by Race and Gender](https://ed.sc.gov/data/other/teacher-data/)
- Teacher counts are pulled from the South Carolina Department of Education and are distributed by race and gender. In order to complete this analysis, you will need teacher diversity data from your state of choice's Department of Education website. 

Note: **Make sure your data is separated by district.**

## Scripts and Folders

In this repository, you'll find 7 scripts, 3 dedicated to cleaning student, teacher, and graduation rate data, 1 dedicated to joining that cleaned data together, 1 dedicated to calculating parity ratios, and 2 dedicated to creating visualizations. 

Input data and outputs for this repository are all organized into labeled folders. Before you start running scripts, you should gather all of your necessary input data and organize it into a folder called 'raw'.

Scripts should be run in the order that they appear below. 

### Data Cleaning Scripts 
1. `Cleaning Scripts/clean_grad.py` 
    - This script will pull graduation rate files from your 'raw' folder, perform a number of cleaning functions on your the data, and save your final cleaned dataframe as a pickle file. In order for this script to best serve your analysis:
        - Look it over 
        - Edit the existing steps to reflect your data
        - Remove any steps that don't serve you
        - Add cleaning steps you think are necessary 
        
    - The "District Column Consistency" code is especially important, as it will allow you to make sure that the column you wish to perform any join functions on is consistent across all of your data.

2. `Cleaning Scripts/clean_student.py`
    - This script will pull student headcount files from your 'raw' folder, perform a number of cleaning functions on your the data, and save your final cleaned dataframe as a pickle file. In order for this script to best serve your analysis:
        - Look it over 
        - Edit the existing steps to reflect your data
        - Remove any steps that don't serve you
        - Add cleaning steps you think are necessary 
        
    - The "District Column Consistency" code is especially important, as it will allow you to make sure that the column you wish to perform any join functions on is consistent across all of your data.

3. `Cleaning Scripts/clean_teacher.py`
    This script will pull teacher diversity files from your 'raw' folder, perform a number of cleaning functions on your the data, and save your final cleaned dataframe as a pickle file. In order for this script to best serve your analysis:
        - Look it over 
        - Edit the existing steps to reflect your data
        - Remove any steps that don't serve you
        - Add cleaning steps you think are necessary 
        
    - The "District Column Consistency" code is especially important, as it will allow you to make sure that the column you wish to perform any join functions on is consistent across all of your data.

### Technical Scripts
4. `Join and Parity Index Scripts/join.py`
- Conducts an outer join on the 'District' column your 3 cleaned pickle files. Joins grad data onto teacher data, and then student data onto the merged grad and teacher file. Saves the final result as a merged pickle file.
5. `Join and Parity Index Scripts/parity_index.py`
- Calculates teacher-student parity ratios by taking the share of X teachers and comparing it to the share of X students. Saves your final result as a pickle file.

### Visualization Scripts
6. `Visualization Scripts/graphs.py`
- Visualization script thatreates 15 graphs. The first 3 are scatterplots that show the relationship between teacher-student parity and graduation rates over time.

The next 12 are bar graphs that show the top 10 counties with: the highest and lowest parity ratios and the highest and lowest graduation rates. 
7. `Visualization Scripts/table.py`
- Visualization script that contains code to get yearly data from the district of your choosing. 

#### Example Table (data is for Spartanburg County School District 1)
    Year  District        Graduation Rate - W    Graduation Rate - B  
    18    SPARTANBURG 1   0.911392               0.868421   
    19    SPARTANBURG 1   0.912536               0.958333   
    20    SPARTANBURG 1   0.935374               0.968750   
    21    SPARTANBURG 1   0.929260               0.850000   
    22    SPARTANBURG 1   0.937500               0.950000   
    23    SPARTANBURG 1   0.936242               0.923077   

    Graduation Rate - H  T-S Parity (W)  T-S Parity (B)  T-S Parity (H)  
    1.000000             1.183992        0.387630        0.081281  
    0.888889             1.182858        0.456084        0.083158  
    1.000000             1.189535        0.417567        0.081933  
    0.937500             1.202244        0.332662        0.075287  
    0.956522             1.200411        0.289707        0.078736  
    0.897436             1.186380        0.236211        0.192698  

 
# Analysis/Results

## Scatterplots
### White 
- When evaluating parity ratios, a parity score of 1 is best. It means that for every 1 White student, there's 1 White teacher. Being below this threshold means there are not enough teachers to account for students and being above means that...

### Black

### Hispanic



# Notes
[^1]: The counties of Bamberg, Barnwell, Orangeburg, and Hampton all experience consolidation between the 2017-2018 and 2022-2023 school years. This is accounted for in the data. 

[^2]: Hispanic is a race rather than an ethnicity marker in this data. 

[^3]: Other races are included in the data but, alot of their data is missing. Hence, they are removed from the analysis. If you wish to conduct a more extensive analysis that includes other races, you would just simply add their column names to any keep_cols code. 

[^4]: Special schools (career schools, governor's schools, schools run through the department of corrections and juvenile justice, etc) are removed. If you wish to add these back, just take out the lines of code that removes them. 
