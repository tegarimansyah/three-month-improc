import cv2
import numpy
import os

# Random character for n byte. 1 Byte = 1 Character
# n = a*b*c
# The randowmByteArray contain random character inside or outside ascii
randomByteArray = bytearray(os.urandom(60)) 

# The flatNumpyArray make randomByteArray carachter become integer (0-255) 
# and make a single array contain n number
flatNumpyArray = numpy.array(randomByteArray)

# Convert the array to make a a*b pixel
# a is vertical array and b is horizontal array
# c is up to you. 1 is grayscale, 3 is BGR and 4 is CMYK
bgrimage = flatNumpyArray.reshape(5, 4 , 3) # (a, b, c)

if cv2.imwrite('img/randomcolor.png',bgrimage) :
	print "Success"
else :
	print "Failed"

print randomByteArray
print flatNumpyArray
print bgrimage
