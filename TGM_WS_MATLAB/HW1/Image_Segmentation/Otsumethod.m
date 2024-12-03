I = imread("Test_Image.jpg");
imshow(I);
A = graythresh(I);
BW = imbinarize(I,A);
BW = squeeze(BW(:,:,1));
imshow(BW);