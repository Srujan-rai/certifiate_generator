import cv2
import os
img=cv2.imread('Certificate_of_Participation_G.png')

img=cv2.putText(img,"srujan",(790,855),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),3)
cv2.imshow("image",img)
cv2.imwrite("image.jpg",img)
cv2.destroyAllWindows()