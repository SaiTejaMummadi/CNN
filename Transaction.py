import numpy as np
import cv2

#We are solving this problem using click events
#To highlight the labels Merchant ID, Transaction ID use left arrow key for red color
#To highlight the values use the right arrow key
#Click on left upper corner and right down corner to create the rectangle values
#This is a interactive way to solve the prblem

def click_event(event, x, y, flags, param):
    #Left click for Blue color
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
        ID.append(x)
        ID.append(y)
        
    #Right Click for Red Color    
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x,', ' ,y)
        values.append(x)
        values.append(y)


ID = []
values =[]
img = cv2.imread('2.jpg')
img= cv2.resize(img,(700,1200))
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
print(ID)
print(values)
i=0
n=len(ID)
m=len(values)
print(n)
while(i<n):
    x1=(ID[i],ID[i+1])
    x2=(ID[i+2],ID[i+3])
    i=i+4
    img=cv2.rectangle(img,x1,x2,(230,216,173),-1)
i=0
while(i<m):
    x1=(values[i],values[i+1])
    x2=(values[i+2],values[i+3])
    i=i+4
    img=cv2.rectangle(img,x1,x2,(203,204,255),-1)
cv2.imshow('image', img)
cv2.imwrite('image.png', img)   
cv2.waitKey(0)
cv2.destroyAllWindows()
