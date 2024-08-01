# Vázquez Galán José Emmanuel
# Sistemas de Vision Artificial 4MM10
# PROYECTO: DETECTOR DE ROSTRO CON CUBREBOCAS EN TIEMPO REAL
# Referencia: https://omes-va.com/deteccion-mascarilla-opencv-python/
# https://github.com/GabySol/OmesTutorials2021/tree/main/Mascarillas%20dataset

import cv2
import os
import time
import mediapipe as mp
import numpy as np
import threading
import tkinter as tk

num_sin_cubrebocas = 0
num_con_cubrebocas = 0

def increment_sin_cubrebocas():
    global num_sin_cubrebocas
    num_sin_cubrebocas += 1

def decrement_sin_cubrebocas():
    global num_sin_cubrebocas
    num_sin_cubrebocas -= 1

def increment_con_cubrebocas():
    global num_con_cubrebocas
    num_con_cubrebocas += 1

def decrement_con_cubrebocas():
    global num_con_cubrebocas
    num_con_cubrebocas -= 1

def run_tkinter():
    root = tk.Tk()

    button_sin_cubrebocas_up = tk.Button(root, text="Sin Cubrebocas +", command=increment_sin_cubrebocas)
    button_sin_cubrebocas_down = tk.Button(root, text="Sin Cubrebocas -", command=decrement_sin_cubrebocas)
    button_con_cubrebocas_up = tk.Button(root, text="Con Cubrebocas +", command=increment_con_cubrebocas)
    button_con_cubrebocas_down = tk.Button(root, text="Con Cubrebocas -", command=decrement_con_cubrebocas)

    button_sin_cubrebocas_up.pack()
    button_sin_cubrebocas_down.pack()
    button_con_cubrebocas_up.pack()
    button_con_cubrebocas_down.pack()

    root.mainloop()

tkinter_thread = threading.Thread(target=run_tkinter)
tkinter_thread.start()

# Define color ranges
lower_red = np.array([0, 50, 50]) 
upper_red = np.array([10, 255, 255])
lower_green = np.array([50, 50, 120]) 
upper_green = np.array([70, 255, 255])

# Create variables to control the previously detected color
prev_color = None

# Define a color threshold
color_threshold = 0.05

mp_face_detection = mp.solutions.face_detection
LABELS = ["Cubrebocas Puesto", "Pongase el Cubrebocas"]
face_mask = cv2.face.LBPHFaceRecognizer_create()
face_mask.read("Cubrebocas_Modelo.xml")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

brillo_actual = 0
tono_actual = 0
last_update = time.time()  # Add this

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
        brillo = cv2.getTrackbarPos('Brillo', 'Camara Detectora')
        tono = cv2.getTrackbarPos('Tono', 'Camara Detectora')
        frame = cv2.add(frame, np.array([brillo, tono, 0]))
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)

        if results.detections:
            for detection in results.detections:
                x, y, w, h = detection.location_data.relative_bounding_box.xmin, detection.location_data.relative_bounding_box.ymin, \
                             detection.location_data.relative_bounding_box.width, detection.location_data.relative_bounding_box.height
                h, w, _ = frame.shape
                min_x = int(x * w)
                min_y = int(y * h)
                max_x = int((x * w) + (w * w))
                max_y = int((y * h) + (h * h))
                rostro = frame[min_y:max_y, min_x:max_x]
                gray = cv2.cvtColor(rostro, cv2.COLOR_BGR2GRAY)
                label, confidence = face_mask.predict(gray)

                if confidence < 100:
                    confidence = f"  {round(100 - confidence)}"
                    label_text = LABELS[label]
                    if label == 1:
                        increment_sin_cubrebocas()
                    else:
                        increment_con_cubrebocas()
                else:
                    label_text = "No Cubrebocas"
                    increment_sin_cubrebocas()

                # Add color detection here
                hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
                green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)
                red_pixels = np.sum(red_mask) / 255
                green_pixels = np.sum(green_mask) / 255

                if red_pixels > color_threshold and prev_color != 'red':
                    increment_con_cubrebocas()
                    prev_color = 'red'

                elif green_pixels > color_threshold and prev_color != 'green':
                    increment_sin_cubrebocas()
                    prev_color = 'green'
                else:
                    prev_color = None
        else:
            increment_sin_cubrebocas()

        cv2.imshow('Camara Detectora', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
