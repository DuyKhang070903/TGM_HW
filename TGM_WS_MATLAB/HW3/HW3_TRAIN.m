idir = 'D:\TGM_HW_DK\TGM_WS_MATLAB\HW3';

% Tải file dữ liệu sign
load(fullfile(idir, 'sign.mat'));

% Tạo danh sách ảnh dương từ gTruth
positiveInstances = objectDetectorTrainingData(gTruth);

imDir = fullfile(idir, 'SignImage');
addpath(imDir);

negativeImages = fullfile(idir, 'NegativeImage');

cd(idir); % Đặt thư mục làm việc hiện tại là 'idir'
trainCascadeObjectDetector('sign.xml', positiveInstances, ...
    negativeImages, 'FalseAlarmRate', 0.2, 'NumCascadeStages', 5);


