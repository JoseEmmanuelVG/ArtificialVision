%% Clean the window and data
clc, clear
close all;

%% Read the image and Convert the to the same size
% Load the two images you want to resize
a = imread('Monedas.jpg');
b = imread('Cuadros.jpg');

% Determine the size of the larger image
max_size = max(size(a), size(b));

% Resize both images to the maximum size
x = imresize(a, max_size(1:2));
y = imresize(b, max_size(1:2));


%% Gray  and invert the colors
x2 = imcomplement(x);
I = rgb2gray(x2);
    y2 = imcomplement(y);
    l = rgb2gray(y2);

%% Pass to Binary and fill the holes
xBinary = imbinarize(I);
xBinaryPro = imfill(xBinary,'holes');
    yBinary = imbinarize(l);
    yBinaryPro = imfill(yBinary,'holes');
% invert the colors to the final Binary Image 
xBinaryInvert = imcomplement(xBinaryPro);
yBinaryInvert = imcomplement(yBinaryPro);


%% Operations &, !!, XOR 
and_img = bitand(xBinaryInvert, yBinaryInvert);
or_img = bitor(xBinaryInvert, yBinaryInvert);
xor_img = bitxor(xBinaryInvert, yBinaryInvert);
    and_img2 = bitand(xBinaryPro, yBinaryPro);
    or_img2 = bitor(xBinaryPro, yBinaryPro);
    xor_img2 = bitxor(xBinaryPro, yBinaryPro);


%% Plot the images in the same figure
Fig = figure('Name', 'T4. Compuertas Lógicas - JEVG');
set(Fig, 'Position', [500 0 1250 1250])
subplot(4,3,2)
imshowpair(x,x2,'montage')
title('Imagen Original e Imagen Invertida')
subplot(4,3,1)
imshow(xBinaryInvert)
title('Imagen sin Huecos con Color Invertido')
subplot(4,3,3)
imshow(xBinaryPro)
title('Imagen sin Huecos')
    subplot(4,3,5)
    imshowpair(y,y2,'montage')
    title('Imagen Original e Imagen Invertida')
    subplot(4,3,4)
    imshow(yBinaryInvert)
    title('Imagen sin Huecos con Color Invertido')
    subplot(4,3,6)
    imshow(yBinaryPro)
    title('Imagen sin Huecos')
%Plot the images with some operation
subplot(4,3,7)
imshow(and_img)
title('AND Imagen sin Huecos con Color Invertido')
    subplot(4,3,8)
    imshow(or_img)
    title('OR')
        subplot(4,3,9)
        imshow(xor_img)
        title('XOR')
subplot(4,3,10)
imshow(and_img2)
title('AND Imagen sin Huecos')
    subplot(4,3,11)
    imshow(or_img2)
    title('OR')
        subplot(4,3,12)
        imshow(xor_img2)
        title('XOR')