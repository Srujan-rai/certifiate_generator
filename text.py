import cv2
import os
img=cv2.imread('participation.png')

img=cv2.putText(img,"Srujan rai",(100, 595),cv2.FONT_HERSHEY_TRIPLEX ,1.6,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("image",img)
cv2.imwrite("image.pdf",img)
cv2.destroyAllWindows()
