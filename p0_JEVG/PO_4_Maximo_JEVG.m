%Clean the window and data
clc, clear
close all;
%Read the image and aply the Max 
x=imread("DogsImage.png");
x2=rgb2gray(x);
Pmax=max(max(x2));
x3=Pmax-x2;
%Plot the images in the same figure
figure
subplot(1,3,1)
imshow(x)
subplot(1,3,2)
imshow(x2)
subplot(1,3,3)
imshow(x3)