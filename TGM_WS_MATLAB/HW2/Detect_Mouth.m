MouthDetector = vision.CascadeObjectDetector('Mouth');
A = imread('D:\TGM_WS_MATLAB\TestImages\Test_Image22.jpg');
bboxes = MouthDetector(A);
AMouths= insertObjectAnnotation(A,'rectangle',bboxes,'mieng');
figure
imshow(AMouths)
title('Nhận diện miệng');