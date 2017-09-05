import Image, ImageDraw, ImageFont

txt = raw_input('text: ');
font_name = raw_input('font name (baskerville/times/helvetica) : ');
font_size = int(raw_input('font size : '));

image = Image.new("RGBA", (200,len(txt)*font_size*2), (0,0,0,0))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("resources/" + font_name + ".ttf", font_size)

draw.text((10, 0), txt, (0,0,0), font=font)
image = image.crop(image.getbbox())
image.save('test.png')