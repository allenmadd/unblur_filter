# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:41:04 2018

@author: madel
"""

def filter_photo(photo):
        import numpy as np
        import cv2
    #convert
#        im_frame = Image.open(photo)
 #       np_frame = np.array(im_frame.getdata())
#############
        ############################   
        #read the photo in as black and white
        img = cv2.imread(photo,0)
       # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #img= np.invert(img)        
        kernel = np.ones((5,5),np.uint8)       
        grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
        alpha=30
        sharpened = img+alpha*(img - grad)
        
        cv2.imshow("name", sharpened)
#
        
        



photo = "C:/Users/madel/OneDrive/Pictures/image_practice.PNG"
filter_photo(photo)