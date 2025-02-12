#prob 1
# 

def check_number(number):
    while True:
        number = int(input("please inter your number: ").strip())
        if isinstance(number, int):
            if number in range(-5, 5):
               return True 
            else:
                print("number out of range (5,-5)") 
                continue
        else:
            print("you should enter integer ")
            continue

print(check_number(5))


#------------------------------------------------------------#

#prob 2

Write a Python program to convert two lists into a
dictionary in a way that item from list1 is the key
and item from list2 is the value. 

def convert_lists(list1: list, list2: list):

    if not isinstance(list1, list) or not isinstance(list2, list):
        return "both inputs should be lists"
    
    if not list1 or not list2:
        return "boths lists shouldnt be empty"
    
    new_dict = dict(zip(list1, list2))

    if len(list1) > len(list2):
        for i in list1[len(list2):]:
            new_dict[i] = None
             
    if len(list2)> len(list1):
        for j in list2[len(list1):]:
            new_dict[j] = None

    return f"your new dictionary is {new_dict}"


print(convert_lists([1,2,3,4], [5,6])) 

#----------------------------------------------------------------
 #prob 3
 Write a Python function to create and print a list
where the values are square of numbers between 1
and 30 (both included).


def create_square_list():
    return print([i**2 for i in range(1, 31)])


create_square_list()


#--------------------------------------------------------------


#prob 4
# Write a Program that takes a list of 5 numbers
# [3,6,4,0,8] then
# a. Remove the last element in list .
# b. Add in the second place ‘R’.
# c. Ask the user to input specific number in list
# then delete it { by taking the list element not
# index}.

def list_manuiplation():
    new_list = []
    for i in range(5):
        while True:
            user_input = int(input(f"please enter number {i+1}: ").strip())
            if not user_input:
                print("your input cant be empty")
                continue
            elif not isinstance(user_input, int):
                print("you should inter integer")
                continue
            else:
                break
        new_list.append(user_input)
    
    new_list.pop(len(new_list)-1)
    print(f"after removing last element list is {new_list}")
    new_list.insert(1, "R")
    print(f"after adding 'R' in second place list is {new_list}")
    while True:

        user_input = int(input("please enter specific number to remove: ").strip())
        
        if not user_input:
            print("your input cant be empty")
            continue
        elif not isinstance(user_input, int):
            print("you should inter integer")
            continue
        elif user_input in new_list:
            new_list.remove(user_input)
            print(f"after removing your input element list is {new_list}") 
            break
        else:
            print("your number is not in ths list ")
            continue
            
list_manuiplation()

#------------------------------------------------------#
#prob 5
# Create 2 dictionaries and append the two in one
# .{take into consideration unique keys }

def create_two_dict(dict1 : dict, dict2 : dict):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return "both inputs must be dictionary"
    
    if not dict1 or not dict2:
        return "both inputs cant be empty"
    
    combined_dic = dict1.copy()
    for key, value in dict2.items():
        if key not in combined_dic:
            combined_dic[key]=value

    return combined_dic

print(create_two_dict({"key":"value"}, {"key2":"value2"}))


#another way 

def create_dict(dict1:dict, dict2:dict):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return "both inputs must be dictionary"
    
    if not dict1 or not dict2:
        return "both inputs cant be empty"
    combined_dic = {**dict1,**dict2}
    return combined_dic

print(create_dict({"key":"value"}, {"key2":"value2"}))


    












