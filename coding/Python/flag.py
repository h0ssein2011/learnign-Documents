from PIL import Image

img = Image.open('flag.png')
img = img.convert('RGB')
print(img.size)

for i in range(img.size[0]):
        r, g, b = img.getpixel((i, 1))
        print( r,g,b)



for i in range(int(img.size[0]/3)):
        r, g, b = img.getpixel((i, 1))
        print( chr(b),end=' ')

for i in range(int(img.size[0]/3),int(img.size[0]*2/3)):
        r, g, b = img.getpixel((i, 1))
        print( chr(255),end=' ')
        

r,g,b =84 ,109, 140
print(chr(r),chr(g),chr(b),end=' ')
r,g,b =222 ,96 ,110
print(chr(r),chr(g),chr(b),end=' ')
