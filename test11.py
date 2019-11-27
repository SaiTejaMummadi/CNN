import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('1.jpg')
img = img[350:1100,0:700]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 160, apertureSize=3)

minLineLength =0
maxLineGap = 2

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 150, minLineLength, maxLineGap, 10)
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(img, (x1, y1), (x2, y2), (153, 0, 0), 2)

#cv2.imwrite('houghlines.jpg', img)
#cv2.imwrite('houghedge.jpg', edges)
cv2.imshow("image", edges)
#cv2.imshow('img', img)
plt.imshow(img)
plt.show()
print(img.shape)
cv2.waitKey(0)
