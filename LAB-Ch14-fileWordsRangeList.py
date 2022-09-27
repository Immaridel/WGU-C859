""" LAB 14.8
input1.txt
ammoniated
millennium
"""

in1 = input()
in2 = input()
in3 = input()

with open(in1, 'r') as f:
    listed = f.readlines()

for i in listed:
    i = i.strip()
    #either of these work, top is just simpler.
    #if in2 <= i <= in3:
    if i >= in2 and i <= in3:
        print(i)
