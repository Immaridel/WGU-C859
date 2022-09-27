## PYTHON EXAM REVIEW

# LABS!
# Ch 2-14... all Labs!
# Ch 21-33 just ADDITIONAL LABS, but important practice!
# Use Submit Mode!!!

# Watch your string input and output
# # 1
# myVar = input().strip() # myVar = input().rstrip()
# # 2
# print("some stuff", end=" ") # if you ever override end
# print() # print(end="\n")

## Important Concepts
# Comp 1: Basic syntax and knowledge: operators, data types, etc
# Comp 2: Control Flow
# Comp 3: Modules and Files

# Comp 1: Basic syntax and knowledge: operators, data types, etc
# Data Types
# int
# float
# bool
# str
# list # []
# dict # {key: value, key:value}
# set # {} # all unique values, no order -> no index, can't slice
# tuple # () immutable, Python sees any x,y,z as a tuple (x,y,z) --> return x,y

# operators
# = # assigning a value
# == # comparison, asking if they're equal
# +
# -
# *
# /
# % # modulo, whole number remainder, how many WHOLE THINGS didn't fit?
# // # floor division, last even division
# <
# >
# <=
# >=
# !=
# += # increment
# -= # decrement
# ** # raise to a power... similar to math.pow()
# # keywords used like operators
# in # if _value_ in _someContainer_
# not # flip around Boolean --> if not _value_ in _someContainer_
# and
# or # any one True means whole condition is True... limit OR to 2 conditions
# bool
# list - [1, 2, 3]
# dict - {}
# in - if myNum in myList
# not - if not myNum in myList

# Comp 2
# Basic control structures
# conditional statements: if, if/else, if/elif, if/elif/else...
# loops
# WHILE - if that repeats
# FOR - Iterating over a container (list, dict, tuple, string, etc) or a known count of items
#
# for myCrap in someContainer:
# for char in myString:
# for key in myDict:
# for n in range(0, 10): (do something ten times)
# for i in range(len(myList)):  # this would output the number for the index of that container  # myList[i]

# SLICE - reverse string or list - abbreviated copy of str, list, tuple
# myList = [1, 2, 3, 4, 5]
# revList = myList[::-1]
# print(revList)

# FUNCTIONS
# defining/writing vs calling
# parameters vs outside or "regular" variables
# parameters vs arguments - parameters are for when you're defining - arguments are when you call the function
# a good function has ONE job, modular
# METHODS are functions that "belong" to that type/class of object
# PRINT shows you the value, RETURN will store it to be called later
# def someFunction(x, y):
#    return x + y
# __name__ is a hidden variable
# if __name__ == "__main__":
#   myInput = int(input().strip())
#    num = someFunction(myInput, someOtherNum)
#    print(num)
# See "tasks" in the last section of Chapters 10, 11, 13, and 14 for function writing practice
# https://codingbat.com/python

# BUILT-IN FUNCTION
    # print()
    # input()
    # len()
    # range()
    # min()
    # max()
    # sum()
    # round() # cousins math.ceil(), math.floor()  [round up, round down]
# creating or recasting
    # str()
    # float()
    # float()
    # list()
    # tuple()
    # set()
    # dict()
    # sorted() # DOES return a sroted list (list.sort() doesn't return a value)
        # list.sort(myList)  # returns nothing, just modifies the mutable list
    # reversed() # list.reversed(myList)  # same thing, other direction
        # list.reverse(myList) # returns nothing, just modifies the mutable list
    # open() # IO/filestream:  .read(), .readlines(), .write()
    # help() # help(str)

#help(str.strip)
# print(dir(str))
#for item in dir(str):
#    if not item.startswith("__"):
#        #print("{}()".format(item))
#        print(item)

# STRINGS
# be able to slice like it's second nature... myString[start:stop:step]
# myString = "abcd"
# myRevString = myString[::-1]
# print(myRevString)

# KNOW YOUR WHITESPACE
# # " " # ... and a lot of other Unicode spaces
# Backslashes characters -
#   "\n" - New Line
#   "\r" - Carriage return (back to beginning of same line
#   "\t" - tab
#   "\b" -
#   "\f" -

