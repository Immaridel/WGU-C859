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
unique_list = []

with open(input(), 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        for word in row:
            if word not in unique_list:
                unique_list.append(word)
        for unique_word in unique_list:
            count = row.count(unique_word)
            print(unique_word, count)