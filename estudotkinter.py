from tkinter import *
import time
from Coordenadas import Coordenadas

coord = Coordenadas();
for j in range(10):
    tempoInicio = time.time()
    root = Tk()
    img = Canvas(root, width=10000, height=10000, bg='black')
    img.pack()
    for i in range(10000):
        img.create_line(coord.inicio[i,0], coord.inicio[i,1], coord.fim[i,0], coord.fim[i,1], fill="white")
    root.mainloop()
    tempoTotal = time.time()-tempoInicio
    print("Tempo do tkInter: ",tempoTotal)