# STRING METHODS
# Use formatting or f-strings rather than concatenation ( myVar + myVar)
# myString.format()
# myString.strip() # myString.rstrip()  [ all vs right-whitespace ]
# myString.split() # returns a list of smaller strings from a larger string
# myString.join() # probably not using on a variable, but a literal.  Opposite of split.
# ", ".join(listOfStrings)
# myString.replace(subStr, newSubStr) # can use as a remove, since there's no remove string method.  Look and replace for empty string. - myString.replace(subStr, "")
# myString.find(subStr) # return the index where it starts, or -1 if not there
# mystring.count(subStr) # return int of number of occurrences
# is/Boolean methods: isupper(), islower(), isdigit(), isspace(), isalpha(), isalnum()
# isnumeric()
# case changing: upper(), lower(), title()

# LISTS
# be able to slice!

# LIST METHODS (no keys in a list)
# myList.append(item)
# myList.remove(value/item)
# myList.pop(index) # removes last index if none provided
# myList.insert(index, item)
# myList.extend(anotherList)
# myList.count(item) # returns number of occurrences of item
# myList.sort() # no return, modified in place
# myList.reverse() # no return, modifies in place
# myList.clear()
# myList.copy()
# myList.index(item) # return index of item/value, can be less useful if there are more than one occurrence of a value

# DICTIONARIES
# use the key like an index
# myDict[key] # retrives the value for that key, same as myDict.get()
# myDict[key] = value # set a new value as long as the key exists or if you're adding a new key and value
    # compare to myDict.update()
# myDict.keys() # create a container of all the keys in the dictionary
# myDict.values() # same thing, but the values
# myDict.items() # useful in for loop - for key, value in myDict.items()
# del myDict['item'] # removes specific key 'item' and its value
    # IN keyword with a dictionary is looking at KEYS and NOT VALUES
# MODULES
# mostly be concerned with 'math' and 'csv'
# MATH
# import math
    # math.factorial()
    # math.ceil()
    # math.floor()
    # math.pow() # **, not to be confused with math.exp()
    # math.sqrt()
    # math.fabs() # builtin abs()  ## show absolute value
    # math.pi()
    # math.exp()
    # math.e

# different import types
# full import: math.factorial()
# partial import
# from math import factorial
# --> factorial()

# ALIASED IMPORT
# import math as m
# --> m.factorial()
# Syntactical partial import that imports all
# from math import *
# --> factorial(), sqrt()
# DIFFERENT IMPORTS EFFECT HOW YOU REFER/CALL TO THE FUNCTION

# RANDOM
# import random
# random.choice() # returns a random item from a list
# random.randint(x, y) # INCLUDES the stop y
# random.randrange(x, y) # exclude teh stop number y

# CSV
# csv.reader() # reads a .csv or .tsv (delimiter set to comma by default)

# COMP 3
# READING FILES
# plaintext, any extension

# with open("filename.txt", "r") as f:
    # When reading, I grab contents and get out of the open block
    # contents = f.read()  # whole file as one big string
    # contents = f.readlines()  # return a list of strings.
    # Each string is a line in the file.  Ends in a newline like any string.

# get off with/open quickly when reading [LOOK FOR SYNTAX, HE DIDN'T ADD IT]
# Okay, so "getting out of" that clode block (new block) closes the file handle.

# import csv
# with open("mock_data.csv", "r") as f:
    # contents = list(csv.reader(f)) # instead of a list of strings, it's going to look like a list of lists, being the individual cell values.  We wrapped it in a list() for better usage.
    ## contents = list(csv.read(f, delimiter=",")) # or \t or whatever you want the delimiter to be
# print(contents)  # closing this indent gets you out of the file and closes the open file handle

# file example
# ['1', 'Flossie', 'Levey', 'flevey0@jimdo.com']

#========================================================
# import csv
# with open("mock_data.csv", "r") as f:
    # contents = list(csv.reader(f))
# with open("mock_data_new", "w") as f2:
    # for line in contents:
        # if line[3].endswith(".org"):  # SLICE would be "if line[3][-4:] == ".org"  # this is less exact, but you could do it
            # f2.write() # takes a single string argument
            # f2.write(",".join(line)) # this would get the data and print it in a comma-separated format string
            # f2.write(",".join(line) + "\n") # One way to do the above with a line return
            # f2.write("{}\n".format(",".join(line))) #
            # f2.write(f"{','.join(line)}\n") # using f-strings
#========================================================



