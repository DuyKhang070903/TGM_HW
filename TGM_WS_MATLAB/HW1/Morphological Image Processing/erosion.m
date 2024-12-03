I = imread("Test_Image.jpg");
SE = strel('square', 5);
I_Ero = imerode(I, SE);
imshowpair(I,I_Ero,'montage');