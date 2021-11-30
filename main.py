from tkinter import *
from PIL import Image, ImageTk
import sys
from matplotlib import colors
import rotate_cursor as rc

class Preview():
    def __init__(self):
        self.canvas = Canvas(root, width=375, height=667)
        self.canvas.pack()

    def create(self, image):
        self.img = ImageTk.PhotoImage(image.resize((375, 667), Image.ANTIALIAS))
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=NW, image=self.img)
    
    def update(self, image):
        self.img = ImageTk.PhotoImage(image.resize((375, 667), Image.ANTIALIAS))
        self.canvas.itemconfig(self.image_on_canvas,image=self.img)

    def show(self, image):
        try:
            canvas.update(image)
        except AttributeError:
            canvas.create(image)

def get_size():
    print("Enter size you want to make.")
    print("SD : 750×1334 / HD : 1500x2668 / FHD : 1859x3306 / UHD : 2303x4096")
    size_dict = {'SD':(750,1334), 'HD':(1500,2668), 'FHD':(1859,3306), 'UHD':(2303,4096)}
    while(True):
        try:
            input = sys.stdin.readline().strip().upper()
            if input in size_dict:
                print(f"{input}{size_dict[input]} selected.\n")
                return size_dict[input]
            else:
                width,height = map(int, input.split())
            return (width,height)
        except ValueError:
            print("Unavailable")
            
def set_background():
    while(True):
        try:
            print("Set horizonal postion as the ratio(%):",end=' ')
            h_ratio = int(input())*0.01
            print("Set vertical position as the ratio(%):",end=' ')
            v_ratio = (100 - int(input()))*0.01
            break
        except ValueError:
            print("Unavailable.")
    return resize(image,h_ratio,v_ratio)

def resize(image, h_ratio, v_ratio):
    pasted = paste(image, h_ratio, v_ratio)
    resized = image.copy()
    while(True):
        print("\nWant to resize?(proportion maintained)(Y/N)",end=' ')
        yn = input()
        if yn == 'y' or yn == 'Y':
            print("Enter width ratio(%):",end=' ')  # < 100
            ratio = int(input())
            wh_ratio = image.height/image.width
            image_width = int(width * ratio * 0.01)
            resized = image.resize((image_width,int(image_width*wh_ratio)), Image.ANTIALIAS)
            pasted = paste(resized, h_ratio, v_ratio)
        # elif yn == 'n' or yn == 'N':
        else:
            print("Confirmed")
            return pasted

def get_background_color():
    print("\nDo you want to change the background color?(Y/N)",end=' ')
    yn = input()
    if yn == 'y' or yn == 'Y':
        change_background()
    # elif yn == 'n' or yn == 'N':
    else:
        print("Okay")

def change_background():
    try:
        print("What color?",end=' ')
        color = input()
        rgb = tuple(map(mul_255,colors.to_rgba(color))) # RGBA using matplotlib
        # rgb = ImageColor.getrgb(color) # RGB using PIL
    except ValueError:
        print("Unavailable color")
        change_background()
    else:
        print(background_color,'->',rgb)
        print("Converting...",end='')
        with rc.Spinner():
            for x in range(0,width):
                for y in range(0,height):
                    # if background.getpixel((x,y)) == background_color:
                    if det_range(background.getpixel((x,y)),background_color) == True:
                        background.putpixel((x,y),rgb)
            assert(True)                            # stop rotating
            sys.stdout.write('\033[2K\033[1G')      # delete command line
            print("Converted!")
            canvas.show(background)


def set_position(image, h_ratio, v_ratio):
    return (int((width - image.width)*h_ratio),int((height - image.height)*v_ratio))

def paste(image, h_ratio, v_ratio):
    position = set_position(image, h_ratio, v_ratio)
    background = Image.new(mode='RGBA', size=size, color=background_color)
    background.paste(image, position)
    canvas.show(background)
    return background

def mul_255(n):
    return int(n*255)

def det_range(pixel, background):
    for i in range(len(background)):
        if abs(background[i] - pixel[i]) > int(255*0.05): # 5% range
            return False
    return True
    

image = Image.open('logo.png').convert('RGBA')  # image to paste
background_color = image.getpixel((0,0))
print(f"image size : {image.size} / background color : {background_color}\n")

size = (width,height) = get_size()

root = Tk()
root.title("Preview")
canvas = Preview()

background = set_background()

get_background_color()

root.mainloop()

background.save('background.png', quality=95)