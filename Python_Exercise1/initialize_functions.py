# from operator import add
"""
A function is a block of code that you can name and that performs a certain task. You can run the block many times by
 using the function name. The definition of a function specifies its name and the data the function needs to work.
 Parameters are the variables in the function that hold this data.
"""


# Zero args function
def zero_arg_function():
    print("This is a very basic function without any arguments/parameter\n")


# functions with arguments/parameters
def introduction(first_name, last_name):
    print("Hi, my name is %s %s. Nice to meet you!\n" % (first_name, last_name))


# functions with default arguments/parameters
def introduction_with_default_args(first_name="John", last_name="Doe"):
    print("Hi, my name is %s %s. Nice to meet you!\n" % (first_name, last_name))


# function with a mix of default arguments
# invoke this function with a mix of passing in zero arg, switch first name and last name arg, etc.
def introduction_with_mix_of_default_args(first_name, last_name="Doe"):
    print("Hi, my name is %s %s. Nice to meet you!\n" % (first_name, last_name))


# function that returns value(s)
def product_of_two_num(num1, num2):
    print(num1 * num2)
    return num1 * num2


# function with arbitrary arguments
# User of this function will pass in N number of real numbers, which will be converted into a tuple.
# The for loop inside the function will iterate over the function and sum up all the numbers and return the sum
# Play with this by adding different number of arugments and observe the results
def add_all_nums(*nums):
    sums = 0
    for num in nums:
        sums += num
    print(sums)
    return sums


# double = lambda x: x * 2
# Equivalent function
def double(x):
    print(x * 2)
    return x * 2


print("-------------------------- recursive function ---------------------")
'''
An if statement allows you to set a condition on whether certain code runs. For example, using a variable called 
game_active, you can use an if statement to ensure the code that starts a game runs only if this variable is set to 
True.
'''


# Recursive function is a function that calls itself
# TO understand this, let's compute fibonacci sequence where the sum of previous two numbers equals the current number. 
def fib(num):
    if num < 2:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


# Scoping: variables have different level of visibility based on where they are defined
# Instance level variables are scoped to the class, meaning any function or control statement has access to it
# Function/method level variables are only visible to the function it was declared in 
# variables defined within a control statement is only visible to the block of code within the control statement

# function level scoping: the variable result in the below function is not available outside of subtract function
def subtract(num1, num2):
    result = num1 - num2
    print(result)
    return result


# Control statement level scoping: variable i in the control statement below is only available to the for loop
for i in range(1, 5):
    print(i)

print("------------ End of Function Initialization ---------------------\n\n")

# TODO: Write a function that returns true if the input string is a palindrome string.
# Input type: String
# Return type: Boolean 
print("------------ TODO palindrome identifier ---------------------\n")
# version 1. It works, but it can false negative on Capital letters in the string.
# def palinfind(x):
#     return x == x[::-1]
# I corrected for Upper case letters with .lower(), but found out spaces are a problem in version 2.
# def palinfind(x):
#     return x.lower() == x.lower()[::-1]

# version 3 improves on version 1, by stripping spaces and passing everything as lowercase.


def palinfind(x):
    # added a print line for my own sanity because my IDE choices
    print(''.join(x.split()).lower() == ''.join(x.split()).lower()[::-1])
    return ''.join(x.split()).lower() == ''.join(x.split()).lower()[::-1]
# punctuation is still a potential issue, but I do not know how to solve that with my current knowledge
# plus I have already spent way too much time on this section.


# shows basic True read
palinfind("kayak")

# showsFalse read
palinfind("totallynotapalindrome")

# shows fixed case error
palinfind("rEdDeR")

# shows fixed blank space
palinfind("Never Odd Or Even")
'''
Boolean values can represent the state of a program or a certain condition. For example, you can use variables such as
 game_active, can_edit, and polling_open, which take either a True or False value. When these values are True, certain
  code sections are enabled as the program runs.
'''
# sample input1: bob

# sample output1: true

# sample input2: Jose

# sample output2: false
