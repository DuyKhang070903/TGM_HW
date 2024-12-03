load('D:\TGM_WS_MATLAB\Train_Data_Label\Train_Data_Label.mat');

Facedetect = selectLabels(gTruth,'face');

if isfolder(fullfile('TrainingData'))    
cd TrainingData
else 
mkdir TrainingData
end
addpath('TrainingData');

trainingData = objectDetectorTrainingData(Facedetect,'SamplingFactor',1,'writeLocation','TrainingData');
detector = trainACFObjectDetector(trainingData,'NumStages',20);
save('Detector.mat','detector');
rmpath('TrainingData');

% % Tải dữ liệu ground truth
% load('D:\TGM_WS_MATLAB\Train_Data_Label\Train_Data_Label.mat');
% 
% % Chọn nhãn 'face' từ dữ liệu
% Facedetect = selectLabels(gTruth, 'face');
% 
% % Tạo thư mục lưu dữ liệu huấn luyện
% if ~isfolder('TrainingData')
%     mkdir('TrainingData');
% end
% 
% % Xuất dữ liệu ground truth thành định dạng XML để dùng với Viola-Jones
% trainingData = objectDetectorTrainingData(Facedetect, 'SamplingFactor', 1, 'WriteLocation', 'TrainingData');
% positiveInstances = trainingData(:, {'imageFilename', 'objectBoundingBoxes'});
% 
% % Ghi lại các nhãn đối tượng vào file XML
% annotationFile = 'TrainingData\annotations.xml';
% writeObjectDetectorAnnotations(positiveInstances, annotationFile);
% 
% Đường dẫn lưu kết quả mô hình huấn luyện
% outputDir = fullfile('TrainingData', 'ViolaJonesModel');
% 
% % Huấn luyện bộ phát hiện đối tượng bằng Viola-Jones
% trainCascadeObjectDetector(outputDir, annotationFile, 'TrainingData', ...
%     'FeatureType', 'Haar', 'NumCascadeStages', 20);
% 
% % Lưu mô hình sau khi huấn luyện
% save('ViolaJones_Detector.mat', 'outputDir');
% 
% disp('Viola-Jones training complete.');


% Viola - Jone
% % Load ground truth data (gTruth) đã gắn nhãn từ Image Labeler hoặc gTruth từ file .mat
% load('gTruth.mat');  % Thay bằng file gTruth của bạn
% 
% % Chọn label cần train (giả sử label là 'Object')
% objectLabels = selectLabels(gTruth, 'Object');
% 
% % Tạo thư mục lưu trữ dữ liệu huấn luyện
% if ~isfolder('TrainingData')
%     mkdir TrainingData
% end
% 
% % Xuất dữ liệu huấn luyện
% trainingData = objectDetectorTrainingData(objectLabels, 'SamplingFactor', 1, 'WriteLocation', 'TrainingData');
% 
% % Huấn luyện bộ phát hiện sử dụng thuật toán Viola-Jones
% % Lưu ý: 'NumCascadeStages' ảnh hưởng đến độ chính xác và thời gian train
% trainCascadeObjectDetector('objectDetector.xml', trainingData, ...
%     'FalseAlarmRate', 0.1, 'NumCascadeStages', 10);
% 
% disp('Training completed. The detector is saved as objectDetector.xml');

