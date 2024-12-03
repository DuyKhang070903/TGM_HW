# Chưa xong
import cv2
import matplotlib.pyplot as plt
from skimage.exposure import match_histograms

# Đọc ảnh gốc và ảnh tham chiếu
A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Histogram/HW1_HistogramSourceImage.jpg')
Ref = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Histogram/HW1_HistogramRefImage.jpg')

# Chuyển đổi ảnh từ BGR (OpenCV) sang RGB (Matplotlib/Scikit-image)
A_rgb = cv2.cvtColor(A, cv2.COLOR_BGR2RGB)
Ref_rgb = cv2.cvtColor(Ref, cv2.COLOR_BGR2RGB)

# Thực hiện khớp histogram
B_rgb = match_histograms(A_rgb, Ref_rgb)

# Hiển thị ảnh gốc, ảnh tham chiếu và ảnh kết quả
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(A_rgb)
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(Ref_rgb)
plt.title('Reference Image')

plt.subplot(1, 3, 3)
plt.imshow(B_rgb)
plt.title('Output Image')

plt.show()

# Hiển thị histogram của ảnh gốc, ảnh tham chiếu và ảnh kết quả
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(A_rgb.ravel(), bins=256, color='blue', alpha=0.5, label='Original')
plt.legend()

plt.subplot(1, 3, 2)
plt.hist(Ref_rgb.ravel(), bins=256, color='green', alpha=0.5, label='Reference')
plt.legend()

plt.subplot(1, 3, 3)
plt.hist(B_rgb.ravel(), bins=256, color='red', alpha=0.5, label='Matched Output')
plt.legend()

plt.show()

