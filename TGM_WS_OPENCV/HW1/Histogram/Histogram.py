import cv2
import matplotlib.pyplot as plt

# A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Histogram/HW1_BrightImage.jpg')
# cv2.imshow('Bright Image', A)

# # Hiển thị histogram của ảnh sáng
# plt.figure()
# plt.title('Histogram for Bright Image')
# plt.hist(A.ravel(), bins=256, range=[0, 256])
# plt.show()

# B = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Histogram/HW1_DarkImage.jpg')
# cv2.imshow('Dark Image', B)

# # Hiển thị histogram của ảnh tối
# plt.figure()
# plt.title('Histogram for Dark Image')
# plt.hist(B.ravel(), bins=256, range=[0, 256])
# plt.show()

C = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Histogram/HW1_HighContrastImage.jpg')
cv2.imshow('High Contrast Image', C)

# Hiển thị histogram của ảnh có độ tương phản cao
plt.figure()
plt.title('Histogram for High Contrast Image')
plt.hist(C.ravel(), bins=256, range=[0, 256])
plt.show()

# D = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Histogram/HW1_LowContrastImage.jpg')
# cv2.imshow('Low Contrast Image', D)

# # Hiển thị histogram của ảnh có độ tương phản thấp
# plt.figure()
# plt.title('Histogram for Low Contrast Image')
# plt.hist(D.ravel(), bins=256, range=[0, 256])
# plt.show()

