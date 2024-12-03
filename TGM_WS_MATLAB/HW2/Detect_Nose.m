NoseDetector = vision.CascadeObjectDetector('Nose');
B = imread('D:\TGM_WS_MATLAB\TestImages\Test_Image22.jpg');
bodyDetector.MinSize = [0.005 0.005];
bboxes = NoseDetector(B);
BNoses = insertObjectAnnotation(B,'rectangle',bboxes,'mui');
figure
imshow(BNoses)
title('Nhận diện mũi');