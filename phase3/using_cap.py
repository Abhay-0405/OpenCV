import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read() #ret->True,false   frame->image 
    if not ret:
        print("could not read frame")
        break
    cv2.imshow("webcam feed ",frame)
    if(cv2.waitKey(1) & 0xff==1)==ord('q'): # 113==113
        print("Quitting....")
        break
