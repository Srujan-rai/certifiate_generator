import cv2
import os
import pandas as pd

df=pd.read_csv('info.csv')
base_image_path="Certificate Final v2.png"
base_image=cv2.imread(base_image_path)
 
output_folder="output"
os.makedirs(output_folder,exist_ok=True)

thickness=3
font=cv2.FONT_HERSHEY_COMPLEX
colour=(0,0,0)
font_scale=1.3
for index,row in df.iterrows():
    name=str(row['name'])
    img_to_text=base_image.copy()
    cv2.putText(img_to_text,name,(790,855),font,font_scale,colour,thickness)
    output_folder_path=os.path.join(output_folder,f"{name}.jpg")
    cv2.imwrite(output_folder_path,img_to_text)
    print(f"certficate {name} is done")    
print("image saved successfully")