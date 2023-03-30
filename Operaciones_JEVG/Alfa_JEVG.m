%% Clean the window and data, Put a valor to variables Contrast and the Bias
clc, clear
close all;
%% Read the image and work with the size
a = imread('Cuadros.jpg');
% Determine the size of the larger image
[M1,N1]=size(a);
[M2,N2]=size(b);
N_min=min(N1,N2);
M_min=min(M1,M2);


%% Gray  and invert the colors
x = rgb2gray(a);
y = rgb2gray(b);

%% Operations &, !!, XOR 
for j=1:N_min
    for i=1:M_min
        I(i,j)=(1-alpha)*x(i,j)+alfa*y(i,j)
    end
end    


%% Plot the images in the same figure
Fig = figure('Name', 'T2. Identificación de monedas Binario  - JEVG');
set(Fig, 'Position', [500 0 1250 1250])
subplot(2,2,1)
imshowpair(a,x,'montage')
title('Imagen Original 1')
    subplot(2,2,2)
    imshowpair(b,y,'montage')
    title('Imagen Original 2')
title('Imagen Original e Imagen Invertida')
subplot(2,2,3)
imshow(I)
title('Imagen CON ALPHA')

 