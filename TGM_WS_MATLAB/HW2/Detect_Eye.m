EyeDetector = vision.CascadeObjectDetector('EyePairBig');
C = imread('D:\TGM_WS_MATLAB\TestImages\Test_Image22.jpg');
bodyDetector.MinSize = [0.005 0.005];
bboxes = EyeDetector(C);
CEyes = insertObjectAnnotation(C,'rectangle',bboxes,'mat');
figure
imshow(CEyes)
title('Nhận diện mắt');