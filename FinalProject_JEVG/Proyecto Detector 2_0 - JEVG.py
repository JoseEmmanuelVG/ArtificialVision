# Vázquez Galán José Emmanuel
# Sistemas de Vision Artificial 4MM10
# PROYECTO: DETECTOR DE ROSTRO CON CUBREBOCAS EN TIEMPO REAL
# Referencia: https://omes-va.com/deteccion-mascarilla-opencv-python/
# https://github.com/GabySol/OmesTutorials2021/tree/main/Mascarillas%20dataset

import cv2
import os
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
LABELS = ["Cubrebocas Puesto", "Pongase el Cubrebocas"]
face_mask = cv2.face.LBPHFaceRecognizer_create()
face_mask.read("Cubrebocas_Modelo.xml")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

brillo_actual = 0
tono_actual = 0

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
                face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
                face_image = cv2.resize(face_image, (72,72), interpolation=cv2.INTER_CUBIC)
                
                result = face_mask.predict(face_image)
                
                if result[1] < 150:
                    color = (0, 255, 0) if LABELS[result[0]] == "Cubrebocas Puesto" else (0,0,255)
                    cv2.putText(frame, "{}".format(LABELS[result[0]]), (xmin, ymin - 25), 2, 1, color, 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), color, 2)
        
        # MUESTRA LA VENTANA CON LA CAMARA Y EL DETECTOR
        cv2.imshow("Camara Detectora", frame)
        if cv2.waitKey(1) == 27:    # 27 es el código ASCII para 'ESC'
            break

cap.release()
cv2.destroyAllWindows()