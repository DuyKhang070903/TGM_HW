I = imread("Test_Image.jpg");
SE = strel('disk', 5);
I_Clo = imopen(I, SE);
imshowpair(I,I_Clo,'montage');