%%%%%%%%%%%
A = imread('HW1_DarkImage.jpg');
Heq = histeq(A);
imshowpair(A, Heq, 'montage')
imhist(A,100)
imhist(Heq,100)
