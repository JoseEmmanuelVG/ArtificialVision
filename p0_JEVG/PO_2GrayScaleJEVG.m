%Clean the window and data
clc, clear
close all;
%Read the image and aply gray and 
Img_rgb=imread("FiguresImage.jpg");
Img_gray=rgb2gray(Img_rgb);
%Plot the images in the same figure
figure
subplot(1,2,1)
imshow(Img_rgb)
subplot(1,2,2)
imshow(Img_gray)
[n,m]=size(Img_gray);
Img_gray_copy(300:400,300:400)=0;
%figure
%imshow(Img_gray_copy)

figure
Histo=histogram(Img_gray);

for i=1:n
    for j=1:m
        if Img_gray(i,j)>=180 %&& Img_gray(i,j)<20
           Img_gray_copy(i,j)=0;
        else
        Img_gray_copy(i,j)=255;
        end
    end
end

figure
imshow(Img_gray_copy)

