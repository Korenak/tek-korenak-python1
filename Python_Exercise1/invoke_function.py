from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the 
function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a 
function and call it when you need it. When you need to change how the action is carried out, you can change the code in
 the function, and the improvement is applied everywhere.
'''
print("------------ TODO invoke functions from initialize_functions.py ---------------------\n\n")
print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

# TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

# Had to add a print line to some functions on initialize_functions.py to get them to display when run in pycharm

zero_arg_function()

introduction("Andrew", "Korenak")

introduction_with_default_args("Randomname",)

introduction_with_mix_of_default_args("Who", "Dat?")

product_of_two_num(31, 5)

add_all_nums(1, 3, 6, 7, 34, 78)

double(20)
# fib ommitted from print due to recursion
fib(42)

subtract(50, 39)
