# Comments are lines in a program that the program ignores when it executes. They allow you to add notes about how the
# program works to help you and other developers understand the code.

# This is a single line comment in Python

"""
Use comments to explain:
    • The role of important variables when you introduce them
    • How you’ve approached a problem after considering multiple approaches
    • What your functions do
    • What classes are used for in the program

    Writing comments will remind you what your code does when you return to it later. Comments also help teams of
    programmers collaborate effectively.
"""

'''
    This is a multi-line 
    comment in Python
'''

# Print to console
# from array import array
# from operator import le


print("This is my first print statement")

'''
In statically typed languages, you must declare the kind of data a variable represents when you define it. Python is a
dynamically typed language, meaning you don’t have to declare the kind of data a variable will represent. In Python, 
the interpreter examines the data associated with the vari-able throughout the life of the program and manages type 
issues for you.
'''

'''
In Python, a variable is a name attached to a piece of data. You first define a variable, then use that name when you
refer to that piece of data.
'''

# Initialize two string variables
first_name = "Andrew"
last_name = "Korenak"
my_age = int(27)

'''
A string is a value made up of text and is one of the simplest data types in any language. Much of the information
that’s passed within and between programs is strings.
Strings are treated as a collection of characters, so the string "123" is different from the numerical value 123. 
A substring is part of a string.
You can perform many actions with strings:
• Joining strings together, known as concatenation
• Inserting the value of a variable into a string, known as interpolation• Changing a string’s case
• Stripping extra whitespace from a string• Searching for a substring within a string
• Replacing some characters in a string
In Python, strings are enclosed using single or double quotes.
'''
'''
# Concatenate strings
print("Hi, my name is " + first_name + " " + last_name)

# use % operator to concatenate
print("Hi, my name is %s %s" % (first_name, last_name))

# using join() to concatenate
print("Hi, my name is " + " ".join([first_name, last_name]))

# using format() to concatenate
print("Hi, my name is {} {}".format(first_name, last_name))
'''
# TODO: Try introducing yourself and add your age as well. On top of first_name & last_name variable add another
# variable called my_age and set it to a number.
# Then try concatenating it using the above four strategies.

print('--------- TODO introduce yourself 4 different concatenate methods -----------------\n')
print("Hello, my name is " + first_name + " " + last_name + ", " + "and I am " + str(my_age) + " " + "years old.\n"
      + "Hello, my name is %s %s and I am %s years old.\n" % (first_name, last_name, str(my_age))
      + "Hola, me llamo " + " ".join([first_name, last_name]) + " Tengo " + str(my_age) + " Años.\n"
      + "Ahoy mateys, me name be {} {} n' I be {} years ole by the reckonin' of the sea.\n".format(first_name,
                                                                                                   last_name,
                                                                                                   str(my_age))
      )  # put them all in one print for fun. my_age must be called as a str since you can not concat it as an int.

'''
Integers and floats are the two main kinds of numerical data types. An integer, or int, is a number with no decimal 
part. A float is a number with a decimal part.
'''

'''
You can perform all basic arithmetic operations with numerical data and do higher-order operations, such as working with
exponents, finding absolute values, and work-ing with trigonometric functions.
Python allows you to represent complex numbers (numbers with real and imaginary parts) and work with fractions.
For computation-intensive work, third-party libraries, such as NumPy, SciPy, and pandas, can make your work easier.
Many dedicated visualization libraries are available as well, such as Matplotlib, Bokeh, Pygal, and Plotly.
'''

# Initialize variables of different data types
simple_string = "this is a simple string"
num = 1234
simple_decimal = 12.4
simple_boolean = True  # A Boolean value represents either T or F. In Python, these values are True and False.
short_array = [1, 2, 3, 4]

'''
You can use the elif, or else if, statement to make your program respond to multiple conditions. This code structure
means “if one condition applies, do this; else if a different condition applies, do something different.”
You can chain together as many of these specific conditions as you need.
An else block runs a particular block of code when all other conditions don’t apply. An else block must always be the
last block in an if-elif-else chain.
'''
# Branching Logic
if simple_decimal < 5.0:
    print("Small decimal")
elif simple_decimal < 9.0:
    print("Mid size decimal")
else:
    print("Big decimal")

'''
A sequence is a data structure that stores a collection of items in a specific order. In some languages, a sequence can 
only contain items of one type; in other languages, including Python, a sequence can have items of different types.
'''
print('--------- printing array from the first index -----------------\n')

# Control flow - for loops
for num in short_array:
    print(num)

