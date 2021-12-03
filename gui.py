from tkinter import *
from PIL import Image, ImageTk

class Preview:

    def __init__(self, master):
        self.master = master
        self.master.title("Preview")
        self.master.overrideredirect(True)

        self.canvas = Canvas(self.master, width=375, height=667)
        self.canvas.pack()

        self.button = Button(self.master, text="CLOSE", overrelief="solid", width=15, command=self.master.destroy)


    def create(self, image):
        self.img = ImageTk.PhotoImage(image.resize((375, 667), Image.ANTIALIAS))
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=NW, image=self.img)

    def update(self, image):
        self.img = ImageTk.PhotoImage(image.resize((375, 667), Image.ANTIALIAS))
        self.canvas.itemconfig(self.image_on_canvas,image=self.img)

    def show(self, image):
        try:
            self.update(image)
        except AttributeError:
            self.create(image)
    
    def close(self):
        self.button.pack()
