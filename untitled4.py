# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 22:56:52 2018

@author: madel
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 16:05:36 2018

@author: madel
"""


###
### think i got it but there are some things to do. 
### I need to make it print the way cv2 does it.
### that probably isnt so hard i can load the file as cv2 does and then
### just printit out. or i can use numpy to convert it intermediately
### then i need to tinker with gaussian settings
###
def filter_photo_3(photo):
    from scipy import misc
    from scipy.ndimage import gaussian_filter
    from scipy.ndimage import gaussian_filter1d
    import numpy as np
    from PIL import Image, ImageTk, ImageFilter
    import matplotlib.pyplot as plt
    import cv2       
    
    #photo = "C:/Users/madel/OneDrive/Pictures/image_practice.PNG"
    face=Image.open(photo)
  #  face=np.fromfile(photo, dtype=np.uint8)
    #face=misc.face(gray=True).astype(float)
    
    
    #blurred_f=gaussian_filter(face,1, order=0, output=None, truncate=1.1)
    blurred_f= gaussian_filter1d(face,10)
    
    blur2 = gaussian_filter1d(face,1)
    
    #filter_blurred_f = gaussian_filter(blurred_f, 1, order=0, output=None)
    #alpha=1000000000000000000
    alpha=2
    beta=20
  #  sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)
    
    sharpened = face+alpha*(face - blurred_f)
    
    #sharpened= face-sharpened
#    plt.figure(figsize=(18,8))
#    plt.imshow(blurred_f-face)
#    plt.savefig("C:/Users/madel/OneDrive/Documents/unblur_filter/blur.png")
    
    #sharpened = face - alpha*blurred_f
 
    plt.figure(figsize=(18,8))
    plt.imshow(sharpened, cmap=plt.cm.gray) 
    plt.savefig("C:/Users/madel/OneDrive/Documents/unblur_filter/alpha.png")
    im = Image.fromarray(blurred_f)
    
    
    im.save("C:/Users/madel/OneDrive/Documents/unblur_filter/images/blurred_images/%d.png" %alpha)
    
#    img = cv2.imread(img,0)
 #   cv2.imshow("Edited and not suspicious at all", img)
   # sharpened.show()
   ## cv2.imshow("Edited and not suspicious at all", sharpened)
   

photo = "C:/Users/madel/OneDrive/Pictures/image_practice.PNG"
filter_photo_3(photo)

