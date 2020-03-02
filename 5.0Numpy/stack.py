import cv2
import numpy

# load image - 0 for 2D
img = cv2.imread("smallgray.png",0) 
print(img)

print("**************************")

# stacking image
img_s = numpy.hstack((img,img,img))
print(img_s)