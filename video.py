import cv2

Videocapture = cv2.VideoCapture('vid/Wildlife.wmv')
fps = Videocapture.get(cv2.cv.CV_CAP_PROP_FPS)
size = (int(Videocapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(Videocapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
videowriter = cv2.VideoWriter('vid/output.avi', cv2.cv.CV_FOURCC('I','4','2','0'), fps, size)

print Videocapture
print size
print fps

success, frame = Videocapture.read()
print success
if success :
		print "hore"
else :
		print "yaah"
while success:
	if success :
		print "yes"
	else :
		print "ohh"
	videowriter.write(frame)
	success, frame = Videocapture.read()
cv2.destroyAllWindows()