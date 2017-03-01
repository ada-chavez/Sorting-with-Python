# Python 3.6.0
#
# Date: 02/28/2017
#
# Author: Ada Chavez
#
# Program: The following is a drill from The Tech Academy demonstrating how to sort a list without the sort function
#
#

# List one
a_list = [67, 45, 2, 13, 1, 998]
empty_a=[]
print (a_list)

# goes through list until it is empty
while a_list:
    for i in range(1000): # sets max range value greater than the biggest value in list
        for x in a_list:
            if x < i: # if value in list is less than range value it will be set to x
                i = x; 
    a_list.remove(i) # removes this value from the original list   
    empty_a.append(i) # places this value into new list
print (empty_a)





# List two
my_list = [89,23,33,45,10,12,45,45,45]
empty_list=[]
print (my_list)


while my_list:
    for i in range(100):
        for x in my_list:
            if x < i:
                i = x;
    my_list.remove(i)    
    empty_list.append(i)
print (empty_list)

