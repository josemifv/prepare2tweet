# coding=utf8
import text2image
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def text2png(text, filename, color="#FFF", bgcolor="#000", width=640, height=480):

    """
    It converts a string to a PNG image
    :param text: String to convert
    :param filename: Name of the output PNG file
    :param color: Text color
    :param bgcolor: Background color
    :param width: Image width
    :param height: Image height
    """
    img = Image.new('RGBA', (width, height), bgcolor)
    font = ImageFont.truetype(text2image.DEFAULT_FONT_FILE, 18)
    draw = ImageDraw.Draw(img)
    draw.text((10,10), text, color, font=font)
    img.save(filename)

if __name__ == '__main__':
    text2png("This is a test", 'test.png')