import cv2
import os
import time
import mediapipe as mp
import numpy as np
import tkinter as tk
import tkinter.font as tkFont

# Definir rangos de colores
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
lower_green = np.array([50, 50, 120])
upper_green = np.array([70, 255, 255])
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# Crear variables para controlar el color detectado previamente
prev_color = None

# Definir un umbral de color
color_threshold = 0.03

mp_face_detection = mp.solutions.face_detection
LABELS = ["Cubrebocas Puesto", "Pongase el Cubrebocas"]
face_mask = cv2.face.LBPHFaceRecognizer_create()
face_mask.read("Cubrebocas_Modelo.xml")

brillo_actual = 0
tono_actual = 0

num_sin_cubrebocas = 0
num_con_cubrebocas = 0
last_update = time.time()

cap = None

# Creamos una función que procesará las imagenes/video
def process_image(image_path):
    global cap
    if image_path.endswith('.jpg') or image_path.endswith('.png'):
        # Para imágenes estáticas, usamos cv2.imread
        img = cv2.imread(image_path)
        process_frame(img)
    elif image_path.endswith('.mp4') or image_path.endswith('.avi'):
        # Para vídeos, usamos cv2.VideoCapture
        cap = cv2.VideoCapture(image_path)
        process_video()
    else:
        # Si no es ni una imagen ni un video, asumimos que es la cámara en vivo
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        process_video()

# Creamos una función que procesará cada frame del video
def process_video():
    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            process_frame(frame)

# Creamos una función que manejará cada frame
def process_frame(frame):
    # Aquí va todo tu código que procesa los frames
    brillo_actual = 0
tono_actual = 0

num_sin_cubrebocas = 0
num_con_cubrebocas = 0
last_update = time.time()  # Añade esto

def incrementa_brillo(brillo):
    global brillo_actual
    brillo_actual = brillo

def incrementa_Tono(tono):
    global tono_actual
    tono_actual = tono

cv2.namedWindow('Camara Detectora', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Brillo', 'Camara Detectora', 0, 255, incrementa_brillo)
cv2.createTrackbar('Tono', 'Camara Detectora', 0, 180, incrementa_Tono)

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    
    while True:
        ret, frame = cap.read()
        if ret == False: break

        # Convertir el marco a HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        
        # Cambiar el brillo
        limite = 255 - brillo_actual
        v[v > limite] = 255
        v[v <= limite] += brillo_actual
        
        # Cambiar el tono
        limite = 180 - tono_actual
        h[h > limite] = 180
        h[h <= limite] += tono_actual
        
        # Combinar de nuevo los canales y convertir a BGR
        hsv = cv2.merge((h, s, v))
        frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        
        #VOLTEAR LA CAMARA
        #frame = cv2.flip(frame, 1)
        
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)
        
        if results.detections is not None:
            for detection in results.detections:
                xmin = int(detection.location_data.relative_bounding_box.xmin * width)
                ymin = int(detection.location_data.relative_bounding_box.ymin * height)
                w = int(detection.location_data.relative_bounding_box.width * width)
                h = int(detection.location_data.relative_bounding_box.height * height)
                if xmin < 0 and ymin < 0:
                    continue
                
                face_image = frame[ymin:ymin + h, xmin:xmin + w]
                
                gray_face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
                gray_face_image = cv2.resize(gray_face_image, (72,72), interpolation=cv2.INTER_CUBIC)

                result = face_mask.predict(gray_face_image)

                hsv_face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2HSV)
                mask_red = cv2.inRange(hsv_face_image, lower_red, upper_red)
                mask_green = cv2.inRange(hsv_face_image, lower_green, upper_green)


                num_red_pixels = cv2.countNonZero(mask_red)
                num_green_pixels = cv2.countNonZero(mask_green)
                num_blue_pixels = cv2.countNonZero(mask_red) # Agreagado reciente

                
                color_detected = None
                if num_red_pixels > color_threshold * face_image.size:
                    color_detected = 'red'
                elif num_green_pixels > color_threshold * face_image.size:
                    color_detected = 'green'
                elif num_green_pixels > color_threshold * face_image.size:
                    color_detected = 'blue'   # Agreagado reciente
                
                if result[1] < 150:
                    color = (0, 255, 0) if LABELS[result[0]] == "Cubrebocas Puesto" else (0,0,255)
                    cv2.putText(frame, "{}".format(LABELS[result[0]]), (xmin, ymin - 25), 2, 1, color, 1, cv2.LINE_AA)
                    cv2.circle(frame, (xmin+w//2, ymin+h//2), max(w//2, h//2), color, 2) # circle instead of rectangle

                    if time.time() - last_update > 5 and color_detected != prev_color:  # Añade esta verificación
                        last_update = time.time()  # Actualiza el tiempo de la última actualización
                        prev_color = color_detected
                        if LABELS[result[0]] == "Cubrebocas Puesto":
                            num_con_cubrebocas += 1
                        else:
                            num_sin_cubrebocas += 1

        # PUT TEXT
        cv2.putText(frame, "Sistemas de Vision Artificial 4MM10", (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, "Alumnos: E.A.C.P; C.A.SJ.P & J.E.V.G", (frame.shape[1] - 200, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, "DETECTOR DE ROSTRO CON CUBREBOCAS EN TIEMPO REAL", (frame.shape[1] // 2 - 200, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, "Personas sin cubrebocas en cuadro: {}".format(num_sin_cubrebocas), (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, "Personas con cubrebocas en cuadro: {}".format(num_con_cubrebocas), (frame.shape[1] - 210, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1, cv2.LINE_AA)

        # MUESTRA LA VENTANA CON LA CAMARA Y EL DETECTOR
        cv2.imshow("Camara Detectora", frame)
        if cv2.waitKey(1) == 27:    # 27 es el código ASCII para 'ESC' cierra el programa cuando se presiona
            break
    pass

root = tk.Tk()
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=10)

font = tkFont.Font(family='Helvetica', size=15, weight='bold')

# Botones para las imagenes, videos y camara en vivo
opciones = ['Imagen1.jpg', 'Imagen2.jpg', 'video.mp4', 'Camara en vivo']
for opcion in opciones:
    button = tk.Button(button_frame, text=opcion, font=font, command=lambda img=opcion: process_image(img))
    button.pack(side=tk.LEFT)

root.mainloop()

cap.release()
cv2.destroyAllWindows()