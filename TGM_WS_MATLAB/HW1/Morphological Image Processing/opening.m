I = imread("Test_Image.jpg");
SE = strel('disk', 5);
I_Op = imopen(I, SE);
imshowpair(I,I_Op,'montage');