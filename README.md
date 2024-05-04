# Diversity and Outcomes
## Hypothesis and Motivation
### Hypothesis
My hope for this repository is that it gives school districts, education analysts, and anyone else interested in education topics and method to take a state of their choosing and measure the impact of student-teacher parity (or the lack thereof) on student outcomes, specifically graduation rates. 

I hypothesize that the state of South Carolina, which I use as a model, will not have much student-teacher parity among Black and Hispanic students and teachers, but will probably have parity among White students and teachers. I hope that someone will use this repository to see if this trend is the same across the country. 

### Motivation
The Brookings Institution published an article in 2017 titled ["4 ways to measure diversity among public school teachers"](https://www.brookings.edu/articles/four-ways-to-measure-diversity-among-public-school-teachers/).

 In this article, the authors discuss the student-teacher diversity gap, diversity gaps based on the adult population, target-based diversity gaps, and the student-teacher parity ratio as different ways to measure teacher diversity. I found the student-teacher parity ratio to be the most interesting because it seems to capture the context of disparities better than a percentage point (p.p.) gap might. For example, let's say District A has 20% teachers of color and 40% students of color. That's a 20 p.p. difference. District B, on the other hand, had 40% teachers of color and 60% students of color. There is still a 20 p.p. difference. However, the student-teacher diversity gap ignores context. A parity ratio will give us the share of 

 ## Data and Summary
 ### Data
 The data includes 
sc report card for grad
sc department of education for student and teacher.
Only using hispanic, black, and white students. 

Hispanic is a race rather than an ethnicity marker in this data
A lot of the information on asian, native american, other races is missing so its not included. Perhaps a future user might do this same work in states with higher populations of Asian and Native American students, more on the west coast. 

I've also included a shp file from 2023, which is used to make all graphs. A number of counties consolidated between the 2018 and 2023 school years in SC. In the years before their consolidation, they are consolidated to reflect an updated and consistent measure of parity. If you wish to view parity pre and post consolidation, you can remove the lines of code in the cleaning scripts that combines these districts.
Additionally, special schools (career schools, governor's schools, schools run through the department of corrections and juvenile justice) are removed. If you wish to add these back, just take out the lines of code that removes them. 

### Summary
In this repository, you'll find scripts, 3 dedicated to cleaning student, teacher, and graduation rate data, 1 dedicated to joining that cleaned data together, 1 dedicated to calculating parity ratios, and 2 dedicated to creating maps and time series graphs. 

The cleaning scripts 


