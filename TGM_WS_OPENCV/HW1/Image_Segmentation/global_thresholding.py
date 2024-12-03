import cv2
from matplotlib import pyplot as plt


A = cv2.imread('D:/TGM_WS_OPENCV/HW1/Image_Segmentation/Test_Image1.jpg')

_, thresh1 = cv2.threshold(A, 127, 255, cv2.THRESH_BINARY)
_, thresh2 = cv2.threshold(A, 127, 255, cv2.THRESH_BINARY_INV)
_, thresh3 = cv2.threshold(A, 127, 255, cv2.THRESH_TRUNC)
_, thresh4 = cv2.threshold(A, 127, 255, cv2.THRESH_TOZERO)
_, thresh5 = cv2.threshold(A, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [A, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()