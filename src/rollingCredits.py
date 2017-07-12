from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


with open('rollCreds.txt') as f:
    content = f.readlines()

[x.strip() for x in content]

print content

'''
http://python-catalin.blogspot.com.ar/2010/06/add-text-on-image-with-pil-module.html
'''
font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf",25)
lines = 360
cols =  640

img=Image.new("RGBA", (cols, lines * 2),(120,20,20))
draw = ImageDraw.Draw(img)
disy = lines
dis_anim = 4
dis_pixel = 25

for i, t in enumerate(content):
    print i, t
    draw.text((0, i*dis_pixel + disy),t[:-1],(255,255,0),font=font)

img.save("imageBase.png")



for i in range(lines / dis_anim + 1):
    lines = dis_anim * i + 360
    print lines
    filename = "imageAnim" + str(i).zfill(4) + ".png"
    img2 = img.crop((0, 0, cols, lines))
    img2.save(filename)