print("------- printing array from the last index -----------\n")

'''
A loop is a block of code that runs multiple times. Use loops when you need to repeat actions more than once, depending
on certain criteria. The two loop types are the for loop and the while loop.
'''
# loop through an array from the last index
for index in range(len(short_array) - 1, -1, -1):
    print(short_array[index])

print("----- Print Odd Numbers ---------------------\n")

'''
A for loop repeats as many times as you specify or once for each item in a sequence. For example, you can write a for
 loop that runs 100 times to repeat an action 100 times. You can also write a for loop that runs once for each item in
  a collection of items.
'''
# for loops print odd numbers from 1 to 10;
for num in range(10):
    if num % 2 == 1:
        print(num)

# or ...

for num in range(10):
    if num % 2 != 0:
        print(num)

print("----------- While Loop -------------------\n")

'''
A while loop runs as long as a certain condition is true. Say you have a game loop that runs as long as a game_active
variable is set to True. You can then put multiple situations inside the loop that cause game_active to become False 
and end the game. You can also use a while loop to process items in a collection that might have new items added to it 
as the loop is running. As long as items are in the collection, you can keep working with it. When the collection is 
empty, the loop stops running.
'''
# While Loop
while_loop_index = 1
while while_loop_index < 10:
    print(while_loop_index)
    while_loop_index += 1

'''
A nested loop is a loop inside another loop. Say you need a loop that examines every pixel in an image. You could write
a loop that looks at each pixel in a row and, inside that loop, add a second loop that looks at every pixel in the
current column for that row.
'''
# TODO: write a for loop to ONLY print even numbers
print("----------- TODO For Loop Even -------------------\n")
# For loop even
for num in range(11):
    if num % 2 == 0:
        print(num)

# TODO: Declare an Array with mixed data types. i.e. string, number, boolean, etc.
# Iterate through this list using for loop and see the output. 
print("----------- TODO Mixed Data Types Array -------------------\n")
mixed_array = [True, 1, "texthere", 30.5]
# Iterate mixed_array overly complex version
for x in mixed_array:
    print(x)

# TODO: Print the data type for each array item.
print("----------- TODO Print Types overly complex solution -------------------\n")
for x in mixed_array:
    if type(x) == int:
        print("Integer")
    if type(x) == float:
        print("Float")
    if type(x) == bool:
        print("Boolean")
    if type(x) == str:
        print("String")
    else:
        continue
print("----------- TODO Print Types Simple Solution -------------------\n")
for x in mixed_array:
    print(type(x))

# TODO: Reverse a String: input = hello, output = olleh
print("----------- TODO hello to olleh -------------------\n")
print("Hello"[::-1])

# TODO: Reverse a number: input = 1234, output = 4321
print("----------- TODO Reverse a number dummy edition -------------------\n")
# you can not normally do this with an INT. Instead (str(1234)) or ("1234") would work.
print(str(1234)[::-1])
# but the results are technically not an int anymore, but instead a string. This could be converted back like below.
output = (str(1234)[::-1])
output = int(output)
print(output, type(output))

'''
Sequences are important when you need to store items in a specific order. For example, a list of website users might be
 ordered according to when each user registered.
With a sequence, you can do the following:
• Add and remove items
• Work with individual items or groups of items
• Determine whether a value is in the sequence
• Look for duplicate or unique items
• Loop through the sequence and do something with each item
• Work with items that match certain conditions.
In Python, the main sequence type is the list. Lists are mutable, meaning you can modify them after creating them. 
Tuples are immutable sequences, meaning they can’t be changed after they’re defined. Strings are a special type of 
sequence: each element in the sequence is a character.
'''
print("------- List --------------")
my_list = ["apple", "banana", "cherry", "mango", "pineapple", "watermelon"]

# print the first item of a list
print(my_list[0])

# print the last item of a list
print(my_list[-1])

# print a range of items 
print(my_list[0:3])

# add item to the end of the list
my_list.append("Cupcake")
print(my_list)

# add item to a specified index
my_list.insert(1, "Chips")
print(my_list)

# remove an item off of a list
my_list.remove("Cupcake")
print(my_list)

# remove an item off of a list by index #
my_list.pop(-1)  # last index removal
print(my_list)

# size of a list
print(len(my_list))

print("--------- Iterate through my_list---------------")
# iterate through a list using for loop
for fruit in my_list:
    print(fruit)

# update an item in the list by index 
my_list[1] = "avocado"

