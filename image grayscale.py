import cv2

image = cv2.imread("img/img.jpg", cv2.CV_LOAD_IMAGE_GRAYSCALE)
if cv2.imwrite('img/img-grayscale.jpg',image) :
	print "Success"
else :
	print "Failed"

oriimage = cv2.imread("img/img.jpg")
newx,newy = oriimage.shape[1]/6,oriimage.shape[0]/6 #new size (w,h)
newimage = cv2.resize(oriimage,(newx,newy))
cv2.imshow("original image",oriimage)
cv2.imshow("resize image",newimage)
cv2.imwrite('img/image-resize.jpg',newimage)
cv2.waitKey(0)
cv2.destroyAllWindows()