import cv2

umbral = 150
img1 = cv2.imread('1.jpg',0)
img123 = cv2.imread('123Inverse.jpg',0)
img2 = cv2.imread('2.jpg',0)
img3 = cv2.imread('3.jpg',0)

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

    if match1 < 0.01:
        contador1 += 1
    elif match2 < 0.01:
        contador2 += 1
    elif match3 < 0.01:
        contador3 += 1

# Convertir la imagen a color para poder agregar texto en color
img123_color = cv2.cvtColor(img123, cv2.COLOR_GRAY2BGR)

# Agregar el conteo de cada número a la imagen
cv2.putText(img123_color, "Conteo de 1s: " + str(contador1), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img123_color, "Conteo de 2s: " + str(contador2), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img123_color, "Conteo de 3s: " + str(contador3), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Mostrar la imagen con el conteo de números
cv2.imshow('Conteo de números', img123_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
