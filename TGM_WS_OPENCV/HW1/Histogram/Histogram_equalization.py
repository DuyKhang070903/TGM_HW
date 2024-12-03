import cv2
import matplotlib.pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Histogram/HW1_DarkImage.jpg', cv2.IMREAD_GRAYSCALE)
# Hàm cv2.equalizeHist() chỉ hoạt động với ảnh grayscale (ảnh đơn kênh, 8-bit) nên phải thêm đoạn cv2.IMREAD_GRAYSCALE 
# để chuyển ảnh về đúng định dạng
Heq = cv2.equalizeHist(A)
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(A, cmap='gray')
plt.title("Ảnh Gốc")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.hist(A.ravel(), bins=100, range=[0, 256], color='blue')
plt.title("Histogram Ảnh Gốc")

plt.subplot(2, 2, 3)
plt.imshow(Heq, cmap='gray')
plt.title("Ảnh Sau Cân Bằng Histogram")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.hist(Heq.ravel(), bins=100, range=[0, 256], color='green')
plt.title("Histogram Ảnh Sau Cân Bằng")

plt.show()


