import cStringIO, base64
from flask import Flask, request
import cgi
import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route("/")
def hello():
	query = cgi.parse_qs(request.query_string)
	print(query)

	txt = query['text'][0]
	font_name = query['font'][0]
	font_size = int(query['size'][0])

	image = Image.new("RGBA", (font_size*len(txt) + 5, font_size + 5), (0,0,0,0))
	draw = ImageDraw.Draw(image)
	try:
		font = ImageFont.truetype("resources/" + font_name + ".ttf", font_size)
	except:
		font = ImageFont.truetype("resources/helvetica.ttf", font_size)

	draw.text((5, 0), txt, (0,0,0), font=font)
	image = image.crop(image.getbbox())
	buffer = cStringIO.StringIO()
	image.save(buffer, format="PNG")
	return "<img src=\"data:image/png;base64," + base64.b64encode(buffer.getvalue()) + "\"/>"


if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, threaded=True)


