load('D:\TGM_WS_MATLAB\HW2\TrainingData\Detector.mat');
% 
img = imread('D:\TGM_WS_MATLAB\TestImages\Test_Image21.jfif');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% % img = imread('D:\TGM_WS_MATLAB\Test_Image.jpg');
% 
[bboxes,scores] = detect(detector,img);

for i = 1:length(scores)
  
   annotation = sprintf('Face with Confidence = %.1f',scores(i));
   %annotation is labels like face and Confidence in percentage
   img = insertObjectAnnotation(img,'rectangle',bboxes(i,:),annotation);
end

figure
imshow(img);


% Test 2
% % Đường dẫn thư mục chứa 20 ảnh
% imageFolder = 'D:\TGM_WS_MATLAB\TestImages\'; % Thay bằng thư mục chứa ảnh
% imageFiles = dir(fullfile(imageFolder, '*.jpg')); % Lấy danh sách các file .jpg trong thư mục
% numImages = length(imageFiles); % Số lượng ảnh
% 
% % Load module detector
% load('D:\TGM_WS_MATLAB\HW2\TrainingData\Detector.mat');
% 
% % Tạo figure cho việc hiển thị
% figure('WindowStyle', 'normal');;
% 
% set(gcf, 'Position', [100, 100, 1600, 700]); % Điều chỉnh kích thước figure
% 
% % Sử dụng tiledlayout để tùy chỉnh khoảng cách
% tiledlayout(5, 4, 'Padding', 'compact', 'TileSpacing', 'compact'); % Lưới 5x4
% 
% % Vòng lặp qua từng ảnh để xử lý và hiển thị
% for i = 1:numImages
%     % Đọc từng ảnh
%     imgPath = fullfile(imageFolder, imageFiles(i).name);
%     img = imread(imgPath);
%     
%     % Phát hiện đối tượng trong ảnh
%     [bboxes, scores] = detect(detector, img);
%     
%     % Gắn nhãn các đối tượng
%     for j = 1:length(scores)
%         annotation = sprintf('Confidence = %.1f', scores(j) * 100); % Hiển thị phần trăm
%         img = insertObjectAnnotation(img, 'rectangle', bboxes(j, :), annotation);
%     end
%     
%     % Hiển thị kết quả trong subplot
%     subplot(ceil(sqrt(numImages)), ceil(sqrt(numImages)), i); % Tạo lưới ô vuông
%     imshow(img,'InitialMagnification', 'fit');
%     title(sprintf('Image %d', i)); % Tiêu đề ảnh
% end
% 
% % Tối ưu kích thước và hiển thị đầy đủ
% sgtitle('Detection Results from All Images'); % Tiêu đề chung


% Viola - Jone
% % Đọc file XML đã huấn luyện (Viola-Jones detector)
% detector = vision.CascadeObjectDetector('objectDetector.xml');
% 
% % Đọc hình ảnh cần phát hiện
% img = imread('testImage.jpg');  % Thay bằng hình ảnh của bạn
% 
% % Phát hiện đối tượng
% bboxes = step(detector, img);
% 
% % Hiển thị kết quả phát hiện
% detectedImg = insertObjectAnnotation(img, 'rectangle', bboxes, 'Object');
% imshow(detectedImg);
% title('Detected Objects');
