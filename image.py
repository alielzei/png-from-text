import cStringIO, base64
import Image, ImageDraw, ImageFont
import sys

txt = sys.argv[1]
font_size = int(sys.argv[2])
font_name = sys.argv[3]

try:
	font = ImageFont.truetype("resources/" + font_name + ".ttf", font_size)
except Exception as e:
	if type(e) == IOError:
		font = ImageFont.truetype("resources/helvetica.ttf", font_size)
	else:
		raise e

image = Image.new("RGBA", ( font_size*(len(txt) + (1/5) ), font_size*2), (0,0,0,0))
draw = ImageDraw.Draw(image)

draw.text((font_size/5, 0), txt, (0,0,0), font=font)

image = image.crop(image.getbbox())
buffer = cStringIO.StringIO()

image.save(buffer, format="PNG")

print(base64.b64encode(buffer.getvalue()));


