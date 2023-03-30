%% Clean the window and data, Put a valor to variables Contrast and the Bias
clc, clear
close all;
C=1;
B=0.5;
%% Read the image invert the colors and apply gray 
x = imread('Monedas.jpg');
x2 = imcomplement(x);
I = rgb2gray(x2);
%% Pa to Binary and fill the holes
xBinary = imbinarize(I);
xBinaryPro = imfill(xBinary,'holes');
%% invert the colors to the final Binary Image 
xBinaryInvert = imcomplement(xBinaryPro);
%% Plot the images in the same figure
Fig = figure('Name', 'T2. Identificación de monedas Binario  - JEVG');
set(Fig, 'Position', [500 0 1250 1250])
subplot(2,3,2)
imshowpair(x,x2,'montage')
title('Imagen Original e Imagen Invertida')
subplot(2,3,4)
imshow(xBinary)
title('Imagen con colores Invertidos convertida a Binaria')
subplot(2,3,3)
imshow(xBinaryInvert)
title('Imagen sin Huecos con Color Invertido')
subplot(2,3,6)
imshow(xBinaryPro)
title('Imagen sin Huecos')