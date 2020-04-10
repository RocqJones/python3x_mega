import cv2

# 'imread' image read. scale 0: black and white and scale1: normal
img = cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img) # it's a 2-demensional arrat
print(img.shape) # know no of pixels in horizontal and vertical
print(img.ndim) # to check img dimension

# resize image
# resized_img = cv2.resize(img,(1000,500))
resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) # devide tuple resolution on ln 8 into 2
cv2.imshow("Galaxy", resized_img) # create a window
cv2.imwrite("galaxy_resized.jpg", resized_img) # write the resized img into a new file
cv2.waitKey(0) # set timmer in milliseconds on how long the window will display
cv2.destroyAllWindows()