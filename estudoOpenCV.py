import numpy as np
import cv2
import time
from Coordenadas import Coordenadas

coord = Coordenadas();
for j in range(10):
    tempoInicio = time.time()
    img = np.zeros((10000,10000,3))
    for i in range(10000):
        cv2.line(img, coord.inicio[i], coord.fim[i], (255,255,255), 1)
    cv2.imshow("Img", img)
    tempoTotal = time.time()-tempoInicio
    print("Tempo do OpenCV: ",tempoTotal)
    cv2.waitKey(0)