from PIL import Image

def det_range(pixel, background):
    for i in range(len(background)):
        if abs(background[i] - pixel[i]) > int(255*0.05): # 5% range
            return False
    return True

def change_background(img, color, background_color):
    for x in range(0,img.width):
        for y in range(0,img.height):
            if det_range(img.getpixel((x,y)),background_color) == True:
                img.putpixel((x,y),color)

def background_to_transparent(img):
    background_color = img.getpixel((0,0))
    print(background_color)
    change_background(img, (0,0,0,0), background_color)

def JPEG_to_PNG(name):
    img = Image.open(f'{name}.jpg').convert('RGBA')
    print("Change background to transparent?(Y/N)",end=' ')
    yn = input()
    if yn.lower() == 'y':
        background_to_transparent(img)
    img.save(f'{name}.png')
