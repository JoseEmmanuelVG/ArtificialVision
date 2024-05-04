%% Clean the window and data
clc, clear
close all;

%% Read the image and work with the size and gray
Im_Origin=imread('DogBlack.png');

%% Operations to the  Filter 
Im_Origin_Ruido= Im_Origin;
[n,m]=size(Im_Origin);
for v=1:1000
    x=round(rand*n);
    y=round(rand*m);
    if x==0
        x=1;
    end
    if y==0
        y=1;
    end  
    if x==n
        x= n-1;
    end
    if y==m
        y= m-1;
    end
    
   Im_Origin_Ruido(x,y)=255;
   Im_Origin_Ruido(x:x+2,y:y+2)=255;    
end

for v=1:1000
    x=round(rand*n);
    y=round(rand*m);
    if x==0
        x=1;
    end
    if y==0
        y=1;
    end  
    if x==n
        x= n-1;
    end
    if y==m
        y= m-1;
    end
    
   Im_Origin_Ruido(x,y)=0;
   Im_Origin_Ruido(x:x+2,y:y+2)=0;    
end

ColorMin=min(Im_Origin_Ruido(x,y));


%% Plot the images in the same figure
Fig = figure('Name', 'T5. Max - Min - Sal y Pimienta JEVG');
set(Fig, 'Position', [0 0 1400 1400])
%Original and Gray image
subplot(2,2,1)
imshow(Im_Origin_Ruido)
imwrite(Im_Origin_Ruido, 'Im_Origin_Ruido.jpg', 'jpg')
subplot(2,2,2)
Imagen_Matlab=imnoise(Im_Origin, 'salt & pepper', 0.02);
imshow(Imagen_Matlab)
title("Funcion MATLAB")

subplot(2,2,4)
imshow(I_min)
title("Funcion MATLAB")
    subplot(2,2,3)
    imshow(I_max)
    title("Funcion MATLAB")
