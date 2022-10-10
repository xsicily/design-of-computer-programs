# User Instructions
#
# Use a list comprehension to identify all the TAs 
# Who are teaching a 300 level course (which would
# be Gundega and Job). The string.find() function
# may be helpful to you.
#
# Your ta_300 variable should be a list of 2 strings:
# ta_300 = ['Gundega is the TA for CS373',
#           'Job is the TA for CS387']

# example 1:
ta_data = [['Peter', 'USA', 'CS262'],
           ['Andy', 'USA', 'CS212'],
           ['Sarah', 'England', 'CS101'],
           ['Gundega', 'Latvia', 'CS373'],
           ['Job', 'USA', 'CS387'],
           ['Sean', 'USA', 'CS253']]

ta_facts = [name + ' lives in ' + country + ' and is the TA for ' +
            course for name, country, course in ta_data]

for row in ta_facts:
    print(row)

# example 2:
remote_ta_facts = [name + ' lives in ' + country + ' and is the TA for ' +
            course for name, country, course in ta_data if country != 'USA']

for row in remote_ta_facts:
    print(row)

# practice
ta_300 = [name + ' is the TA for ' + course for name, country, course in ta_data 
        if course.find('3', 0, 3)==2]


print(ta_300)