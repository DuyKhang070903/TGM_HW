% Use the AlexNet model
net = alexnet;
% Get the input size and class names of the model
inputSize = net.Layers(1).InputSize;
classNames = net.Layers(end).ClassNames;
numClasses = numel(classNames);
% Specify the folder containing the images to classify
% imageFolder = 'D:/TGM_HW_DK/TGM_WS_MATLAB/HW9/Dog';
% imageFolder = 'D:/TGM_HW_DK/TGM_WS_MATLAB/HW9/cellphone';
% imageFolder = 'D:/TGM_HW_DK/TGM_WS_MATLAB/HW9/airplanes';
% imageFolder = 'D:/TGM_HW_DK/TGM_WS_MATLAB/HW9/elephant';
imageFolder = 'D:/TGM_HW_DK/TGM_WS_MATLAB/HW9/crayfish';
% imageFolder = 'D:/TGM_HW_DK/TGM_WS_MATLAB/HW9/Cucumber';
% Find all the files in the folder matching the pattern
theFiles = dir(fullfile(imageFolder, '*.jpg'));
% theFiles = dir(fullfile(imageFolder, '*.png'));
% Loop over each image file and classify using the AlexNet model
figure
for k = 1 : length(theFiles)
    baseFileName = theFiles(k).name;
    fullFileName = fullfile(theFiles(k).folder, baseFileName);
    fprintf(1, 'Now reading %s\n', fullFileName);
    % Read and resize the image
    image = imread(fullFileName);
    image = imresize(image, inputSize(1:2));
    % Classify the image
    [label, scores] = classify(net, image);
    [~, idx] = sort(scores, 'descend');
    idx = idx(5:-1:1);
    classNamesTop = net.Layers(end).ClassNames(idx);
    scoresTop = scores(idx);
% Display the image and top 5 predictions
    if k <= 10
        subplot(4, 10, k);
        imshow(image);
        subplot(4, 10, k+10);
        barh(scoresTop)
        xlim([0 1])
        title('Top 5 Predictions')
        xlabel('Probability')
        yticklabels(classNamesTop)
    else
        subplot(4, 10, k+10);
        imshow(image)
        subplot(4, 10, k+20);
        barh(scoresTop)
        xlim([0 1])
        title('Top 5 Predictions')
        xlabel('Probability')
        yticklabels(classNamesTop)
    end
end