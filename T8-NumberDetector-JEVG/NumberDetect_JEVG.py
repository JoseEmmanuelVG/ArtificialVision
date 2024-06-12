import cv2
import numpy as np
import tkinter as tk
import tkinter.font as tkFont

# Define the predefined images
# Define the predefined images
imagenes = ['123.jpg', '123Varied.jpg', '123Inverse.jpg', '123Size.jpg']

def process_image(imagen):
    umbral = 150
    img1 = cv2.imread('1.jpg', 0)
    img123 = cv2.imread(imagen, 0)  # Utilizar la imagen seleccionada
    img2 = cv2.imread('2.jpg', 0)
    img3 = cv2.imread('3.jpg', 0)
    img4 = cv2.imread('4.jpg', 0)

 
    _, img1_umbral = cv2.threshold(img1, umbral, 255, cv2.THRESH_BINARY_INV)
    _, img123_umbral = cv2.threshold(img123, umbral, 255, cv2.THRESH_BINARY_INV)
    _, img2_umbral = cv2.threshold(img2, umbral, 255, cv2.THRESH_BINARY_INV)
    _, img3_umbral = cv2.threshold(img3, umbral, 255, cv2.THRESH_BINARY_INV)
    _, img1_umbral = cv2.threshold(img1, umbral, 255, cv2.THRESH_BINARY_INV)
    _, img123_umbral = cv2.threshold(img123, umbral, 255, cv2.THRESH_BINARY_INV)
    _, img2_umbral = cv2.threshold(img2, umbral, 255, cv2.THRESH_BINARY_INV)
    _, img3_umbral = cv2.threshold(img3, umbral, 255, cv2.THRESH_BINARY_INV)


    contornos1, _ = cv2.findContours(img1_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contornos2, _ = cv2.findContours(img2_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contornos3, _ = cv2.findContours(img3_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contorno1 = contornos1[0]
    contorno2 = contornos2[0]
    contorno3 = contornos3[0]

    contornos123, _ = cv2.findContours(img123_umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contador1 = 0
    contador2 = 0
    contador3 = 0

    for contorno in contornos123:
        match1 = cv2.matchShapes(contorno1, contorno, cv2.CONTOURS_MATCH_I1, 0.0)
        match2 = cv2.matchShapes(contorno2, contorno, cv2.CONTOURS_MATCH_I1, 0.0)
        match3 = cv2.matchShapes(contorno3, contorno, cv2.CONTOURS_MATCH_I1, 0.0)

        if match1 < 0.2:
            contador1 += 1
        elif match2 < 0.3:
            contador2 += 1
        elif match3 < 0.9:
            contador3 += 1

    # Convertir la imagen a color para poder agregar texto en color
    img123_color = cv2.cvtColor(img123, cv2.COLOR_GRAY2BGR)

    # Agregar el conteo de cada número a la imagen
    cv2.putText(img123_color, "Conteo de 1s: " + str(contador1), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(img123_color, "Conteo de 2s: " + str(contador2), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(img123_color, "Conteo de 3s: " + str(contador3), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
  
    signature_text = 'JEVG'
    cv2.putText(img123_color, signature_text, (img123_color.shape[1] - 200, img123_color.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (250, 0,0), 2)

    # Mostrar la imagen con el conteo de números
    cv2.imshow('Conteo de números', img123_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Create a Tkinter window
root = tk.Tk()

# Configure the source
fontsize = 17
font = tkFont.Font(family='Helvetica', size=fontsize)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create a button for each image
for imagen in imagenes:
    button = tk.Button(button_frame, text=imagen, font=font, command=lambda img=imagen: process_image(img))
    button.pack(side=tk.LEFT)

# Starting the Tkinter event loop
root.mainloop()


