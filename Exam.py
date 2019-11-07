#Omair Duadu
#Lab1 Exam 4/11/2019
#Notepad++
# Program will create a pascals triangle using the mat library.
# the program uses lists to store the values and print them.
# the number of rows is dependabt on how many the user chooses.

import math # importing the math library

rows_desired = int(input("\nHow many rows of the Triangle do you want?\n\n:"))
# taking input from user about the desired number of rows to be printed 
    
#function which does all the maths through using the math.factorial 
def combination(x, y): # The calculations of the individual lists
    return int((math.factorial(x)) / ((math.factorial(y)) * math.factorial(x - y)))

#function which does all the appending.
def triangle_appending(rows):
    pascal_list = []     # need something to collect our results in

        
    for i in range(rows): #  this loop will append the new calculations into a list 
                          #  called row and then append row into pascal_list
        new_row = [] # need a list to collect the rows which were just calculated
        
        for old in range(i + 1): #
            new_row.append(combination(i, old))# appending the figures into the list row
        
        pascal_list.append(new_row) #appending the row to the bigger list called pascal_list
        
    return pascal_list



for print_rows in triangle_appending(rows_desired):# loop to print the desired number of rows
    print(print_rows)# printing rows :)

'''

Reflecting back to the work i realised the errors i had, the errors i had made 
revolve around my layout. I had made the mathematical function to late in the 
code so it was not accessed by the appending function.

Thank You
'''
