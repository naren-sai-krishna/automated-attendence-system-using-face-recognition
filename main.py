# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:02:47 2018

@author: naren
"""
import FaceDetection as fd



print('Enter 1: To add a new face to the database')
print('Enter 2: To Make Features')
print('Enter 3: To Train on the dataset')
print('Enter 4: For Face Detection Demo')
print('Enter 5: For Face Recognition Demo')
print('Enter your Choice:',end="")
choice = int(input().strip())
if choice==4:
        fd.detect_demo()

