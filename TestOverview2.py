# Exam Review 2022 Aug 27

# LABS
# Ch 2-14... all Labs!
# Ch 21-33 just ADDITIONAL LABS, but important practice!
# Use Submit Mode!!!

# Watch your string input and output
# # 1
# myVar = input().strip() # myVar = input().rstrip()
# # 2
# print("some stuff", end=" ") # if you ever override end
# print() # print(end="\n")

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

# Comp 2
# the HOW stuff... control flow structures
# IF statements... if, if/else, if/elif, if/elif/else, etc
# LOOPS
# WHILE - an IF that repeats
# FOR - looping over a container, or a known number of times (range)
# for _value_ in _container_:
# for item in myList:
# for n in range(0, 4): # [0, 1, 2, 3]
# for i in range(len(myList)): # myList[i]
# for key in myDictionary: # x, y = [1, 2]... for k, v in myDictionary.items()

# FUNCTIONS
# defining/writing vs calling
# parameters vs "outside" or "regular" variables
# parameters vs arguments
# a function has ONE particular job, modular
# return vs print() or "output" # do whichever the question
# methods are functions that belong to a particular class or data type

# def someFunction(x, y):
#     return x + y
#
# if __name__ == "__main__":
#     myInput = int(input())
#     num = someFunction(myInput, someOtherNum)
#     print(num)

# See "tasks" in the last section of Ch 10, 11, 13, 14 for function writing practice
# CodingBat also has good function-based Python questions:
# https://codingbat.com/python

# BUILT-IN FUNCTIONS
# print()
# input()
# len()
# sum()
# min()
# max()
# range()
# list()
# dict()
# tuple()
# set()
# sorted() # compare to list.sort()
# reversed() # compare to list.reverse()
# round() # regular round() is a built-in, cousins math.ceil(), math.floor()
# open() # IO/filestream: .read(), .readlines(), .write()
#
# help() # help(str), help(list)
# dir()
# # help(str)
# # help(str.capitalize)
#
# # dir() # returns a LIST of attributes
# # print(dir(dict))
#
# for item in dir(str):
#     if not item.startswith("_"):
#         print("{}()".format(item))

# STRINGS
# be able to slice like it's 2nd nature: myString[start:stop:step]
# myString = "abc"
# myRevString = myString[::-1]
# print(myRevString)

# KNOW YOUR WHITESPACE
# " " # ... and a lot of other Unicode spaces
# "\n"
# "\r"
# "\t"
# "\f"

# STRING METHODS
# myString.format() # or the similar f string
# myString.strip()
# myString.split()
# ",".join(someListOfStrings)
# myString.replace(subStr, newSubStr) # use it to remove myString.replace(subStr, "")
# myString.find(subStr) # return index, or -1
# myString.count(subStr) # return int of number of occurences
# case: title(), upper(), lower(), capitalize()
# is/Boolean methods: isupper(), islower(), isdigit(), isspace()


### sidequest... question on using .join() when you don't have a list of strings
### ... well, you'd need a new list with the values of ints or float recast as strings
### I would do that with a plain old for loop and a new list,
### but you could also do it with a comprehension, which is just a shorter version of the same

### jdList = ["1", "2", "3"]
### print("|".join(jdList))
### jdList = [1, 2, 3]
### if you really like comprehension: expression for item in container ** opt if **
### print("|".join([str(x) for x in jdList]))


# LISTS
# again, be able to slice

# LIST METHODS
# +
# myList.append(item)
# myList.insert(i, item)
# myList.extend(anotherList)
# # -
# myList.pop() # pop by index
# myList.remove(item) # remove by value
# # other
# myList.count(item) # don't confuse with len()
# myList.sort()
# myList.reverse()
# # not as important
# myList.index() # be careful, could be in there more than once
# myList.copy()
# myList.clear()

# DICT
# use the key like an index
# myDict[key] # retrieve the value for that key, so like get()
# myDict[key] = value # assign (new) value for that key, so like update()
# myDict.items() # for k, v in myDict.items()
# myDict.keys()
# myDict.values()

# SETS
# mySet.add()
# mySet.remove(item) # by value
# mySet.pop() # removes a random item

# MODULES
# math and csv

# MATH MODULE
# import math
# math.factorial(x)
# math.ceil(x.yz)
# math.floor(x.yz)
# math.pow(x, y) # similar to **, not to be confused math.exp()
# math.sqrt(x)
# math.fabs() # abs()
# math.e
# math.pi

# different import types
# full import: math.factorial()
# from math import factorial
# --> factorial()
# from math import factorial, floor
# --> floor()
# --> factorial()
# from math import *
# still factorial(), sqrt()
# aliased imports
# import math as m --> m.factorial()

# # OPENING FILES
#  good practice in Ch 14 Task 4, 7, 8

with open("test.txt", "r") as f:
    contents = f.readlines()  # a list of line by line strings
print(contents)

for line in contents:
    line = line.strip()
    print(line)  # print(line, end="\n")

import csv  # for csv.reader()

with open("mock_data.csv", "r") as f:
    content = list(csv.reader(f))  # csv.reader(f, delimiter="\t")
print(content)

with open("output_data2.csv", "w") as f2:
    for line in contents:
        if line[3].endswith(".org")  # if line[3][-4:]:
            f2.write(",".join(line) + "\n")  # write() takes a single string as its arg
            # f2.write("{}\n".format(",".join(line)))
