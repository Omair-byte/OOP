#Omair Duadu
#Lab1 Exam 4/11/2019
#Notepad++

import math # importing the math library

rows_desired = int(input("\nHow many rows of the Triangle do you want?\n"))
# taking input from user about the desired number of rows to be printed 
    
#function which does all the maths    
def combination(x, y): # The calculations of the individual lists
    return int((math.factorial(x)) / ((math.factorial(y)) * math.factorial(x - y)))

#function which does all the appending.
def triangle_pending(rows):
    pascal_list = []     # need something to collect our results in

        
    for i in range(rows): #  this loop will append the new calculations into a list 
                          #  called row and then append row into pascal_list
        new_row = [] # need a list to collect the rows which were just calculated
        
        for old in range(i + 1): #         
            new_row.append(combination(i, old))# appending the figures into the list row
        
        pascal_list.append(row) #appending the row to the bigger list called pascal_list
        
    return pascal_list



for print_rows in triangle_pending(rows_desired):# loop to print the desired number of rows
    print(print_rows)# printing rows :)

'''

Reflecting back to the work i reakised the errors i had, the errors i had made 
revolve around my layout. I had made the mathematical function to late in the 
code so it was not accessed by the appending function.


'''
