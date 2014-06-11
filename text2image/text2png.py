# -*- coding: utf-8 -*-
import text2image
import textwrap
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def text2png(text, filename, color=text2image.DEFAULT_FONT_COLOR, bgcolor=text2image.DEFAULT_BG_COLOR,
             margin=text2image.DEFAULT_IMAGE_MARGIN, chars_per_line=text2image.DEFAULT_CHARS_PER_LINE):

    """
    It converts a string to a PNG image
    :param text: String to convert
    :param filename: Name of the output PNG file
    :param color: Text color
    :param bgcolor: Background color
    :param width: Image width
    :param height: Image height
    """
    font = ImageFont.truetype(text2image.DEFAULT_FONT_FILE, 18)
    lines = textwrap.wrap(text, chars_per_line)
    # Add signature
    lines.append(" ")
    lines.append(text2image.DEFAULT_SIGNATURE)

    # Get sizes in order to calculate the result image size
    font_widths = range(len(lines))
    font_heights = range(len(lines))
    for i in range(len(lines)):
        font_widths[i], font_heights[i] = font.getsize(lines[i])
    font_width = max(font_widths)
    font_height = max(font_heights)

    width = font_width + (margin * 2)
    height = font_height * len(lines) + (margin * 2)

    img = Image.new('RGBA', (width, height), bgcolor)
    draw = ImageDraw.Draw(img)
    offset = margin
    for line in lines:
        draw.text((margin, offset), line.decode('utf-8'), color, font=font)
        offset += font_height
    img.save(filename)

if __name__ == '__main__':
    text2png("This is a test", 'test.png')