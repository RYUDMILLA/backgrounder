from PIL import Image

def to_white(name):
    img = Image.open(f'{name}.jpg')
    img.load()
    bg = Image.new(mode='RGB',size=img.size,color=(255,255,255))
    bg.paste(img,mask=img.split()[3])
    bg.save(f'{name}.jpg',"JPEG",quality=100)

def to_black(name):
    img = Image.open(f'{name}.jpg').convert('RGB')
    img.save(f'{name}.jpg')

def PNG_to_JPEG(name):
    print("Transparent to White? to Black?")    
    wb = input()
    if wb.lower() == 'white':
        to_white(name)
    elif wb.lower() == 'black':
        to_black(name)
    else:
        to_white(name)
