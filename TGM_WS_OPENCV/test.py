import cv2
# import numpy as np

img = cv2.imread('D:/hinh-anh-long-lan-trong-phong-thuy.jpg',1)

# gray_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.rotate(img,cv2.ROTATE_180)

# Hiển thị ảnh xám
cv2.imshow('Display Image', img)

# Chờ phím nhấn và đóng cửa sổ hiển thị
cv2.waitKey(0)
# cv2.destroyAllWindows()

#print(img)
print(type(img))

print(img.shape)

# gray_x = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

# cv2.imshow('Display Image', img)

# cv2.waitKey(0)

# cv2.destroyAllWindows()

# import cv2

# # Đọc ảnh từ đường dẫn
# img = cv2.imread('D:/hinh-anh-long-lan-trong-phong-thuy.jpg')

# # Kiểm tra nếu ảnh được đọc thành công
# if img is not None:
#     # Chuyển đổi ảnh màu sang ảnh xám
#     gray_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Hiển thị ảnh xám
#     cv2.imshow('Display Image', gray_x)

#     # Chờ phím nhấn và đóng cửa sổ hiển thị
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Error: Image not found or unable to load.")

