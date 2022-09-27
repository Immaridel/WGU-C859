"""
Write a program that first reads in the name of an input file and then reads the file using the
csv.reader() method. The file contains a list of words separated by commas. Your program should
output the words and their frequencies (the number of times each word appears in the file)
without any duplicates.

The contents of the input1.csv are: hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy

Ex: If the input is:

input1.csv

the output is:

hello 1
cat 2
man 2
hey 2
dog 2
boy 2
Hello 1
woman 1
Cat 1
"""

import csv

with open(input(), 'r') as f:
    unique_words = []
    csv = csv.reader(f)
    for row in csv:
        for word in row:
            if word not in unique_words:
                unique_words.append(word)
        for unique in unique_words:
            count = row.count(unique)
            print(unique, count)
