FaceDetector = vision.CascadeObjectDetector;
I = imread('D:\TGM_WS_MATLAB\TestImages\Test_Image21.jpg');
bboxes = FaceDetector(I);
IFaces = insertObjectAnnotation(I,'rectangle',bboxes,'mat');
figure
imshow(IFaces)
title('Nhận diện khuôn mặt');