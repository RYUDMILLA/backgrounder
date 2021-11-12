from PIL import Image, ImagePalette

width = 600
height = 1000

background = Image.new(mode='RGB',size=(width,height), color=(256,256,256))

image = Image.open('logo.png')
print(image.size)

# keep the original
image_copy = background.copy()
position = ((image_copy.width-image.width)//2, (image_copy.height-image.height)//2)
image_copy.paste(image,position)
image_copy.save('pasted_image.png')

# change the original
pos = ((width - image.width)//2,(height - image.height)//2)
Image.Image.paste(background,image,pos)

background.save('background.png')

