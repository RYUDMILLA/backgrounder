from PIL import Image, ImagePalette
from sys import stdin

# print("iPhone 8 : 750 × 1334")
phones = ['iphone8']
input = stdin.readline().strip()
if input in phones:
    width = 750
    height = 1334
else:
    width,height = map(int, input.split())

background = Image.new(mode='RGB',size=(width,height), color=(256,256,256))

image = Image.open('logo.png')
print(image.size)

# change the original
pos = ((width - image.width)//2,(height - image.height)//2)
Image.Image.paste(background,image,pos)

background.save('background.png')
