#!/usr/bin/env python

def sorting(listinput, start, end):
	pivot = listinput[end]
	bottom = start
	top = end
	read = 1

	while read :
		while bottom != top:
			if listinput[bottom] > pivot :
				listinput[top] = listinput[bottom]
				break
			bottom += 1

		while top != bottom:
			top -= 1
			if listinput[top] < pivot :
				listinput[bottom] = listinput[top]
				break

		if top == bottom :
			read = 0
	
	listinput[top] = pivot
	return top

def quicksort(listinput, start, end) :
	if start < end :
		center = sorting(listinput, start, end)
		quicksort(listinput, center, end)
		quicksort(listinput, start, center-1)
	else :
		return 1

# Make an Array
number = int(raw_input())
listinput = [i for i in range(1,number+1)]

# Asking for input
for i in range(0,number) :
	print "%d input : " % (i+1),
	listinput[i] = int(raw_input())

quicksort(listinput,0,len(listinput)-1)

print listinput