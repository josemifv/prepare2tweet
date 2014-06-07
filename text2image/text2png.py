# coding=utf8
import text2image
import textwrap
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def text2png(text, filename, color=text2image.DEFAULT_FONT_COLOR, bgcolor=text2image.DEFAULT_BG_COLOR, width=640):

    """
    It converts a string to a PNG image
    :param text: String to convert
    :param filename: Name of the output PNG file
    :param color: Text color
    :param bgcolor: Background color
    :param width: Image width
    :param height: Image height
    """
    offset = 20
    font = ImageFont.truetype(text2image.DEFAULT_FONT_FILE, 18)
    lines = textwrap.wrap(text, 70)
    height = int(font.getsize(lines[0])[1] * len(lines)) + (offset * 2)  # Increase the image size in a 20%

    img = Image.new('RGBA', (width, height), bgcolor)
    draw = ImageDraw.Draw(img)
    margin = 20
    for line in lines:
        draw.text((margin, offset), line, color, font=font)
        offset += font.getsize(line)[1]
    img.save(filename)

if __name__ == '__main__':
    text2png("This is a test", 'test.png')