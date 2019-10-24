#Omair Duadu
#Lab1 Exam 24/10/2019
#Notepad++

import math

#taking the number of rows which are to be created
input_h =input(print("\n\nHow many rows would you like in you triangle : \n"))
h = int(input_h)


# this function will create the lists and store the data
def make_new_row(rows):
    new_row = [] 
    for follow in range(rows): 
        row = [] # something to hold the elements        
        
        for element in range(follow + 1): 
            # using .append function
            rows.append(combination(follow, element))
        new_row.append(rows)
        
    return new_row

# this function is in responsible for all the calculations
def calculations(x, y): # [1,1] are x and y
    return int((math.factorial(x)) / ((math.factorial(y)) * math.factorial(x - y)))



# now we can print the new rows which have been calculated
for printer in make_new_rowl(h):
    print(printer)

    
# i had started to get confused by  all the rows at this stage to be honest
