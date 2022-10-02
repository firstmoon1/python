

import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils


cam=cv2.VideoCapture(0)


while True:
    
    ret,frame=cam.read()
    frame=cv2.resize(frame,(300,300))
    if not ret:
        print("no camera connection")
        break
    blur = cv2.GaussianBlur(frame, (7, 7),1)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #ret, thresh = cv2.threshold(blur, 200, 255,cv2.THRESH_BINARY_INV)
    color_low = np.array( [ 160 , 200 , 52 ] ) 
    color_high = np.array( [ 180 , 255 , 255 ] ) 
    mask=cv2.inRange(hsv,color_low,color_high) 
    
    kernel=np.ones((5,5),np.uint8)
    dilation=cv2.dilate(mask,kernel,iterations=1) # iteration 'ı arttırınca kalem'in en boy görüntüsü artıyor  md imshow da 1 den 10 'a cekince gördüm
    morpholog=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) # MORPH_OPEN : iç dıs komple ciziyor
    md=cv2.morphologyEx(dilation,cv2.MORPH_OPEN,kernel) # MORPH_OPEN : iç dıs komple ciziyor
    
    contours,_ = cv2.findContours( mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    
    
    # secme yapıyor en büyük red colour nesnesini alır, referans ise hacim.
    if contours is not None: 
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        # draw the book contour (in green)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
   
    # bu ise komple bütün red colour detection yapar
    """
    for i in contours:
        #area=cv2.contourArea(i)
        #if area>100:
        M = cv2.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #cv2.drawContours(frame, [i], -1, (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            #cv2.putText(frame, "center", (cx - 20, cy - 20) , cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.rectangle(frame,(cx-25,cy-25),(cx+25,cy+25),(0,255,0),4)
            #print(f"x: {cx} y: {cy}")  
    """    
    
    
    
    #cv2.circle(frame,()),5,(0,255,0),2)
    #cv2.rectangle(frame,(100,100),(300,300),(0,0,255),5)
    
    cv2.imshow("cam",frame)
    cv2.imshow("color_picker",mask)
    cv2.imshow("morpholog-dilation",md)
    if cv2.waitKey(1) & 0xff==27:
        break

cam.release()
cv2.destroyAllWindows()



