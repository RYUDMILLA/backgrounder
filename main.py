from PIL import Image, ImagePalette
from sys import stdin


def get_input():
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
    Image.Image.paste(background,image,position)

def change_background():
    background_color = image.getpixel((0,0))

    for x in range(0,width):
        for y in range(0,height):
            background.putpixel((x,y),background_color)

def resize():
    pass

# print("iPhone 8 : 750 × 1334")
phones = ['iphone8']

size = (width,height) = get_input()

background = Image.new(mode='RGB',size=size, color=(256,256,256))

image = Image.open('logo.png')
image.convert('RGB')
print(image.size)

change_background()

paste()

background.save('background.png')
