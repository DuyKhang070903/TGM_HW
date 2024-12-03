%%%%%%%%%%%
A = imread('HW1_HistogramSourceImage.jpg');
Ref = imread('HW1_HistogramRefImage.jpg');
B = imhistmatch(A,Ref);
imshow(A)
title('Original Image')
imhist(A)
imshow(Ref)
title('Reference Image')
imhist(Ref)
imshow(B)
title('Output Image')
% imhist(B)
