%Clean the window and data
clc, clear
close all;
    %Read the images and convert to Gray format
    ImgColor=imread('DogsImage.png');
    ImgGray=rgb2gray(ImgColor);
        %Create a vector to the histogram with the ImgColor
        X=zeros(1,256);
        n=0;
        %Sweep the values of the matrix
        for k=1:2:256
             %Reset "n"
             n=0;
             %Se recorre cada celda de la matriz
             for i=1:length(ImgColor(:,1))
                 for j=1:length(ImgColor(1,:))
                 %Count the repite values
                     if (ImgColor(i,j)==k || ImgColor(i,j)==k-1)
                     n=n+1;
                     X(k)=n;
                     end 
                 end
             end
        end
        %Figure to the histphram 
        figure(1);
        
       %Plot the images in the same figure to the ImgColor   
    subplot(2,2,1)
    imshow(ImgColor);
    title(['Imagen a procesar';'a Color'],'FontWeight','bold')
    subplot(2,2,2)
        imshow(ImgColor);
        title(['Imagen a Procesar';'a Color'],'FontWeight','bold')
        subplot(2,2,3)
        bar(X)
        title(['Histograma "ALGORITMO"';'Imagen a Color'],'FontWeight','bold','FontName','Arial Black',...
        'Color','Blue');
    
%Compare with the histtogram function
subplot(2,2,4); 
histogram(ImgColor,'FaceColor','r')
title(['Histograma "HISTOGRAM"';'Imagen a Color'],'FontWeight','bold','FontName','Arial Black',...
    'Color','Red');


        %Create a vector to the histogram with the ImgGray
        Y=zeros(1,256);
        m=0;
        %Sweep the values of the matrix
        for z=1:2:256
             %Reset "n"
             m=0;
             %Se recorre cada celda de la matriz
             for x=1:length(ImgGray(:,1))
                 for y=1:length(ImgGray(1,:))
                 %Count the repite values
                     if (ImgGray(x,y)==z || ImgGray(x,y)==z-1)
                     m=m+1;
                     Y(z)=m;
                     end 
                 end
             end
        end
        %Figure to the histphram 
        figure(2);
        
%Plot the images in the same figure to the ImgGray  
    subplot(2,2,1)
    imshow(ImgGray);
    title(['Imagen a procesar en';'Escala de Grises'],'FontWeight','bold')
    subplot(2,2,2)
        imshow(ImgGray);
        title(['Imagen a Procesa';'en Escala de Grises'],'FontWeight','bold')
        subplot(2,2,3)
        bar(Y)
        title(['Histograma "ALGORITMO"';'Imagen en grises'],'FontWeight','bold','FontName','Arial Black',...
        'Color','Blue');
%Compare with the histtogram function
subplot(2,2,4); 
histogram(ImgGray,'FaceColor','r')
title(['Histograma "HISTOGRAM"';'Imagen en grises'],'FontWeight','bold','FontName','Arial Black',...
    'Color','Red');

