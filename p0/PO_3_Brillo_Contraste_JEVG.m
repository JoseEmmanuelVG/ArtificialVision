%Clean the window and data
clc, clear
close all;
%Put a valor to variables Contrast and the Bias
C=0.1;
B=100;
%Read the image and aply gray and 
x=imread("DogsImage.png");
x2=rgb2gray(x);
x3=x2*C+B;
%Plot the images in the same figure
figure
subplot(1,3,1)
imshow(x)
subplot(1,3,2)
imshow(x2)
subplot(1,3,3)
imshow(x3)


