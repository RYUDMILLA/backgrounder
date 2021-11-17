from PIL import Image, ImagePalette
import sys
from matplotlib import colors
# import time

def get_size():
    try:
        input = sys.stdin.readline().strip().upper()
        if input in size_dict:
            print(f"{input}{size_dict[input]} selected. ")
            return size_dict[input]
        else:
            width,height = map(int, input.split())
        return (width,height)
    except ValueError:
        print("Unavailable")
        exit(0)

def paste():
    print("select location : mid / bottom / top / upper/ lower")
    while(True):
        location = sys.stdin.readline().strip()
        if location == 'mid':
            position = ((width - image.width)//2,(height - image.height)//2)
            break
        elif location == 'bottom':
            position = ((width - image.width)//2,(height - image.height))
            break
        elif location == 'lower':
            position = ((width - image.width)//2,(int)((height - image.height)*0.75))
            break
        elif location == 'top':
            position = ((width - image.width)//2,0)
            break
        elif location == 'upper':
            position = ((width - image.width)//2,(int)((height - image.height)*0.25))
            break
        else:
            print("Unavailable.Enter Again")
    # Image.Image.paste(background,image,position)
    background.paste(image, position)

def mul_255(n):
    return int(n*255)

def change_background(color):
    rgb = tuple(map(mul_255,colors.to_rgba(color)))
    print(background_color,'->',rgb)

    for x in range(0,width):
        for y in range(0,height):
            if background.getpixel((x,y)) == background_color:
                background.putpixel((x,y),rgb)

def get_background_color():
    print("Do you want to change the background color?(Y/N)",end=' ')
    yn = input()
    if yn == 'y' or yn == 'Y':
        print("What color?",end=' ')
        color = input()
        change_background(color)
    elif yn == 'n' or yn == 'N':
        print("Okay")

def resize():
    pass

print("SD : 750×1334 / HD : 1500x2668 / FHD : 1859x3306 / UHD : 2303x4096")
size_dict = {'SD':(750,1334), 'HD':(1500,2668), 'FHD':(1859,3306), 'UHD':(2303,4096)}

size = (width,height) = get_size()

image = Image.open('logo.png').convert('RGBA')  # image to paste
print(f"image size : {image.size}")

background_color = image.getpixel((0,0))
background = Image.new(mode='RGBA',size=size, color=background_color)

paste()

get_background_color()

background.save('background.png')
