import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Edge_Detection/Test_Image2.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(
    img,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=15,
    param1=100,  #Giá trị càng lớn thì giảm bớt các cạnh yếu, từ đó giảm số lượng vòng tròn được phát hiện
    param2=30,   #Giá trị này càng cao thì yêu cầu độ chính xác của đường tròn càng cao, giảm số lượng vòng tròn được phát hiện
    minRadius=10,
    maxRadius=50
)

if circles is not None:
    circles = np.uint16(np.around(circles)) 
    for i in circles[0, :]:
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Vẽ vòng tròn bên ngoài
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)     # Vẽ tâm của đường tròn
        
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cimg, cmap='gray')
plt.title('Detected Circles')
plt.show()
