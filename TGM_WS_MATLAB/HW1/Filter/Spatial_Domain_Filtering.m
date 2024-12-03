%%%%%%%%%%%%
A = imread('HW1_BoxFilter.jpg');
imshow(A)
title('Original image')
A_filter = imboxfilt(A,5);
imshow(A_filter)
title('Output image use box filter 5x5')
A_filter = imboxfilt(A,15);
imshow(A_filter)
title('Output image use box filter 15x15')