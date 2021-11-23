from PIL import Image
import sys
from matplotlib import colors
import rotate_cursor as rc

def get_size():
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
        exit(0)

def set_position(image, location):
    if location == 'mid':
        position = ((width - image.width)//2,(height - image.height)//2)
    elif location == 'bottom':
        position = ((width - image.width)//2,(height - image.height))
    elif location == 'lower':
        position = ((width - image.width)//2,(int)((height - image.height)*0.75))
    elif location == 'top':
        position = ((width - image.width)//2,0)
    elif location == 'upper':
        position = ((width - image.width)//2,(int)((height - image.height)*0.25))
    return position

def set_background():
    print("select location : mid / bottom / top / upper/ lower")
    locations = ['mid','bottom','lower','top','upper']
    while(True):
        location = sys.stdin.readline().strip()
        if location in locations:
            break
        else:
            print("Unavailable.Enter Again.")
    # Image.Image.paste(background,image,position)
    return resize(image, location)

def paste(image, location):
    position = set_position(image, location)
    background = Image.new(mode='RGBA', size=size, color=background_color)
    background.paste(image, position)
    background.show()
    return background

def resize(image, location):
    pasted = paste(image, location)
    resized = image.copy()
    while(True):
        print("\nWant to resize?(Y/N)",end=' ')
        yn = input()
        if yn == 'y' or yn == 'Y':
            print("Enter width ratio(%):",end=' ')  # < 100
            ratio = int(input())
            wh_ratio = image.height/image.width
            image_width = int(width * ratio * 0.01)
            resized = image.resize((image_width,int(image_width*wh_ratio)), Image.ANTIALIAS)
            pasted = paste(resized, location)
        # elif yn == 'n' or yn == 'N':
        else:
            print("Confirmed")
            return pasted

def mul_255(n):
    return int(n*255)

def det_range(pixel, background):
    for i in range(len(background)):
        if abs(background[i] - pixel[i]) > int(255*0.05): # 5% range
            return False
    return True

def change_background(color):
    rgb = tuple(map(mul_255,colors.to_rgba(color))) # RGBA using matplotlib
    # rgb = ImageColor.getrgb(color) # RGB using PIL
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

def get_background_color():
    print("\nDo you want to change the background color?(Y/N)",end=' ')
    yn = input()
    if yn == 'y' or yn == 'Y':
        print("What color?",end=' ')
        color = input()
        change_background(color)
    # elif yn == 'n' or yn == 'N':
    else:
        print("Okay")

image = Image.open('sensitivity.png').convert('RGBA')  # image to paste
background_color = image.getpixel((0,0))
print(f"image size : {image.size} / background color : {background_color}\n")

print("Enter size you want to make.")
print("SD : 750×1334 / HD : 1500x2668 / FHD : 1859x3306 / UHD : 2303x4096")
size_dict = {'SD':(750,1334), 'HD':(1500,2668), 'FHD':(1859,3306), 'UHD':(2303,4096)}
size = (width,height) = get_size()

background = set_background()

get_background_color()

background.save('background.png', quality=95)
