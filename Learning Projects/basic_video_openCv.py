import cv2,time

video = cv2.VideoCapture(0)
#0 is for in built camera
#if you have any external cams you can use 1
#time delay freezes the code for 3 seconds
a=0
while True:
    a+=1
    check , frame = video.read()
    
# it returns check (bool) if the camera is initialized properly 
#frame is the first fram that it had captured when the webcam started
    cv2.imshow("First Capture",frame)
    key = cv2.waitKey(1)
    #if you increase the wait key the capture rate reduces have number of frames captured can be reduced
    if key == ord('q'):
        break 

video.release()
print(a)
cv2.destroyAllWindows()