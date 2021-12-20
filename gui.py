from tkinter import *
from PIL import Image, ImageTk

class Preview:

    def __init__(self, master, ratio):
        self.master = master
        self.master.title("Preview")
        self.master.overrideredirect(True)
        
        self.ratio = ratio
        if self.ratio >= 1:
            self.horizonal = True
            self.canvas = Canvas(self.master, width=400, height=self.ratio*400)
        else:
            self.horizonal = False
            self.canvas = Canvas(self.master, width=400//self.ratio, height=400)
        self.canvas.pack()

        self.button = Button(self.master, text="CLOSE", overrelief="solid", width=15, command=self.master.destroy)


    def create(self, image):
        if self.horizonal:
            self.img = ImageTk.PhotoImage(image.resize((400, int(self.ratio*400)), Image.ANTIALIAS))
        else:
            self.img = ImageTk.PhotoImage(image.resize((int(400/self.ratio), 400), Image.ANTIALIAS))
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=NW, image=self.img)

    def update(self, image):
        if self.horizonal:
            self.img = ImageTk.PhotoImage(image.resize((400, int(self.ratio*400)), Image.ANTIALIAS))
        else:
            self.img = ImageTk.PhotoImage(image.resize((int(400/self.ratio), 400), Image.ANTIALIAS))
        self.canvas.itemconfig(self.image_on_canvas,image=self.img)

    def show(self, image):
        try:
            self.update(image)
        except AttributeError:
            self.create(image)
    
    def close(self):
        self.button.pack()
