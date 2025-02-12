# a. Sum Function
# b. Subtract Function
# c. Divide Function
# d. Multiply Function

def sum_function(*args):
    for number in args:
        if not isinstance(number, int):
            raise TypeError("Error: All arguments must be integers")
   
    return sum(args)

def subtract_function(*args):
    for number in args:
        if not isinstance(number, int):
            raise TypeError("Error: All arguments must be integers")
        if number == 0 :
            raise ValueError("Error: Subtracting zero from Number")
   
    return args[0] - sum(args[1:])

def divide_function(a:int,b:int):
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError("Error: Both arguments must be integers")
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero") 
    
    return a / b

def multiply_function(a:int, b:int):
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError("Error: Both arguments must be integers")
    if a == 0 or b == 0:
        raise ValueError("Error: Multiply with Zero")
    return a * b


    
