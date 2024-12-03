import cv2
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Filter/HW1_MedianFilter.jpg')
# Thêm nhiễu 
# Prob giá trị xác xuất mà một điểm ảnh bị biến đổi thành muối(255) hoặc tiêu(0), tầm giá trị o->1
def add_salt_pepper_noise(image, prob):
    output = np.copy(image)
    # Xác suất cho nhiễu muối và tiêu
    salt = np.ceil(prob * image.size * 0.5)
    pepper = np.ceil(prob * image.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(salt)) for i in image.shape]
    output[coords[0], coords[1], :] = 255 # muối
    coords = [np.random.randint(0, i - 1, int(pepper)) for i in image.shape]
    output[coords[0], coords[1], :] = 0 # tiêu
    return output

B = add_salt_pepper_noise(A, 0.04)
B_gray = cv2.cvtColor(B, cv2.COLOR_BGR2GRAY)

plt.subplot(1, 2, 1)
plt.imshow(B_gray, cmap='gray')
plt.title('Noise salt & pepper')
# Lọc Median
C = cv2.medianBlur(B_gray, 3)

plt.subplot(1, 2, 2)
plt.imshow(C, cmap='gray')
plt.title('Output image use Median Filter')
plt.show()



