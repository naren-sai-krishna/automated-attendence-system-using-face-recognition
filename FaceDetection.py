# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:50:37 2018

@author: naren
"""


import cv2                  



def detect_demo():
    face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
    eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')
    
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, img = cap.read()
        if ret:
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                   
            
            
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)             
            for (x, y, w, h) in faces:                                      
                gray_face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))  
                eyes = eye_cascade.detectMultiScale(gray_face)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255,255,255), 2)
                    
            cv2.imshow('Face Detection Using Haar-Cascades ', img)         
            if cv2.waitKey(1) & 0xFF == ord('q'):                           
                break

    cv2.destroyAllWindows()
