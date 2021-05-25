import extcolors
import PIL
import json
img = PIL.Image.open("one.png")
# img = PIL.Image.open("two.png")
# img = PIL.Image.open("three.jpeg")
# img = PIL.Image.open("four.png")
# img = PIL.Image.open("five.png")
colors, pixel_count = extcolors.extract_from_image(img)

width, height = img.size

def rgb_to_hex(red, green, blue):
    return '#%02x%02x%02x' % (red, green, blue)



rgb_im = img.convert('RGB')

data  = {'dominant_color': rgb_to_hex(colors[0][0][0],colors[0][0][1],colors[0][0][2]) , 'logo_border': rgb_to_hex(rgb_im.getpixel(((0.01*width),(0.01*height)))[0],rgb_im.getpixel(((0.01*width),(0.01*height)))[1],rgb_im.getpixel(((0.01*width),(0.01*height)))[2]) }
person_json = json.dumps(data)
print(person_json)

f = open("test_outputs.md", "a")
f.write(person_json)
f.close