# Final Project of the Artificial Vision course

## First steps
A pre-trained model was applied to detect people and assess whether they are wearing face masks. This approach is common in computer vision tasks and can be useful in a variety of applications, such as safety monitoring, regulatory compliance, and disease prevention. 
In our case the use would be to predict and report if a person was not wearing a mouthpiece. 

### Mask Detection with OpenCV and Python

In this tutorial, Gabriela Solano, the creator and administrator of OMES, shows you how to build your own mask detector quickly and easily. You can find the instructions and base code on [YouTube](https://omes-va.com/deteccion-mascarilla-opencv-python/).

#### Overview

This tutorial covers:
- Detecting if a person is wearing a mask
- Dataset preparation
- Model training
- Testing the model

#### Prerequisites

Ensure you have the following Python libraries installed:
- Numpy
- OpenCV
- MediaPipe

#### 1. Dataset

The dataset consists of two classes: images of faces with masks and images of faces without masks. These images are obtained by applying face detection with MediaPipe and resizing them to a specific height and width. 

Access the dataset on GitHub: [Mask Dataset](https://github.com/GabySol/OmesTutorials2021/tree/main/Mascarillas%20dataset).

#### 2. Training the Model

The model is trained using the Local Binary Patterns Histogram (LBPH) Face Recognizer, which is commonly used for facial recognition. Below is the script used for training, named `train.py`:

```python
import cv2
import os
import numpy as np

dataPath = ".../Dataset_faces"
dir_list = os.listdir(dataPath)
print("Lista archivos:", dir_list)

labels = []
facesData = []
label = 0

for name_dir in dir_list:
    dir_path = dataPath + "/" + name_dir
    for file_name in os.listdir(dir_path):
        image_path = dir_path + "/" + file_name
        print(image_path)
        image = cv2.imread(image_path, 0)
        facesData.append(image)
        labels.append(label)
    label += 1

print("Etiqueta 0: ", np.count_nonzero(np.array(labels) == 0))
print("Etiqueta 1: ", np.count_nonzero(np.array(labels) == 1))

# LBPH FaceRecognizer
face_mask = cv2.face.LBPHFaceRecognizer_create()

# Training
print("Entrenando...")
face_mask.train(facesData, np.array(labels))

# Save model
face_mask.write("face_mask_model.xml")
print("Modelo almacenado")
```

#### 3. Testing the Model

The trained model is tested using a script named `test_face_mask.py`. This script applies face detection to the input images, converts them to grayscale, and resizes them before making predictions with the LBPH Face Recognizer.

```python
import cv2
import os
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
LABELS = ["Con_mascarilla", "Sin_mascarilla"]

# Load the model
face_mask = cv2.face.LBPHFaceRecognizer_create()
face_mask.read("face_mask_model.xml")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while True:
        ret, frame = cap.read()
        if ret == False: break
        frame = cv2.flip(frame, 1)
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
                face_image = frame[ymin: ymin + h, xmin: xmin + w]
                face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
                face_image = cv2.resize(face_image, (72, 72), interpolation=cv2.INTER_CUBIC)
                
                result = face_mask.predict(face_image)
                if result[1] < 150:
                    color = (0, 255, 0) if LABELS[result[0]] == "Con_mascarilla" else (0, 0, 255)
                    cv2.putText(frame, "{}".format(LABELS[result[0]]), (xmin, ymin - 15), 2, 1, color, 1, cv2.LINE_AA)
                    cv2.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), color, 2)
        cv2.imshow("Frame", frame)
        k = cv2.waitKey(1)
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
```

## Next Step
My Schoolmates, C. P. Edder Alexis and S.J. P. Christian Alexis, made modifications to the original script to better suit their specific course and project requirements "Proyecto Detector SVA.py". They added author credits and a project title, changed the labels from "Con_mascarilla" and "Sin_mascarilla" to "Cubrebocas Puesto" and "Pongase el Cubrebocas", and renamed the model file to "Cubrebocas_Modelo.xml". Additionally, they included comments to indicate specific actions, adjusted the text display position, and changed the window name to "Camara Detectora". These changes, along with minor adjustments for clarity, reflect a customized approach to the initial script.


# Final Steps and Aportation 

While my Schoolmates made adjustments to the original script, these changes did not fully demonstrate the concepts learned during the course. Therefore, from this point forward, I have implemented my own adaptations and enhancements to Gabriela Solano's script to improve its adaptability to various environments. Below are the significant improvements I have made [FinalProjectInterface_JEVg.py](https://github.com/JoseEmmanuelVG/ArtificialVision/blob/main/FinalProject_JEVG/FinalProjectInterface_JEVg.py) Script :

### Key Enhancements

1. **Color Detection and Thresholding**:
   - Introduced HSV color space thresholding to detect specific colors (red, green, blue) in the face image. This helps in identifying additional contextual information from the image.

2. **Brightness and Tone Adjustment**:
   - Added trackbars for real-time adjustment of brightness and tone, allowing for better handling of different lighting conditions in the input images.

3. **Enhanced Detection Feedback**:
   - Modified the bounding box from a rectangle to a circle for a more visually distinct marker on detected faces.
   - Implemented a mechanism to count and display the number of people detected with and without masks over time.

4. **Improved User Interface**:
   - Added informative text overlays on the camera feed to provide real-time feedback and context, such as course information, author names, and the number of detections.

5. **Efficiency and Performance**:
   - Included a timing mechanism to ensure updates to the detected color and mask status occur at controlled intervals, reducing unnecessary computations.



## Video Testing and Validation

Video tests were conducted using images under a Creative Commons license, ensuring free use without copyright restrictions. These images included representations of individuals both with and without face masks. This procedure was performed to confirm and validate the correct functionality of the project.
<p align="center">            
<img src="https://github.com/user-attachments/assets/e32f5e1a-87e6-4473-919d-fd13964200bf" width="800" height="400">
</p>


Additionally, variations in brightness and tone metrics were made during the tests. This was done to investigate how these changes might affect detection accuracy in situations where lighting conditions might not be optimal during program execution.

<p align="center">            
<img src="https://github.com/user-attachments/assets/1cd84b9b-c6ee-46dc-983e-6bd6c71ccf1c" width="800" height="400">
</p>


Finally, a comparison was made between images with and without face masks to verify the system's effectiveness. In both test instances, whether through test images or in the classroom via live camera, the expected results were obtained, thereby reaffirming the correct functionality of the implementation.

<p align="center">            
<img src="https://github.com/user-attachments/assets/46b419a0-5948-491d-af6e-b6f087d29a08" width="600" height="300">
<img src="https://github.com/user-attachments/assets/d75487e6-6e77-4fe6-ba90-40102645117e" width="600" height="300">
</p>









<details>
  <summary> <H1> 🌟 Did you find any repository useful? </H1></summary>
  If any project has been helpful to you, consider giving it a ⭐ star in the repository and follow my GitHub account to stay tuned for future updates! 🚀

  In addition, I am always open to suggestions, recommendations or collaborations. Feel free to [get in touch](https://www.linkedin.com/in/vazquez-galan-jose-emmanuel-664968221) if you have any questions or ideas for improving this project. I'm excited for your feedback and contributions.

  Thank you for your interest and support! 😊
</details>


<p align="center">
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
</p>
