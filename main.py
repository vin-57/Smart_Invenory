import cv2
import numpy as np
from pyzbar.pyzbar import decode # libary, that allows us to detect qr-code and decod it

#img = cv2.imread('1.png')
#code=decode(img)
#print(code)

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()
 #print(myDataList)

while True:

    success, img = cap.read()
    for barcode in deode (img):
    #print (barcode.data)
    myData = barcode.data.decode('utf-8')
    print(myData)
    
    if myData in myDataList:
        myOutput='Inventoryed'
        myColor = (0, 255, 0)
    else:
        myOutput='Un-Inventoryed'
        myColor = (0, 0, 255)

    pts = np.array([barcode.polygon],np.int32) #use poligon
    pts = pts.reshape ((-1, 1,2))
    cv2.polylines(img, [pts], True, myColor, 5)
    pts2 = barcode.rect
    cv2.putText(img, myData, (pts2[0], pts2[1], cv2.FONT_HERSHEY_SIMPEX, 0.9, myColor, 2))

cv2.imshow("result", img)
cv2.waitKey(1)
