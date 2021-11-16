from PIL import Image, ImagePalette
from sys import stdin
from matplotlib import colors

def get_size():
    try:
        input = stdin.readline().strip()
        if input in phones:
            width,height = 750, 1334
        else:
            width,height = map(int, input.split())
        return (width,height)
    except ValueError:
        print("Unavailable")

def paste():
    print("select location : mid / bottom / top / upper/ lower")
    while(True):
        location = stdin.readline().strip()
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
            print("Unavailable")
            paste()
    # Image.Image.paste(background,image,position)
    background.paste(image, position)

def mul_255(n):
    return int(n*255)

def change_background(color):
    rgb = tuple(map(mul_255,colors.to_rgba(color)))
    print(rgb,background_color)

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

# print("iPhone 8 : 750 × 1334")
phones = ['iphone8']

size = (width,height) = get_size()

image = Image.open('logo.png').convert('RGBA')  # image to paste
print(image.size)

background_color = image.getpixel((0,0))
background = Image.new(mode='RGBA',size=size, color=background_color)

paste()

get_background_color()

background.save('background.png')
