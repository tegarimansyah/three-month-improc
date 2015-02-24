import cv2

image = cv2.imread('img/img.jpg')
if cv2.imwrite('img/img.png',image) :
	print "Success"
else :
	print "Failed"
