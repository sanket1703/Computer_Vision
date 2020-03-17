import cv2,time

video = cv2.VideoCapture(0)
#0 is for in built camera
#if you have any external cams you can use 1
#time delay freezes the code for 3 seconds
face_cascade = cv2.CascadeClassifier("/Users/apple/Desktop/ML/CV/haarcascade_frontalface_default.xml")
#importing the classifier

while True:
    check , frame = video.read()
# it returns check (bool) if the camera is initialized properly 
#frame is the first frame that it had captured when the webcam started 
# because we are in a while loop the Frame is the nothing but many frames combining to form Video
#but here we work with each and every frame and then proccess them and show them simultaneously
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors= 5)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y),(w+x,h+y),(0,255,0),3)
    cv2.imshow("First Capture",frame)
    key = cv2.waitKey(1)
    #if you increase the wait key the capture rate reduces have number of frames captured can be reduced
    if key == ord('q'):
        break 

video.release()
cv2.destroyAllWindows()