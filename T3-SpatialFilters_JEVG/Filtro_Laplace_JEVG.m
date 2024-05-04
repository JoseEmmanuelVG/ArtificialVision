%% Clean the window and data
clc, clear
close all;
%% Read the image and work with the size and gray
a = imread('Lamborghini.jpg');
x = rgb2gray(a);
% Channge to doble and get the size of the image
[m,n]=size(x);
Im=double(x);
[o,p]=size(a);
Im2=double(a);

%% Operations to the Spacial Filter 
                    % Laplace RGB
% Aply a Laplacian Filter to each canal of color RGB and Divide the color canals
red_channel = a(:,:,1);
green_channel = a(:,:,2);
blue_channel = a(:,:,3);
 % kernel Laplacian Filter
kernel = [0 1 0; 
          1 -3.99 1; %Middle value could be change
          0 1 0];
red_channel_filt = imfilter(double(red_channel), kernel, 'symmetric', 'conv');
green_channel_filt = imfilter(double(green_channel), kernel, 'symmetric', 'conv');
blue_channel_filt = imfilter(double(blue_channel), kernel, 'symmetric', 'conv');
% Combine the filter canals to get the final image
Im_FiltLaplace = cat(3, red_channel_filt, green_channel_filt, blue_channel_filt);
% Converti to uint8
Im_FiltLaplace = uint8(Im_FiltLaplace);
                    % Laplace Gray
for r=2:m-1 
    for c=2:n-1
        Im_FiltLaplaceGray(r,c)=sum(sum(Im(r-1:r+1,c-1:c+1)*kernel));
    end
end 
% Converti to uint8
Im_FiltLaplaceGray=uint8(Im_FiltLaplaceGray);

                % Gauss RGB and Gray
% Aply a Gaussian Filter to each canal of color RGB and Divide the color canals
sigma = 3; % it could be chage
hsize = 2 * ceil(3 * sigma) + 1;
H = fspecial('gaussian', hsize, sigma);
red_channel_filt = imfilter(double(red_channel), H, 'symmetric', 'conv');
green_channel_filt = imfilter(double(green_channel), H, 'symmetric', 'conv');
blue_channel_filt = imfilter(double(blue_channel), H, 'symmetric', 'conv');% Combinar los canales filtrados para obtener la imagen final
Im_FiltGauss = cat(3, red_channel_filt, green_channel_filt, blue_channel_filt);
 % Converti to uint8 Gauss RGB
Im_FiltGauss = uint8(Im_FiltGauss); 
    % Create the Convolution Matriz to the gAUSS fILTER Gray
    [X, Y] = meshgrid(-hsize:hsize, -hsize:hsize);
    h = exp(-(X.^2 + Y.^2) / (2*sigma^2)); %Ecuation to create a Gauss Filter
    h = h / sum(h(:));
    % Aply the convolution matrix to the image
    Im_FiltGaussGray = conv2(double(x), h, 'same');
    % Converti to uint8 Gauss Gray
    Im_FiltGaussGray = uint8(Im_FiltGaussGray);



%% Plot the images in the same figure
%Plot the first image with the Gray and Filter
Fig = figure('Name', 'T5. Filtro Gaussiano y Laplace JEVG');
set(Fig, 'Position', [0 0 1400 1400])
%Original and Gray image
subplot(3,4,2)
imshow(a)
title('Imagen Original 1')
subplot(3,4,1); 
histogram(a,'FaceColor','r')
title({'Histograma', 'Imagen Original RGB'}, ...
    'FontWeight', 'bold', 'FontName', 'Arial Black', 'Color', 'Red', ...
    'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle');
    subplot(3,4,3)
    imshow(x)
    title('Imagen Gray')
    subplot(3,4,4); 
    histogram(x,'FaceColor','r')
    title({'Histograma', 'Imagen Gray'}, ...
    'FontWeight', 'bold', 'FontName', 'Arial Black', 'Color', 'Red', ...
    'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle');

%Laplacian Filter
subplot(3,4,5); 
histogram(Im_FiltLaplace,'FaceColor','Green')
title({'Histograma Filtro Laplaciano', 'Imagen Original RGB'}, ...
    'FontWeight', 'bold', 'FontName', 'Arial Black', 'Color', '0.16,0.38,0.27', ...
    'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle');
subplot(3,4,6)
imshow(Im_FiltLaplace)
title('Imagen Original con fltro Laplaciano')
    subplot(3,4,7)
    imshow(Im_FiltLaplaceGray)
    title('Imagen Gray con fltro Laplaciano')
    subplot(3,4,8); 
    histogram(Im_FiltLaplaceGray,'FaceColor','Green')
    title({'Histograma Filtro Laplaciano', 'Imagen Gray'}, ...
    'FontWeight', 'bold', 'FontName', 'Arial Black', 'Color', '0.16,0.38,0.27', ...
    'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle');

%Gaussian Filter
subplot(3,4,9); 
histogram(Im_FiltGauss,'FaceColor','Blue')
title({'Histograma Filtro Gaussiano', 'Imagen Original RGB'}, ...
    'FontWeight', 'bold', 'FontName', 'Arial Black', 'Color', 'Blue', ...
    'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle');
subplot(3,4,10)
imshow(Im_FiltGauss)
title('Imagen Original con fltro Gaussiano')
    subplot(3,4,11)
    imshow(Im_FiltGaussGray)
    title('Imagen Gray con fltro Gaussiano')
    subplot(3,4,12); 
    histogram(Im_FiltGaussGray,'FaceColor','Blue')
    title({'Histograma Filtro Gaussiano', 'Imagen Gray'}, ...
    'FontWeight', 'bold', 'FontName', 'Arial Black', 'Color', 'Blue', ...
    'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle');
% Signature
sgtitle({'Filtro Laplaciano y Gaussiano', 'JEVG'}, 'FontWeight', 'bold', 'HorizontalAlignment', 'center');


    
    
   
 