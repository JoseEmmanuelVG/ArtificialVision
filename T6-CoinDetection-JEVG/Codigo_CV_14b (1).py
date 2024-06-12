import cv2 as cv

umbral=140

Img = cv.imread('Coins.jpg',1)

img_gray=cv.cvtColor(Img,cv.COLOR_BGR2GRAY)

_,img_Binary=cv.threshold(img_gray,umbral,255,cv.THRESH_BINARY_INV)

cv.imshow("Imagen Binaria",img_Binary)

Contornos,_=cv.findContours(img_Binary, cv.RETR_EXTERNAL ,cv.CHAIN_APPROX_NONE)
cv.drawContours(Img,Contornos,-1,(0,255,255),3)
cv.imshow("Contronos",Img)

cv.waitKey(0)
cv.destroyAllWindows()

