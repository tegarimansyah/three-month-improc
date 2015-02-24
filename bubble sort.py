#!/usr/bin/env python

# from sys import argv
# name, number = argv

# Make an Array
number = int(raw_input())
listinput = [i for i in range(1,number+1)]

# Asking for input
for i in range(0,number) :
	print "%d input : " % (i+1),
	listinput[i] = int(raw_input())

# Bubble Sort
for i in range(0,len(listinput)) :
	for j in range(i+1,len(listinput)) :
		if listinput[i] > listinput[j] :
			tmp = listinput[j]
			listinput[j] = listinput[i]
			listinput[i] = tmp

print listinput
