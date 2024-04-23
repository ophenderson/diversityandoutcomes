# This script is going to be used to join (outer join) data for each year into one file so that in the end we have 1 file for each school year that has grad, student, and teacher data
# This script will also drop special school cases (alternative schools, career and technical schools, etc)


# Want to join grad rate onto teacher data by district id and school and then join that onto student data so that in the end the district and district name data looks like it does in the student data
# merged = teacher_data.merge(grad_data, on = 'DISTRICT', how ='outer')