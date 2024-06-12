import cv2 as cv

# Umbral fijo
umbral = 125
# Leer la imagen
Img = cv.imread('Coins.png',1)
Img_copy=Img.copy()

# Convertir a escala de grises
img_gray=cv.cvtColor(Img,cv.COLOR_BGR2GRAY)

def Imagen_Binaria(umbral):
    global img_umbral
    _,img_umbral=cv.threshold(img_gray,umbral,255,cv.THRESH_BINARY_INV)
    cv.imshow("Imagen Binaria",img_umbral)

def Contornos():
    Contornos, _ = cv.findContours(img_umbral, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

    # Definir rangos de área para diferentes tipos de monedas
    moneda_1 = [75, 100]
    moneda_2 = [150, 200]
    moneda_3 = [700, 750]
    moneda_4 = [600, 700]
    moneda_5 = [250, 500]

    num_monedas = [0, 0, 0, 0, 0]  # Contador para cada tipo de moneda

    for contorno in Contornos:
        area = cv.contourArea(contorno)

        # Comprobar en qué rango de área cae cada contorno y aumentar el contador correspondiente
        if moneda_1[0] < area < moneda_1[1]:
            num_monedas[0] += 1
        elif moneda_2[0] < area < moneda_2[1]:
            num_monedas[1] += 1
        elif moneda_3[0] < area < moneda_3[1]:
            num_monedas[2] += 1
        elif moneda_4[0] < area < moneda_4[1]:
            num_monedas[3] += 1
        elif moneda_5[0] < area < moneda_5[1]:
            num_monedas[4] += 1

    Img = Img_copy.copy()
    cv.drawContours(Img, Contornos, -1, (0, 255, 255), 3)
    
    # Añadir texto a la imagen con el número de monedas para cada tipo
    fuente = cv.FONT_HERSHEY_SIMPLEX
    color = (0, 0, 255)  # color rojo
    grosor = 2
    for i, num in enumerate(num_monedas):
        cv.putText(Img, 'Monedas de tipo {}: {}'.format(i+1, num), (10, 50 + i*50), fuente, 0.7, color, grosor, cv.LINE_AA)
    cv.imshow("Contorno", Img)

def Actualizar_imagen(umbral):
    Imagen_Binaria(umbral)
    Contornos()

# Llama a la función con el umbral fijo
Actualizar_imagen(umbral)

cv.waitKey(0)
cv.destroyAllWindows()


