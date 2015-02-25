#!/usr/bin/env python
from sys import argv

nama, banyaknya = argv

x = int(banyaknya)
for i in range(1,x+1):
	if i % 2 == 0 :
		print i

# just try it out