# Iterate through a list with access to index and item in the list using enumerate
for index, fruit in enumerate(my_list):
    print("index: %s =  %s " % (index, fruit))

# TODO: Using a for loop update every item in the my_list list into dessert items
# dessert = ["apple cake", "banana cake", "donut", "fudge", "ice cream", "jilapi"]
print("-------------------- TODO update list to junkfoods ---------------------------------\n")
for x in my_list:
    my_list[0] = 'apple cake'
    my_list[1] = 'banana cake'
    my_list[2] = 'donut'
    my_list[3] = 'fudge'
    my_list[4] = 'ice cream'
    my_list[5] = 'jilapi'
print(my_list)

print("-------------------- Dictionary ---------------------------------\n")
# initialize dictionary
# Empty dictionary initialization
empty_dict = {}
print("Empty dictionary: %s" % empty_dict)

# Initialize dictionary with some key/pair values
country_capital_dict = {"America": "Washington DC", "Bangladesh": "Dhaka", "Canada": "Ottawa", "Denmark": "Copenhagen",
                        "Ethopia": "Addis Ababa"}
print("\nDictionary with initialized values:\n%s" % country_capital_dict)

# adding items to an existing dictionary
country_capital_dict["France"] = "Paris"
country_capital_dict["Germany"] = "Berlin"
print("\nDictionary with new item added:\n%s" % country_capital_dict)

# Removing items from an existing dictionary 
# NOTE: dict.pop() is preferable method of removing an item from a dictionary. Also, del can delete an entire dictionary
# when you don't specify key to delete.
#
del country_capital_dict["Germany"]
country_capital_dict.pop("France")
print("\nDictionary after deletion:\n%s" % country_capital_dict)

# updating values in a dictionary
country_capital_dict["Bangladesh"] = "Sylhet"
print("\nDictionary after update:\n%s" % country_capital_dict)

# Accessing values in a dictionary
print("\nCapital of Canada is: %s" % country_capital_dict.get("Canada"))

print("Capital of Denmark is: %s" % country_capital_dict["Denmark"])

print("\n----------------------- Iterate through a Dictionary------------------------------\n")
# Using for-loops to iterate through a dictionary:
for key, value in country_capital_dict.items():
    print("Country: %s, Capital City: %s" % (key, value))

# TODO: Create 5 lists of real life items and create 5 dictionaries. For example,
# for list, I would create a list for list of chores I need to do on weekends. i.e chores = ['laundry', 'pick-up mail',
# 'clean the apt']
# for dictionary, I would have friends to phone number. friends = {'jose': '718-233-6464', 'ali': '646-232-2323'}
print("\n----------------------- TODO 5 Lists and 5 Dicts------------------------------\n")
# randomlists.com for items at random to make a list out of
list1_rand_movies = ("The House", "Batman", "Sinkhole", "Resident Evil", "Meander")
list2_rand_team = ("Indianapolis Colts", "Buffalo Bills", "Atlanta Falcons", "Seattle Seahawks", "Denver Broncos")
list3_rand_artists = ("Christina Aguilera", "Billie Eilish", "Amy Stroup", "Fenton Robinson", "Bruno Mars")
list4_rand_adjectives = ("average", "creepy", "closed", "panicky", "paltry")
list5_rand_color = ("Dark Green", "Steel Blue", "Dark Sea Green", "Lemon Chiffon", "Dark Cyan")

dict1_name_zip = {"Shyanne": "98144", "Julie": "37128", "Cecilia": "45520", "Lyric": "20175", "Keith": "10002"}
dict2_f_food = {"f0": "artichokes", "f1": "date sugar", "f3": "honeydew mellon", "f4": "grouper", "f5": "pistachio"}
dict3_babyname = {"August": "Ok name", "Alfonso": "Crap", "Marina": "Crap", "Cael": "Hell No",
                  "Lisa": "Normal Sounding"}
# Yes, I understand that some states have matching city names, therefore this would not work as a key for a larger dict
dict4_location = {"Scottsdale": "AZ", "Stockton": "CA", "Cincinnati": "OH", "Columbus": "GA", "Pittsburgh": "PA"}
dict5_words = {"fret": 4, "rabble": 6, "credulous": 9, "Whimsical": 9, "imperative": 10}

print(list1_rand_movies)
print(list2_rand_team)
print(list3_rand_artists)
print(list4_rand_adjectives)
print(list5_rand_color)
print(dict1_name_zip)
print(dict2_f_food)
print(dict3_babyname)
print(dict4_location)
print(dict5_words)
