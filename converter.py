from tkinter import *
from PIL import Image
import sys
from matplotlib import colors
import rotate_cursor as rc
from gui import Preview

class Background:

    def __init__(self, image_name):
        self.image = Image.open(f'{image_name}.png').convert('RGBA')  # image to paste
        
        self.background_color = self.image.getpixel((0,0))
        print(f"image size : {self.image.size} / background color : {self.background_color}\n")

        print("Enter size you want to make.")
        print("SD : 750×1334 / HD : 1500x2668 / FHD : 1859x3306 / UHD : 2303x4096")
        self.size = (self.width,self.height) = self.get_size()

        self.root = Tk()
        self.canvas = Preview(self.root)

        self.background = self.set_background(self.image)

    def get_size(self):
        size_dict = {'SD':(750,1334), 'HD':(1500,2668), 'FHD':(1859,3306), 'UHD':(2303,4096)}
        while(True):
            try:
                self.input = sys.stdin.readline().strip().upper()
                if self.input in size_dict:
                    print(f"{self.input}{size_dict[self.input]} selected.\n")
                    return size_dict[self.input]
                else:
                    self.width,self.height = map(int, self.input.split())
                return (self.width,self.height)
            except ValueError:
                print("Unavailable")
            
    def set_background(self, image):
        while(True):
            try:
                print("Set horizonal postion as the ratio(%):",end=' ')
                self.h_ratio = int(input())*0.01
                print("Set vertical position as the ratio(%):",end=' ')
                self.v_ratio = (100 - int(input()))*0.01
                break
            except ValueError:
                print("Unavailable.")
        return self.resize(image,self.h_ratio,self.v_ratio)

    def resize(self, image, h_ratio, v_ratio):
        self.pasted = self.paste(image, h_ratio, v_ratio)
        self.resized = image.copy()
        while(True):
            print("\nWant to resize?(proportion maintained)(Y/N)",end=' ')
            self.yn = input()
            if self.yn == 'y' or self.yn == 'Y':
                print("Enter width ratio(%):",end=' ')  # < 100
                self.ratio = int(input())
                self.wh_ratio = image.height/image.width
                self.image_width = int(self.width * self.ratio * 0.01)
                self.resized = image.resize((self.image_width,int(self.image_width*self.wh_ratio)), Image.ANTIALIAS)
                self.pasted = self.paste(self.resized, h_ratio, v_ratio)
            # elif yn == 'n' or yn == 'N':
            else:
                print("Confirmed")
                return self.pasted

    def get_background_color(self):
        print("\nDo you want to change the background color?(Y/N)",end=' ')
        self.yn = input()
        if self.yn == 'y' or self.yn == 'Y':
            self.change_background()
        # elif yn == 'n' or yn == 'N':
        else:
            print("Okay")

    def change_background(self):
        try:
            print("What color?",end=' ')
            self.color = input()
            self.rgb = tuple(map(mul_255,colors.to_rgba(self.color))) # RGBA using matplotlib
            # rgb = ImageColor.getrgb(color) # RGB using PIL
        except ValueError:
            print("Unavailable color")
            self.change_background()
        else:
            print(self.background_color,'->',self.rgb)
            print("Converting...",end='')
            with rc.Spinner():
                for x in range(0,self.width):
                    for y in range(0,self.height):
                        # if background.getpixel((x,y)) == background_color:
                        if det_range(self.background.getpixel((x,y)),self.background_color) == True:
                            self.background.putpixel((x,y),self.rgb)
                assert(True)                            # stop rotating
                sys.stdout.write('\033[2K\033[1G')      # delete command line
                print("Converted!")
                self.canvas.show(self.background)
                self.root.mainloop()


    def set_position(self, image, h_ratio, v_ratio):
        return (int((self.width - image.width)*h_ratio),int((self.height - image.height)*v_ratio))

    def paste(self, image, h_ratio, v_ratio):
        self.position = self.set_position(image, h_ratio, v_ratio)
        self.background = Image.new(mode='RGBA', size=self.size, color=self.background_color)
        self.background.paste(image, self.position)
        self.canvas.show(self.background)
        return self.background

    def save(self):
        self.background.save('background.png', quality=95)

def det_range(pixel, background):
    for i in range(len(background)):
        if abs(background[i] - pixel[i]) > int(255*0.05): # 5% range
            return False
    return True

def mul_255(n):
    return int(n*255)
    