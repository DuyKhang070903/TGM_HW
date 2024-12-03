import cv2
from matplotlib import pyplot as plt


A = cv2.imread('D:/TGM_WS_OPENCV/HW1/Image_Segmentation/Test_Image.jpg', cv2.IMREAD_GRAYSCALE)

thresh, otsu = cv2.threshold(A, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('otsu.jpg', otsu)

plt.subplot(1, 2, 1)
plt.imshow(A, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(otsu, cmap='gray')
plt.title('Ostu_Image')
plt.show()
