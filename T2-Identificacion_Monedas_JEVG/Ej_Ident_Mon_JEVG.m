%% Configuracion Inicial
clc; % Borra las entradas a la ventana de comandos
close all; % Cierra todas las ventanas o figuras
Fig = figure('Name', 'Deteccion de una forma especifica en una imagen');
set(Fig, 'Position', [0 0 1000 1000])
imagen_original = imread('Monedas.jpg');
subplot(2, 2, 1)
imshow(imagen_original);

%% Transformacion a una imagen binaria
imagen = rgb2gray(imagen_original);
subplot(2, 2, 2)
imshow(imagen);
umb = graythresh(imagen);
bw = imbinarize(imagen, umb);
subplot(2, 2, 3)
imshow(bw);

%%  Base de datos
subplot(2, 2, 4)
img_final = imfill(bw, 'holes'); % Se rellena los huecos en las moendas
img_final = bwareafilt(img_final, [500 Inf]); % Se hace un filtro para los objetos pequeños e indeseados
Objetos = bwlabel(img_final);
imshow(label2rgb(Objetos));
Propiedades = regionprops(Objetos);

hold on
Areas = zeros(1, length(Propiedades));

for i = 1:length(Propiedades)
    Coordenadas = Propiedades(i).BoundingBox;
    Centro = Propiedades(i).Centroid;
    Areas(i) = Propiedades(i).Area;
    rectangle('Position', Coordenadas, ...
        'EdgeColor', 'r', 'LineWidth', 3)
    x = Centro(1);
    y = Centro(2);
    plot(x, y, '+k');
end

pause
%% Imagen a procesar
close all
Fig = figure('Name', 'Deteccion de una forma especifica en una imagen');
set(Fig, 'Position', [0 0 800 800])
imagen_original = imread('coinsExample.jpg');
subplot(1, 2, 1)
imshow(imagen_original);
imagen = rgb2gray(imagen_original);
umb = graythresh(imagen);
bw = imbinarize(imagen, umb);
img_final = imfill(bw, 'holes');
img_final = bwareafilt(img_final, [500 Inf]);
Objetos = bwlabel(img_final);
subplot(1, 2, 2)
imshow(Objetos);
Propiedades = regionprops(Objetos);

pause
hold on
Error = 150; % Error de área permitido

for i = 1:length(Propiedades)
    Coordenadas = Propiedades(i).BoundingBox;
    Centro = Propiedades(i).Centroid;
    Area = Propiedades(i).Area;
    x = Centro(1);
    y = Centro(2);
    % Detección de monedas
    if ((Area >= Areas(1) - Error) && (Area <= Areas(1) + Error))
        rectangle('Position', Coordenadas, ...
            'EdgeColor', 'r', 'LineWidth', 3)
        plot(x, y, '+r');
    end

    if ((Area >= Areas(2) - Error) && (Area <= Areas(2) + Error))
        rectangle('Position', Coordenadas, ...
            'EdgeColor', 'g', 'LineWidth', 3)
        plot(x, y, '*g');
    end

    if ((Area >= Areas(3) - Error) && (Area <= Areas(3) + Error))
        rectangle('Position', Coordenadas, ...
            'EdgeColor', 'b', 'LineWidth', 3)
        plot(x, y, 'xb');
    end

    if ((Area >= Areas(4) - Error) && (Area <= Areas(4) + Error))
        rectangle('Position', Coordenadas, ...
            'EdgeColor', 'w', 'LineWidth', 3)
        plot(x, y, 'ok');
    end

    if ((Area >= Areas(5) - Error) && (Area <= Areas(5) + Error))
        rectangle('Position', Coordenadas, ...
            'EdgeColor', 'c', 'LineWidth', 3)
        plot(x, y, 'sc');
    end

    if ((Area >= Areas(6) - Error) && (Area <= Areas(6) + Error))
        rectangle('Position', Coordenadas, ...
            'EdgeColor', 'y', 'LineWidth', 3)
        plot(x, y, 'dk');
    end

end