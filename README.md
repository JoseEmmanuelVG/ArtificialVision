# Artificial Vision


## Computer Vision Histogram

### Histograms
A histogram is a function that presents an image with its different grayscale levels.

These are a graphical representation of the values of all the pixels in the image. On the x-axis, it starts with the value 0 corresponding to black, and on the right, the maximum value corresponding to white is represented. If the image is in color, the histograms of the three values for red, green, and blue are shown. The histogram allows us to analyze the image based on grayscale distribution; values close to 0 indicate a dark image, whereas values close to the maximum value indicate a light image. Furthermore, if the range of histogram values is large, the image will have high contrast; if small, the contrast will be low. It also allows us to differentiate the number of objects and their sizes.

### Image Discretization
The histogram of an image with grayscale levels in the range [0, L-1] is a discrete function p(rk) = nk/n, where rk is the k-th grayscale level, nk is the number of pixels in the image at that grayscale level, n is the total number of pixels in the image, and k = 0,1,2..., L-1. In general, p(rk) provides an idea of the probability value that the grayscale level rk will appear. The graphical representation of this function for all k values offers a global description of an image's appearance.

### Matlab Histogram Properties

Histogram properties control the appearance and behavior of the histogram. By changing property values, you can modify various aspects of the histogram. Use dot notation to refer to a particular object and property:

```matlab
h = histogram(randn(10,1));
c = h.BinWidth;
h.BinWidth = 2;
```

- [counts,binLocations] = imhist(I) calculates the histogram for the grayscale image I. The function imhist returns histogram counts and bin locations. The histogram's number of bins is determined by the image type.
- [counts,binLocations] = imhist(I,n) specifies the number of bins, n, used to calculate the histogram.
- [counts,binLocations] = imhist(X,cmap) calculates the histogram for the indexed image X with the color map cmap. The histogram has a bin for each entry in the color map.
imhist(___) displays a histogram plot. If the input image is an indexed image, the histogram shows pixel value distribution over a color bar of the color map cmap.

## References
- Clericus, S. P. (2006). “Visión Artificial: Análisis Teórico del Tratamiento Digital de Imágenes Para su aplicación en la identificación de objetos.”. Universidad Austral de Chile, - Valdivia.
- Matlab. (2023).
-- Histogram Properties - imhist
Plot histogram without using matlab hist() function
MATLAB Graphics Chart Primitive Histogram Properties
- PETISCO, B. B. (2022). Introducción a la Visión Artificial: Procesos y Aplicaciones. UNIVERSIDAD COMPLUTENSE DE MADRID, Madrid.



<p align="center">
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
</p>


