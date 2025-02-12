#prob 1
# 1. Write a Python program to read a file line by line
# and store it into a list. 

def write_file(filename):
   
    with open(filename, 'r') as file:
        
        lines = file.readlines()
        my_list = [line.strip() for line in lines]
       
    return my_list


    # return my_list
try:
    print(write_file("file1.txt"))

except FileNotFoundError:
    print("The file was not found.")

except Exception as e:
    print("An error occurred:", e)

#---------------------------------------------------------------------------------#
#prob 2
# 2. Create a list of strings , Add to it yourname then
# Write the list to a new File .

def write_to_file():
    my_list = ["mohamed hgar\n", "heba hgar"]        
    with open("file2.txt", 'w', encoding= "utf-8") as file:
        for item in my_list:
            file.write(item)

    with open("file2.txt", 'w', encoding= "utf-8") as file:
        file.write("mahmoudhgar\nmena hgar")

    

try:
    write_to_file()
except Exception as e :
    print("An error occurred:", e)


#---------------------------------------------------------------------------------#

#prob 3
# 3. Create package directory called Calculator and add
# file called my_functions that have the following
# function
# a. Sum Function
# b. Subtract Function
# c. Divide Function
# d. Multiply Function
  
from Calculator.my_function import (
sum_function,
  subtract_function,
  divide_function,
  multiply_function) 

print(sum_function(3, 5,8))
print(subtract_function(2, 5,8))
print(divide_function(3, 2))
print(multiply_function(3, 6))

#---------------------------------------------------------------------------------#


#prob 4
#4. Use the created Package in python code that takes
# input operand from User : 0->sum , 1->subtract ,
# 2->divide , 3 ->Multiple.
# a. If one of the two numbers is zero and operand
# is subtract raise Value Error with message “
# subtracting zero from Number “.
# b. If one of the two numbers is zero and operand
# is divide raise Zero division Error with message
# “ can’t divide with zero “.
# c. If one of the two numbers is zero and operand
# is Multiply raise Value Error with message “
# Multiply with Zero “. 

#------------------------------------------------------------------------------#
#lecture problems
#prob 1
# Write a function in Python that accepts two string parameters. The ﬁrst parameter will be a string of characters,
# and the second parameter will be the same string of characters, but they’ll be in a different order and have one
# extra character. The function should return that extra character.
# ○
# For example, if the ﬁrst parameter is “eueiieo” and the second is “iieoedue,” then the function should
# return “d.” 

def find_extra_char(a:str, b:str):
   
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both parameters should be strings")
    
    if abs(len(a.strip())-len(b.strip())) != 1:
        raise ValueError("String 'a' should be exactly one character longer than 'b'")
    
    for char in b:
        if char not in a:
            return char
    
    
        
    
print(find_extra_char("eueiieo", "iieoedue"))  

#----------------------------------------------------------------
#prob 2
# Write a function that accepts a number as a parameter. The function should return a number that’s the difference
# between the largest and smallest numbers that the digits can form in the number.
# ○
# For example, if the parameter is “213”, the function should return “198”, which is the result of 123
# subtracted from 321.


def largest_smallest_difference(num:int):
    if not isinstance(num, int):
        raise TypeError("The parameter should be an integer")
    if num < 10 :
        raise ValueError("The number should be at least two digits")

    digits = [digit for digit in str(num)]
    max_num_list = sorted(digits, reverse= True)
    max_num = int("".join(max_num_list))
    min_num_list  = sorted(digits)
    min_num = int("".join(min_num_list))
    return max_num-min_num

print(largest_smallest_difference(213))  

