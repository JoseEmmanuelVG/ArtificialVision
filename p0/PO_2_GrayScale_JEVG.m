%Clean the window and data
clc, clear
close all;

Img_rgb=imread("DogColor.png");
Img_gray=rgb2gray(Img_rgb);
figure
subplot(1,2,1)
imshow(Img_rgb)
subplot(1,2,2)
imshow(Img_gray)
[n,m]=size(Img_gray);
Img_gray_copy(300:400,300:400)=0;
figure
imshow(Img_gray_copy)