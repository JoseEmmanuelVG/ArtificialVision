# Import the libraries and add the plot size
import cv2 
import numpy as np
Plot = np.ones((300, 300, 3), np.uint8)*255

# Draw the lines to the plot
for i in range(50, 300, 50):
   cv2.line(Plot, (0, i), (300, i), (0, 0, 255),2)
for j in range(50, 300, 50):
    cv2.line(Plot, (j, 0), (j, 300), (0, 0, 255),2)

# My signature
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(Plot, 'JEVG', (110, 150), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

# Plot the image
cv2.imshow('Imagen', Plot)
cv2.waitKey(0)
cv2.destroyAllWindows()
