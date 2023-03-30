%% Clear the window and data
clc, clear
close all;

%% Read the image, figure and aply the Max 
x=imread("DogsImage.png");
x2=rgb2gray(x);
Max_x2=max(max(x2));
Min_x2=max(max(x2));

%% Function to work
[N,M]=size(image2);
for i=1:N
    for j=1:M



%% Plot the images in the same figure
figure
subplot(1,2,1)
imshow(x)
subplot(1,3,2)
imshow(x2)
subplot(1,3,3)
imshow(x3)