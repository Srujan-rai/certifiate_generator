import cv2
import os
img=cv2.imread('Certificate v4.png')

img=cv2.putText(img,"Input text here",(790, 855),cv2.FONT_HERSHEY_COMPLEX,1.3,(0,0,0),3)
cv2.imshow("image",img)
cv2.imwrite("image.jpg",img)
cv2.destroyAllWindows()
