# Question 1: Basic Function Definition and Calling

# TODO: Define a function called 'greet' that prints "Hello, 
def greet():
    print(f'Hello, World!')
 
# TODO: Call the 'greet' function
greet()
#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# # TODO: Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
name=input("Name: ")
def personalized_greeting(name):
    print(f'hello, {name}')


# TODO: Call the 'personalized_greeting' function with your name)
personalized_greeting(name)
----------------------------------------------------------------------------------
# Question 3: Function with Return Vanumber = 5
# TODO: Define a function called 'square' that takes a number as a parameter and returns its squar
def square(number):
    return number**2
# # TODO: Call the 'square' function with the number 5 and print the result
    print(square (number))

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# TODO: Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area(length, width):
    answer=length*width
    return answer
# TODO: Call the 'rectangle_area' function with length 4 and width 5, and print the result
print(f'rectangle_area, {4, 5}')
#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(function,number):
    return function(number)
# TODO: Define a function called 'double' that takes a number as a parameter and returns its double
def double(number):
    return number*2


# TODO: Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
double = apply_operation(double,7)
print(double)

# TODO: Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
def square(number):
    return number*number
square=apply_operation(square,3)
print(square)
a callback function is a function that is used as paramitar 

for loop



while loop 
count=0 (means it will start to count from 0)
while count<5: ( a condition that has external value)
    print(count)
    #increment (the increase in number)
    #decrement(decrease in numbers)


    