import cv2
import numpy as np
import time,sys
import math
def red():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        blurred = cv2.GaussianBlur(frame,(5,5),0,5)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        low_red=np.array([161,155,84])
        high_red=np.array([179,255,255])

        red_mask=cv2.inRange(hsv,low_red,high_red)
        red = cv2.bitwise_and(blurred,blurred, mask=red_mask)

        contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        screenCenterX = cap.get(3)//2
        screenCenterY = cap.get(4)//2
        font = cv2.FONT_HERSHEY_SIMPLEX
        

        for c in contours:
            area = cv2.contourArea(c)
            
            if area > 200:

                c = max(contours, key = cv2.contourArea)       # En büyük kırmızı alanı buluyor
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                M = cv2.moments(c)
                cx = int(M["m10"] / M["m00"]) # objenin merkezini verir, cx,cy budur x ve y kordinatlarına göre
                cy = int(M["m01"] / M["m00"])

                distancePixel = math.sqrt((screenCenterX-cx)**2+(screenCenterY-cy)**2)
                if not (screenCenterX - cx) == 0:
                    degree = 90 - math.degrees(math.atan2((screenCenterY - cy),(cx - screenCenterX)))  
                else:
                    degree = 0


                cv2.putText(frame, f"x: {cx}",(10,25),font, 0.6, (0,0,255),2)
                cv2.putText(frame, f"y: {cy}",(10,50),font, 0.6, (0,0,255),2)
                cv2.putText(frame, f"Distance: {int(distancePixel)}",(10,75),font, 0.6, (0,0,255),2)
                cv2.putText(frame, f"Degree: {round(90-degree,1)}",(10,100),font, 0.6, (0,0,255),2)
                cv2.circle(frame, (cx, cy), 4, (255, 255, 255), -1)
                cv2.line(frame,(int(cx),int(cy)),(int(screenCenterX),int(screenCenterY)),(235, 52, 55),3)  # Ekranın ortasından kırmızı alanın merkezine çizgi çekiyor 
                cv2.circle(frame,(int(screenCenterX),int(screenCenterY)),1,(255,255,255),-1)

        #cv2.imshow('Red Detection',blurred)
        cv2.imshow('Red Detection',frame)
        cv2.imshow("inrange",red_mask)
        if cv2.waitKey(1)==ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
red()