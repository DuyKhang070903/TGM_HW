%%%%%%%%%%%
A = imread('HW1_MedianFilter.jpg');
B = imnoise(A, 'salt & pepper', 0.04);
B_gray = rgb2gray(B);
imshow(B_gray);
title('Noise salt & pepper');
C = medfilt2(B_gray);
imshow(C);
title('Output image use Median Filter');
