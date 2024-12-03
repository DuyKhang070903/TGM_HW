I = imread("Test_Image.jpg");
imshow(I);
T = adaptthresh(I,0.3,'ForegroundPolarity','dark');
BW = imbinarize(I,T);
BW = squeeze(BW(:,:,1));
imshow(BW);