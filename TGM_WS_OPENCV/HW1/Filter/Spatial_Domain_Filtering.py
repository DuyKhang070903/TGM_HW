import cv2
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Filter/HW1_BoxFilter.jpg')

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(A, cv2.COLOR_BGR2RGB))  # Chuyển ảnh từ BGR sang RGB để hiển thị đúng màu sắc
plt.title('Original image')

# Áp dụng bộ lọc box 5x5 (tương đương với imboxfilt(A, 5) trong MATLAB)
A_filter_5x5 = cv2.blur(A, (5, 5))

# Hiển thị ảnh sau khi dùng box filter 5x5
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(A_filter_5x5, cv2.COLOR_BGR2RGB))
plt.title('Box filter 5x5')

# Áp dụng bộ lọc box 15x15 (tương đương với imboxfilt(A, 15) trong MATLAB)
A_filter_15x15 = cv2.blur(A, (15, 15))

# Hiển thị ảnh sau khi dùng box filter 15x15
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(A_filter_15x15, cv2.COLOR_BGR2RGB))
plt.title('Box filter 15x15')

plt.show()
