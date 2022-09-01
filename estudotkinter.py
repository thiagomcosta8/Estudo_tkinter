from tkinter import *
from Coordenadas import Coordenadas

class Tela(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.canvas = Canvas(self, width=500, height=500, background="black")
        self.xsb = Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,10000,10000))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Mouse
        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<ButtonRelease-1>", self.Clicou)
        self.canvas.bind("<B1-Motion>", self.scrool_restart) 
        self.canvas.bind("<ButtonPress-3>", self.zoomOut)
        self.canvas.bind("<B3-Motion>", self.scroll_move)    
        #linux scroll
        self.canvas.bind("<Button-4>", self.zoomerP)
        self.canvas.bind("<Button-5>", self.zoomerM)
        #windows scroll
        self.canvas.bind("<MouseWheel>",self.zoomer)

    #clique do mouse
    def Clicou(self, event):
        print("Clicou: " + str(event.x) + ";" + str(event.y))

    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
        print("Start: " + str(event.x) + ";" + str(event.y))
    
    def scrool_restart(self, event):
        ...

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        print("Move:" + str(event.x) + ";" + str(event.y))

    #zomm out
    def zoomOut(self, event):
        self.canvas.scale("all", event.x, event.y, 0.9, 0.9)

    #windows zoom
    def zoomer(self,event):
        if (event.delta > 0):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif (event.delta < 0):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    #linux zoom
    def zoomerP(self,event):
        self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    def zoomerM(self,event):
        self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

if __name__ == "__main__":
    coord = Coordenadas()
    root = Tk()
    img = Tela(root)
    img.pack(fill="both", expand=True)
    img.canvas.create_line(10, 10, 100, 100, fill="red")

    for i in range(10000):
        img.canvas.create_line(coord.inicio[i,0], coord.inicio[i,1], coord.fim[i,0], coord.fim[i,1], fill="white")
    root.mainloop()

