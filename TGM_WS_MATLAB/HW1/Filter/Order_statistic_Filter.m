%%%%%%%%%%
J = imread('HW1_OrderStatisticFilter.jpg');
imshow(J)
title('Original image')

gray_J = rgb2gray(J);
A_med = ordfilt2(gray_J, 5, ones(3,3));
imshow(A_med)
title('Median filter')

%Ảnh sau khi sử dụng max filter:
A_max = ordfilt2(gray_J, 9, ones(3,3));
imshow(A_max)
title('Max filter')



