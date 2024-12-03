I = imread("Test_Image.jpg");
SE = strel('disk', 4);
I_edg = imdilate(I, SE);
SE = strel('disk', 4);
I_Dil = imdilate(I, SE);
I_edg = I_Dil - I;
imshowpair(I,I_edg,'montage');