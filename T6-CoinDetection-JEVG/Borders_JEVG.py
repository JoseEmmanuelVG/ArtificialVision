#Make a contour detector using cv.findContours(), cv.drawContours(), 
#making the threshold value interactive using a scrollbar (createTrackbar()). JEVG

#Libraries 
import cv2 as cv

# HSV Control & Contour locate
Img = cv.imread('Coins.png', 1)
img_original = Img.copy()

# Add title
titulo = "Control HSV (Brillo, Tono) y Umbral"
fuente_titulo = cv.FONT_HERSHEY_SIMPLEX; tamaño_titulo = 0.6; color_titulo = (0, 0, 255)
grosor_titulo = 2; posicion_titulo = (70, 20)
cv.putText(img_original, titulo, posicion_titulo, fuente_titulo, tamaño_titulo, color_titulo, grosor_titulo)

# Añadir firma
firma = "JEVG"
fuente_firma = cv.FONT_HERSHEY_SIMPLEX; tamaño_firma = 0.6; color_firma = (0, 255, 0)
grosor_firma = 2; posicion_firma = (10, img_original.shape[0] - 10)
cv.putText(img_original, firma, posicion_firma, fuente_firma, tamaño_firma, color_firma, grosor_firma)

cv.namedWindow('Imagenes', cv.WINDOW_NORMAL)

# Initialize the global variables
brillo_actual = 0
tono_actual = 0
umbral = 0

# DEFINE BIOS FUNCTION
def incrementa_brillo(brillo):
    global img_original, brillo_actual  # Add a global variable for BIOS
    brillo_actual = brillo  # Update the Bios

    img = img_original.copy()

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)

    limite = 255 - brillo
    v[v > limite] = 255
    v[v <= limite] += brillo

    # apply the tone 
    limite = 180 - tono_actual
    h[h > limite] = 180
    h[h <= limite] += tono_actual

    hsv = cv.merge((h, s, v))
    img = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

# Contour detector using cv.findContours(), cv.drawContours(), 
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, img_binary = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY_INV)
    contornos, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.drawContours(img, contornos, -1, (0, 255, 255), 3)
    img_binary_color = cv.cvtColor(img_binary, cv.COLOR_GRAY2BGR)  
    img_concatenada = cv.hconcat([img, img_binary_color])  # Concatenate 2 images horizontally

    cv.imshow('Imagenes', img_concatenada)

# Define the Tone Function
def incrementa_Tono(tono):
    global img_original, tono_actual, brillo_actual  # # Add a global variable for Tone
    tono_actual = tono  # Update the Tone

    img = img_original.copy()

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)

    # Aplicamos el brillo aquí también
    limite = 255 - brillo_actual
    v[v > limite] = 255
    v[v <= limite] += brillo_actual

    limite = 180 - tono
    h[h > limite] = 180
    h[h <= limite] += tono

    hsv = cv.merge((h, s, v))
    img = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

# Contour detector using cv.findContours(), cv.drawContours(), 
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, img_binary = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY_INV)
    contornos, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.drawContours(img, contornos, -1, (0, 255, 255), 3)
    img_binary_color = cv.cvtColor(img_binary, cv.COLOR_GRAY2BGR)  
    img_concatenada = cv.hconcat([img, img_binary_color])  # Concatenate 2 images horizontally

    cv.imshow('Imagenes', img_concatenada)
    
# Threshold and edge detection implemented
def incrementa_Umbral(new_umbral):
    global umbral, img_original, brillo_actual, tono_actual
    umbral = new_umbral
    img = img_original.copy()

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)

    # Apply the Bios
    limite = 255 - brillo_actual
    v[v > limite] = 255
    v[v <= limite] += brillo_actual

    # Also apply the tone
    limite = 180 - tono_actual
    h[h > limite] = 180
    h[h <= limite] += tono_actual

    hsv = cv.merge((h, s, v))
    img = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# Contour detector using cv.findContours(), cv.drawContours(), 
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, img_binary = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY_INV)
    contornos, _ = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.drawContours(img, contornos, -1, (0, 255, 255), 3)

    img_binary_color = cv.cvtColor(img_binary, cv.COLOR_GRAY2BGR)  # Convert t o Binary
    img_concatenada = cv.hconcat([img, img_binary_color])  # Concatenate 2 images horizontally

    cv.imshow('Imagenes', img_concatenada)

# Add the sladers
cv.createTrackbar('Brillo', 'Imagenes', 0, 255, incrementa_brillo)
cv.createTrackbar('Tono', 'Imagenes', 0, 180, incrementa_Tono)
cv.createTrackbar('Umbral', 'Imagenes', 0, 255, incrementa_Umbral)

cv.waitKey(0)
cv.destroyAllWindows()
