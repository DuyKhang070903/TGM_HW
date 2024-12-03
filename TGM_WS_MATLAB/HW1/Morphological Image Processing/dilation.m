I = imread("Test_Image.jpg");
SE = strel('disk', 5);
I_Dil = imdilate(I, SE);
imshowpair(I,I_Dil,'montage');