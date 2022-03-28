# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019357    
  
# Date: 28/11/2020

#References
# Same references from for loops and lists in part 3 and 2.


mylist = ['''Progress
Progress (module trailer)
Progress (module trailer)
Do not Progress - module retriever
Do not Progress - module retriever
Do not Progress - module retriever
Do not Progress - module retriever
Exclude
Exclude
Exclude''']

mylist2=['''Progress  1: * 
Trailing   2 : ** 
Retriever 4: **
Excluded 3: ***

10 outcomes in total.''']

# Making mylist and mylist2 to combine them together to make the output similar to the actual output.

for i in mylist:
    print(i)
for i in mylist2: # Creating for loop to remove all the inverted commas and the brackets and making the list print horizontal way.
    print()
    print(i)
