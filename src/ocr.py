try:
    import Image
except ImportError:
    from PIL import Image

import cv2
import pandas as pd
import pytesseract
import cv2
import remove_noise as rn
import re
import numpy as np


#read image
img='dl3.jpg'

#preprocessing
img=rn. process_image_for_ocr(img)

#extract the text
text=pytesseract.image_to_string(img)

#text = text.replace('\n', ' ').replace('\r', '')

data_requ={}

#split across : 
for i in text.split("\n"):
	if ':' in i:
		j=i.split(':')
		data_requ[j[0]]=(j[1])
#print(data)

text1 = text.replace('\n', ' ').replace('\r', '')
#print(text1)
#for Address 
add=[]
add.append(re.search(r'Address:(.*?)Authorisation',text1 ).group(1))
data_requ['Address']=add

#for DOB
dob=[]
dob.append(re.search(r'DOB: (.*?)86',text1 ).group(1))
data_requ['DOB']=dob
#print(dob)
bg=[]
bg.append(re.search(r'86:(.*?)Address',text1 ).group(1))
data_requ['bg']=bg

#make dataframe
df=pd.DataFrame(data=data_requ)
df.to_csv('details.csv',sep=',')

