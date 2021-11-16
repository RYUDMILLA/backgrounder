from PIL import Image

def to_white(image):
    img = Image.open(image)
    img.load()
    bg = Image.new(mode='RGB',size=img.size,color=(255,255,255))
    bg.paste(img,mask=img.split()[3])
    bg.save('sample.jpg',"JPEG",quality=100)

def to_black(image):
    img = Image.open(image).convert('RGB')
    img.save('sample.jpg')

def PNG_to_JPEG():
    image = 'logo.png'
    print("Transparent to White? to Black?")    
    wb = input()
    if wb.lower() == 'white':
        to_white(image)
    elif wb.lower() == 'black':
        to_black(image)
    else:
        to_white(image)

    


