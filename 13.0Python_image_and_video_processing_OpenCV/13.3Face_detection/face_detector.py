import cv2

# read the cascade.
face_cascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")

# load the img
img = cv2.imread("Files/photo.jpg")
# img = cv2.imread("Files/news.jpg")

# make image gray scale to increase accuracy
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect-multi-scale method -> This searches for cascade classifier in XML and return face cordinates
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)
# cv2.imshow("Gray",gray_img)

# Now we need to draw the rectangle on the face using "print(faces)" output
"""
    (x,y)
        *------
        |     |
        ------*
              (x+w,y+h)
"""
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3) # '0,255,0' is BGR and 3 is height

resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Gray",resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()