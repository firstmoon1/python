

import cv2
from matplotlib import pyplot as plt
import numpy as np

def nothing():
    pass

cv2.namedWindow("tracker",cv2.WINDOW_NORMAL)

#bu ekrana cıkartıyor cv2.imshow() ile aynı işi görüyor 
#cv2.namedWindow("cam",cv2.WINDOW_NORMAL)
#cv2.namedWindow("mask",cv2.WINDOW_NORMAL)
#cv2.namedWindow("mask1",cv2.WINDOW_NORMAL)

cv2.createTrackbar("Low-H","tracker" ,0,255,nothing )
cv2.createTrackbar("Low-S","tracker" ,0,255,nothing )
cv2.createTrackbar("Low-V","tracker" ,0,255,nothing )
cv2.createTrackbar("UP-H","tracker" ,0,255,nothing )
cv2.createTrackbar("UP-S","tracker" ,0,255,nothing )
cv2.createTrackbar("UP-V","tracker" ,0,255,nothing )

cam=cv2.VideoCapture(0)


while True:
    
    ret,frame=cam.read()
    frame=cv2.resize(frame,(250,250))
    blurred_frame=cv2.GaussianBlur(frame,(5,5),0)
    if not ret:
        print("no camera connection")
        break
    
    hsv = cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)
    
    l_h=cv2.getTrackbarPos("Low-H","tracker")
    l_s=cv2.getTrackbarPos("Low-S","tracker")
    l_v=cv2.getTrackbarPos("Low-V","tracker")
    u_h=cv2.getTrackbarPos("UP-H","tracker")
    u_s=cv2.getTrackbarPos("UP-S","tracker")
    u_v=cv2.getTrackbarPos("UP-V","tracker")
       
    color_low = np.array( [ l_h , l_s , l_v ] ) 
    color_high = np.array( [ u_h , u_s , u_v ] )
    mask=cv2.inRange(hsv,color_low,color_high)
    mask1=cv2.bitwise_and(frame,frame,mask=mask)
    
    kernel=np.ones((5,5),np.uint8)
    
    erosion=cv2.erode(mask,kernel)
    dilation=cv2.dilate(mask,kernel)
    #morpholog=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) # MORPH_GRADIENT : border ciziyor
    morpholog=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) # MORPH_OPEN : iç dıs komple ciziyor
    md=cv2.morphologyEx(dilation,cv2.MORPH_OPEN,kernel) # MORPH_OPEN : iç dıs komple ciziyor
    
    cv2.imshow("cam",frame)
    cv2.imshow("color_range",mask)
    cv2.imshow("bitwise",mask1)
    cv2.imshow("erosion",erosion)
    cv2.imshow("dilation",dilation)
    cv2.imshow("morpholog",morpholog)
    cv2.imshow("morp+dilation",md)
    
    if cv2.waitKey(1) & 0xff==27:
        break

cam.release()
cv2.destroyAllWindows()



