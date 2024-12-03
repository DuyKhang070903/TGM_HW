I = imread('Test_Image2.jpg');
imshow(I)
[centers, radii, metric] = imfindcircles(I, [10 30]);
centersStrong10 = centers(1:10, :);
radiiStrong10 = radii(1:10);
metricStrong10 = metric(1:10);
viscircles(centersStrong10, radiiStrong10, 'EdgeColor', 'b');
