#!/usr/bin/env python3
from tkinter import *
from PIL import Image, ImageColor
import sys
import rotate_cursor as rc
from gui import Preview
import os


# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)

def dominant_color(image, transparent):  
    if transparent == False:    # RGB(not alpha)
        reduced = image.convert("P", palette=Image.ADAPTIVE) 
        palette = reduced.getpalette() 

        p_colors = reduced.getcolors()
        p_color = [_[0] for _ in p_colors]
        idx = p_colors[p_color.index(max(p_color))][1]

        rgb = palette[3*idx:3*idx+3]
        rgb.append(255)
        return tuple(rgb)
    else:                       # Transparent background
        make_transparent(image)
        return (0,0,0,0)

def get_size():
    print("Enter size you want to make.(width height)")
    print("SD : 750x1334 / HD : 1500x2668 / FHD : 1859x3306 / UHD : 2303x4096")
    size_dict = {'SD':(750,1334), 'HD':(1500,2668), 'FHD':(1859,3306), 'UHD':(2303,4096)}
    while(True):
        try:
            input = sys.stdin.readline().strip().upper()
            if input in size_dict:
                print(f"{input}{size_dict[input]} selected.\n")
                return size_dict[input]
            else:
                width,height = map(int, input.split())
                print(f"{width}, {height} selected.\n")
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
        try:
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
        except ValueError:
            print("Error")

def get_background_color():
    print("\nDo you want to change the background color?(Y/N)",end=' ')
    yn = input()
    if yn == 'y' or yn == 'Y':
        change_background()
    # elif yn == 'n' or yn == 'N':
    else:
        print("Okay")
    canvas.close()

def change_background():
    try:
        print("What color?",end=' ')
        color = input()
        rgb = ImageColor.getcolor(color,'RGBA')
    except ValueError:
        print("Unavailable color")
        change_background()
    else:
        print(background_color,'->',rgb)
        print("Converting...",end='')
        with rc.Spinner():
            for x in range(0,width):
                for y in range(0,height):
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

def det_range(pixel, background):
    for i in range(len(background)):
        if abs(background[i] - pixel[i]) > int(255*0.05): # 5% range
            return False
    return True
    
def has_transparency(image):
    if image.mode == "P":
        transparent = image.info.get("transparency", -1)
        for _, index in image.getcolors():
            if index == transparent:
                return True
    elif image.mode == "RGBA":
        extrema = image.getextrema()
        if extrema[3][0] < 255:
            return True
    return False

def make_transparent(image):
    for x in range(0,image.width):
        for y in range(0,image.height):
            if image.getpixel((x,y))[-1] < int(255*0.15):
                image.putpixel((x,y),(0,0,0,0))


image = Image.open(sys.argv[1]).convert('RGBA')  # image to paste
# background_color = image.getpixel((0,0))
background_color = dominant_color(image, has_transparency(image))
print(f"image size : {image.size} / background color : {background_color}\n")

size = (width,height) = get_size()

root = Tk()
canvas = Preview(root, size[1]/size[0])

background = set_background()

get_background_color()

root.mainloop()

background.save(f'results/{os.path.splitext(os.path.basename(sys.argv[1]))[0]}_bg.png', quality=95)
