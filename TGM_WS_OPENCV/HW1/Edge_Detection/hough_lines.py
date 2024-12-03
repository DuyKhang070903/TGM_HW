import cv2
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Edge_Detection/Test_Image1.jpg')
I = A.copy()
A_gray = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(A_gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

for line in lines[0:10]:
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(A, (x1,y1), (x2,y2), (0,0,255), 1)
plt.subplot(1, 3, 1)
plt.imshow(I, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edges Image')

plt.subplot(1, 3, 3)
plt.imshow(A, cmap='gray')
plt.title('Lines Image')
plt.show()
