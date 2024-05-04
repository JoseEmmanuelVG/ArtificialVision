%% Clean the window and data
clc, clear
close all;

%% Read the image and work with the size and gray
Im_Origin=imread('Lamborghini.jpg');

%% Operations to the  Filter 
Imagen_RuidoMatlab=imnoise(Im_Origin, 'salt & pepper', 0.05);
Imagen_Gray = rgb2gray(Imagen_RuidoMatlab); 
% Copy to the Max and Min Filter and 
Imagen_Max = Imagen_Gray;
Imagen_Min = Imagen_Gray;
Dimen_Filt = 3;

% Pixel to Pixel Sweep
for i = 1:size(Imagen_Gray, 1)
    for j = 1:size(Imagen_Gray, 2)
        
        window = Imagen_Gray(max(1, i-floor(Dimen_Filt/2)):min(size(Imagen_Gray, 1), i+floor(Dimen_Filt/2)), ...
            max(1, j-floor(Dimen_Filt/2)):min(size(Imagen_Gray, 2), j+floor(Dimen_Filt/2)));
        
        Imagen_Max(i, j) = max(window(:));
        Imagen_Min(i, j) = min(window(:));
        
    end
end
Imagen_MaxMin= (Imagen_Max + Imagen_Min);

%% Plot the images in the same figure
Fig = figure('Name', 'T6. Max - Min - Sal y Pimienta JEVG');
set(Fig, 'Position', [0 0 1000 1000])
subplot(4,2,1); imshow(Imagen_Gray)
title("Imagen Gray con Ruido")
subplot(4,2,2); histogram(Imagen_Gray,'FaceColor','r')
title(['Histograma Ruido Sal y Pimienta'],'FontWeight','bold','FontName','Arial Black');
    subplot(4,2,3); imshow(Imagen_Max) 
    title('Filtro Max');
    subplot(4,2,4); histogram(Imagen_Max,'FaceColor','blue')
    title(['Histograma Filtro Máximo'],'FontWeight','bold','FontName','Arial Black');
        subplot(4,2,5); imshow(Imagen_Min) 
        title('Filtro Min');
        subplot(4,2,6); histogram(Imagen_Min,'FaceColor','green')
        title(['Histograma Filtro Mínimo'],'FontWeight','bold','FontName','Arial Black');
subplot(4,2,7); imshow(Imagen_RuidoMatlab) 
        title('Imagen Original con Ruido');
subplot(4,2,8); imshow(Imagen_MaxMin) 
        title('Imagen con Ambos Filtros Max-Min');
% Signature
sgtitle({'Quitar ruido sal y pimiento', 'JEVG'}, 'FontWeight', 'bold', 'HorizontalAlignment', 'center');
