import cv2
import pprint

face_cascade = cv2.CascadeClassifier("/Users/apple/Desktop/ML/CV/haarcascade_frontalface_default.xml")
print(face_cascade)
img1 = cv2.imread("/Users/apple/Desktop/ML/CV/Learning Projects/Data/adrian.jpg",0)  
img = cv2.imread("/Users/apple/Desktop/ML/CV/Learning Projects/Data/adrian.jpg",1)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors= 5)
print(type(faces))
print(faces)
#faces return the coordinates of the face x, y ,w ,h in this form 

#(0,0) ---->  increases
#  |
#  |
#  V
#increases
# this the coordinate system followed by openCV
# also the coordinates given in the faces are upper left corner coordinates
for x,y,w,h in faces:
    y = 0
    img = cv2.rectangle(img, (x,y),(w+x,h+y),(0,255,0),3)
    # it iterates through only once 
    # using for loop in just one iteration we assign values of xywh from faces
cv2.imshow("final",img)
cv2.waitKey(0)
cv2.destroyAllWindows()