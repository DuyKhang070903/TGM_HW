I = imread("Test_Image.jpg");
I = squeeze(I(:,:,1));
I_sobel = edge(I, 'sobel',0.1);
subplot(1,2,1);
imshow(I);
title('Original Image');
subplot(1,2,2);
imshow(I_sobel);
title('Sobel');
