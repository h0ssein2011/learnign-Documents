from PIL import Image

img = Image.open('flag.png')
img = img.convert('RGB')
print(img.size)
r, g, b = img.getpixel((1, 1))
print(r, g, b)


