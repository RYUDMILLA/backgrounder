from PIL import Image

def to_white(image, name):
    img = Image.open(image)
    img.load()
    bg = Image.new(mode='RGB',size=img.size,color=(255,255,255))
    bg.paste(img,mask=img.split()[3])
    bg.save(f'{name}.jpg',"JPEG",quality=100)

def to_black(image, name):
    img = Image.open(image).convert('RGB')
    img.save(f'{name}.jpg')

def PNG_to_JPEG(name):
    image = f'{name}.png'
    print("Transparent to White? to Black?")    
    wb = input()
    if wb.lower() == 'white':
        to_white(image, name)
    elif wb.lower() == 'black':
        to_black(image, name)
    else:
        to_white(image, name)
