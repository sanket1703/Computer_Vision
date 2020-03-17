import cv2,time
import pandas as pd
import datetime

#creating date time object
datetime_object = datetime.datetime.now()

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("/Users/apple/Desktop/ML/CV/haarcascade_frontalface_default.xml")
first_frame = None
status_list = [None,None]
#We initialise the status list to zero zero
#we make sure that the list len remains the same
times = []
#this list hold the time values at which 
df = pd.DataFrame(columns = ["Start","End"])
#Above we have made a data frame using pandas
while True:
    check , frame = video.read()
    status =0 
    print(status_list)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray , (21,21),0)
    # the Gaussian blurr is used to improve accuracy
    if first_frame is None:
        first_frame = gray
        continue
    # The above if condition stores the first img to the first_frame
    #now we calculate difference between first frame and the running frames
    delta_frame = cv2.absdiff(first_frame,gray)
    cv2.imshow("First Capture",delta_frame)
    thresh_delta = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta,None,iterations=0)
    #cv2.imshow("First Capture",thresh_delta)
    #try the above it shows wonders
    # it essentially changes 

    (cnts,heirar) = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #the above code finds Contours and returns a list 
    for contour in cnts:
        if cv2.contourArea(contour)>1000:
            continue
        #Above we are thresholding the motion to 1000 (area)
        status = 1
        #When object is detected status changes to 1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)
    #initially we have 2 none values the we append and get 3 values 
    #the code below takes only latest two values which gives us the list of len 2 always
    status_list = status_list[-2:]
    #The below logic is such where 0 1 means the object was not present but then got detected 
    #and 1 0 means that object was detected but now going 
    #similarly 1 1 means its moving and 0 0 means not there
    if status_list[-1]==0 and status_list[-2] ==1:
        times.append(datetime.datetime.now())
    if status_list[-2]==0 and status_list[-1] ==1:
        times.append(datetime.datetime.now())
    cv2.imshow('frame',frame)
    cv2.imshow('Delta',delta_frame)
    cv2.imshow('gray',gray)
    cv2.imshow('Thresh',thresh_delta)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break 

video.release()

print(times)
print(status_list)
for i in range(0,len(times)-1,2):
    df = df.append({"Start": times[i],"End":times[i+1]},ignore_index = True)
df.to_csv("Time.csv")
cv2.destroyAllWindows()
