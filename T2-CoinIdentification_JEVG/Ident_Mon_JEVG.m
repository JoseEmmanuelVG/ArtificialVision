%% Clear the window and data, Put a valor to variables Contrast and the Bias
clc, clear
close all;
C=1;
B=0.5;

%% Read the image aply gray and insert Filters
    %Gray
x=imread("Monedas.jpg");
xGray = rgb2gray(x);

    %Binary 
xUmbral = graythresh(xGray);
xBinaria = imbinarize(xGray, xUmbral);

    %Umbral
level = graythresh(x);
xGrayThresh = imbinarize(x,level);

    %Filter Contrast and Bias
xFiltro = xBinaria*C+B;

    %Edge Border Detection
xBordeSobel = edge(xGray,'sobel');
xBordeCanny = edge(xGray,'canny');

%% Plot the images in the same figure
Fig = figure('Name', 'T2. Identificación de monedas  - JEVG');
set(Fig, 'Position', [500 0 1250 1250])
subplot(4,3,1)
imshow(x)
title('Imagen Original')
subplot(3,3,2)
imshow(xGray)
title('Escala de Grises')
subplot(3,3,3)
imshow(xBinaria)
title('Binaria')
subplot(3,3,4)
imshow(xFiltro)
title('Contraste y Brillo')
subplot(3,3,5)
imshow(xBordeSobel)
title('Filtro Sobel')
subplot(3,3,6)
imshow(xBordeCanny)
title('Filtro Canny')
subplot(3,3,8)
imshowpair(x,xGrayThresh,'montage')
title('Umbral de imagen global usando el método de Otsu')

