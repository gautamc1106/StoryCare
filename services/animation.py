import scipy as sp
import PIL
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import textwrap
import os
from PIL import ImageOps

def animator(imageURL, imageText, img_idx):

    im = Image.open(imageURL)
    basewidth = 600
    im = im.resize([basewidth, basewidth], Image.ANTIALIAS)

    x = im.size[0]
    y = im.size[1]

    try:
    	draw = ImageDraw.Draw(im,'RGBA')
    except ValueError:
    	im = im.convert('RGBA')
    	draw = ImageDraw.Draw(im,'RGBA')


    if(img_idx==0):
    	lines = textwrap.wrap(imageText, 20)

    else:
    	lines = textwrap.wrap(imageText, 37)

    maxlen = max(len(s) for s in lines)
    long_line = [s for s in lines if len(s)==maxlen ]
    unique_line = list(set(long_line))
    unique_line = unique_line[0]

    print("Maxlen")
    print(maxlen, long_line)


    font, font_color = font_type(im, unique_line, img_idx)

    text_width, text_height = font.getsize(unique_line)

    region  = new_region(x,y)

    x_text = 0.05*x
    y_text = 0.8*y + ((0.8*y)-(text_height*len(lines)))/2 - 0.05*y


    #draw.rectangle(region, (255,0,0,190))
    draw.polygon(region, (255,250,250,230))
    for line in lines:

    	draw.text((x_text, y_text), line, font=font, fill= font_color)
    	y_text += text_height + 5

    im.show()



def font_type(image,txt, img_idx):
	font_size = 1

	if img_idx==0:
		font_fname = '../fonts/Arial/ARIBL.ttf'
		font_color = 'rgb(0,0,0)'
	else:
		font_fname = '../fonts/Arial/Arialn.ttf'
		font_color = 'rgb(0,0,0)'


	font = ImageFont.truetype(font_fname, font_size)

	img_fraction = 0.60
	while font.getsize(txt)[0] < (img_fraction*image.size[0]):
		font_size += 1
		font = ImageFont.truetype(font_fname, font_size)
	font_size -= 1
	font = ImageFont.truetype(font_fname, font_size )

	return font, font_color

def new_region(x,y):
	region = [(0,0.8*y), (0.8*x,0.8*y), (0.85*x,0.75*y), (x,0.75*y), (x,y),(0,y)]
	return region

animator('/Users/gautamchheda/Desktop/Startup Studio/stock_images/shutterstock_121813225.jpg','StoryCarf3rjfh3uihf3iufhfu3fu3ffnjr3hfjrhfhrgh5ghihgige is the best',1)
