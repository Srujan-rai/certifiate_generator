import cv2
import os
img=cv2.imread('1.jpg')

img=cv2.putText(img,"srujan_uehfheihi",(1188,1600),cv2.FONT_HERSHEY_COMPLEX,4,(0,0,0),7)
cv2.imshow("image",img)
cv2.imwrite("image.jpg",img)
cv2.destroyAllWindows()