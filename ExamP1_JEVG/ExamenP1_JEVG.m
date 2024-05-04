%% Clean the window and data and add the value to variables Contrast and the Bias
clc, clear
close all;
C=0.2;
B=30;
B2=1;

%% Read the image and aply gray and add Bias and contrast
x=imread("DogColor.png");
x2=rgb2gray(x);
% Bias
x3 = x + B;
% Contrast
x4=x2*C+B2;
x5=x2*C+B;;
x6=imadjust(x3, [0 1], [0.1 0.9]);

%% Plot the images in the same figure
figure
subplot(2,3,1)
title('Imagen Original') 
imshow(x)
subplot(2,3,2)
imshow(x2)
title('Imagen a escala de grises') 
subplot(2,3,3)
imshow(x3)
title('Imagen brillo al 30%')
subplot(2,3,4)
imshow(x4)
title('Imagen Contraste al 20%') 
subplot(2,3,5)
imshow(x5)
title('Imagen Contraste al 20% y Brillo al 30% METODO 1')
subplot(2,3,6)
imshow(x5)
title('Imagen Contraste al 20% y Brillo al 30% METODO 2') 