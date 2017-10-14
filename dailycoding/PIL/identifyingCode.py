# coding=utf-8
"""生成验证码图片
路径记得自己改(*^▽^*)"""
import random
from PIL import Image, ImageFont, ImageDraw, ImageFilter

fontPath = r'C:\Windows\Fonts\Arial.ttf'
outputFigPath = r'code.jpg'


# 随机字母:
def rnd_char():
	return chr(random.randint(65, 90))


# 随机颜色1——数字:
def rnd_color():
	return (random.randint(64, 255),
	        random.randint(64, 255),
	        random.randint(64, 255))


# 随机颜色2——底片噪声:
def rnd_color2():
	return (random.randint(32, 127),
	        random.randint(32, 127),
	        random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype(fontPath, 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
	for y in range(height):
		draw.point((x, y),
		           fill=rnd_color())
# 输出文字:
for t in range(4):
	draw.text((60 * t + 10, 10),
	          rnd_char(),
	          font=font,
	          fill=rnd_color2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save(outputFigPath, 'jpeg')
