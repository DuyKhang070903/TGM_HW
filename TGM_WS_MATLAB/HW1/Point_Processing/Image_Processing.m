%%%%%%%%%%
A = imread('HW1_OnePiece.jpg');
% imshow(A)

gray_A = rgb2gray(A);
% imshowpair(A, gray_A, 'montage')

negative_A = 255 - gray_A;
imshowpair(gray_A, negative_A, 'montage')




