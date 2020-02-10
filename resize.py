import os
import cv2
import glob
import numpy as np

img_dir ="E:\Kampus-\Materi\Skripsweet\Python\GLCM\Gray-Level-Cooccurrence-Matrix-master\sampel\Sampel"
data_path = os.path.join(img_dir,'*jpg')
files = glob.glob(data_path)
result = []
for f1 in files:
    img = cv2.imread(f1)
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    imageresized = cv2.resize(image_gray,(96,96) ,interpolation=cv2.INTER_AREA)
    
    result.append(imageresized)
    

     #save each image
    iteratorName = 1
    prefixPathDir = "E:\Kampus-\Materi\Skripsweet\Python\GLCM\Gray-Level-Cooccurrence-Matrix-master\Sampel"
    for img in result :
        cv2.imwrite(prefixPathDir+str(iteratorName)+".jpg", img)
        iteratorName+=1
