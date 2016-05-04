from PIL import Image, ImageDraw

im = Image.new('RGB', (400, 400), (255, 255, 255))
draw = ImageDraw.Draw(im)
draw.line((100, 100, 300, 300), fill=128)
draw.rectangle([(100, 100), (300, 300)], outline=1)
x, y, r = 200, 200, 100
draw.ellipse((x - r, y - r, x + r, y + r), outline=1)
im.show()
