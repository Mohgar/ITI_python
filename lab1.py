

#prob 1
#1. Write a program that counts up the number of
#vowels [a, e, i, o, u] contained in the string.


def count_vowels(word):
    vowels = ["a","e","i","o","u"]
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    if count == 0 :
        print("No vowels found")
    else:  
        print(count) 

count_vowels("ahmed")

count_vowels("AHMED")
count_vowels("hhhhh")
#---------------------------------------------------------------------------------#

# #prob 2
# 2. Write a function that accepts two arguments (length,
# start) to generate an array of a specific length filled
# with integer numbers increased by one from start.


def array_generator(length:int, start:int ):
    array = []
    for i in range(length):
        array.append( start)
        start += 1
    return array

print(array_generator(5, 1))

#another way 


def array_generator_v2(length, start):
    return [start + i for i in range(length)]

print(array_generator_v2(5, 1))

#----------------------------------------------------------------------------------#

# #prob 3
#3. Fill an array of 5 elements from the user, Sort it in
# descending and ascending orders then display the
# output .

def sorted_array():
    my_array=[]
    for i in range(5):
        print(f"Enter number {i+1}:")  
        while True:
            try:
                my_array.append(int(input("Enter an integer: ")))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
    print("Array before sorting: ", my_array)  


    my_array.sort()
    print("Array in ascending order: ", my_array)
    my_array.sort(reverse=True)
    print("Array in descending order: ", my_array)

    
sorted_array()

#----------------------------------------------------------------------------------#

#prob 4

# 4. Write a function that takes a number as an
# argument and if the number divisible by 3 return
# "Fizz" and if it is divisible by 5 return "buzz" and if is
# is divisible by both return "FizzBuzz"


def number(number):
    try:
        if number < 0:
            return "The input should be a positive integer"
        elif number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return "this number is not divisible by 3 or 5"
    except TypeError:
        return "The input should be an integer"
    


try:
    print(number(llll))
except NameError:
    print("Name 'llll' is not defined")

#---------------------------------------------------------------------------------#
#prob 5
# 5. Write a Python function that checks whether a
# passed string is palindrome or not.Note: A
# palindrome is a word, phrase, or sequence that
# reads the same backward as forward, e.g., madam
# or nurses run {ignoring the spaces }.

def palindorme_word(word):
    if type(word) == str:
        word = word.lower().replace(" ", "") 
        if len(word) < 2:
            return True  
        else:
            return word == word[::-1]
    else:
        return "The input should be a string"
    
        

print(palindorme_word("mohm"))

#--------------------------------------------------------------------------------#


#prob 6

#6. Write a function that takes a string and prints the
# longest alphabetical ordered substring occured. For
# example, if the string is 'abdulrahman' then the
# output is: Longest substring in alphabetical order is:
# abdu

def longest_alphabetical(word):
    longest = ""
    current = ""

    if type(word) == str:
        word = word.lower().replace(" ","")
        for i in range(len(word)):
            if i == 0 or word[i] >= word[i-1]:
                current += word[i]
            else:
                current = word[i]
        if len(current) > len(longest):
            longest = current
        return longest
    else:
        return "The input should be a string"
           
        
            

print(longest_alphabetical("rhmanabdu"))

#---------------------------------------------------------------------------------#

def add_two_numbers(num1,num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return num1 + num2
    except ValueError:
        return "Both inputs should be integers"
    

print(add_two_numbers(10, 20))

#---------------------------------------------------------------------------------#


def swap_two_numbers(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return num2, num1
    except ValueError:
        return "Both inputs should be integers"
    

print(swap_two_numbers(10, 20))

#-------------------------------------------------------------------------------------#


def check_prime_num(num):
    try:
        num = int(num)
        if num <= 1:
            return False
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    except ValueError:
        return "The input should be an integer"
    


#---------------------------------------------------------------------------------------------#


def reverse_string():
    while True:

            input_string = str(input("please enter a string to be reversed: ")).strip()
            if input_string.isalpha():
                if len(input_string) < 2:
                    print("minimum char to be reversed is 2 ")
                    continue

                
                else:
                    print(input_string[::-1])
                    break
                    
            else:
                print("please enter string")
                continue

reverse_string()
        

