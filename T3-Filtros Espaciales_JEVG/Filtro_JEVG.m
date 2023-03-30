%% Clean the window and data
clc, clear
close all;
%% Read the image and work with the size and gray
a = imread('LetraPixelada.jpg');
x = rgb2gray(a);
b = imread('LetrasPixeladas2.png');
y = rgb2gray(b);
% Determine the size of the larger image
[m,n]=size(x);
Im=double(x);
Im_filtro=Im;
[o,p]=size(y);
Im2=double(y);
Im_filtro2=Im2;

%% Operations to the Spacial Filter 
for r=2:m-1
    for c=2:n-1
        Im_filtro(r,c)=1/9*(Im(r-1,c-1) + Im(r-1,c) + Im(r-1,c+1) + ...
                            Im(r,c-1) + Im(r,c) + Im(r,c+1) + ...
                            Im(r+1,c-1) + Im(r+1,c) + Im(r+1,c+1));
    end
end    
Im_filtro=uint8(Im_filtro);
for r=2:o-1 
    for c=2:p-1
        Im_filtro2(r,c)=1/9*(Im2(r-1,c-1) + Im2(r-1,c) + Im2(r-1,c+1) + ...
                            Im2(r,c-1) + Im2(r,c) + Im2(r,c+1) + ...
                            Im2(r+1,c-1) + Im2(r+1,c) + Im2(r+1,c+1));
    end
end    
Im_filtro2=uint8(Im_filtro2);

%% Plot the images in the same figure
%Plot the first image with the Gray and Filter
Fig = figure('Name', 'T3. Filtro Espacial - JEVG');
set(Fig, 'Position', [0 0 1500 1500])
subplot(2,5,1); 
histogram(a,'FaceColor','r')
title('Histograma Imagen 1','FontWeight','bold','FontName','Arial Black','Color','Red');
subplot(2,5,2)
imshow(a)
title('Imagen Original 1')
    subplot(2,5,3)
    imshow(x)
    title('Imagen Gray')
        subplot(2,5,4)
        imshow(Im_filtro)
        title('Imagen con fltro')
subplot(2,5,5); 
histogram(Im_filtro,'FaceColor','r')
title('Histograma 1','FontWeight','bold','FontName','Arial Black','Color','Red');

%Plot the Secound image with the Gray and Filter
subplot(2,5,6); 
histogram(b,'FaceColor','m')
title('Histograma Imagen 2','FontWeight','bold','FontName','Arial Black','Color','m'); 
subplot(2,5,7)
imshow(b)
title('Imagen Original 2') 
    subplot(2,5,8)
    imshow(y)
    title('Imagen Gray')
        subplot(2,5,9)
        imshow(Im_filtro2)
        title('Imagen con fltro')
subplot(2,5,10); 
histogram(Im_filtro2,'FaceColor','m')
title('Histograma Imagen con Filtro 2','FontWeight','bold','FontName','Arial Black','Color','m');

 