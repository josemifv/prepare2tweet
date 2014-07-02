# -*- coding: utf-8 -*-
import text2image
import textwrap
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def text2png(text,
             filename,
             color=text2image.DEFAULT_FONT_COLOR,
             bgcolor=text2image.DEFAULT_BG_COLOR,
             margin=text2image.DEFAULT_IMAGE_MARGIN,
             chars_per_line=text2image.DEFAULT_CHARS_PER_LINE):

    """
    It converts a string to a PNG image

    :param text: String to convert
    :param filename: Name of the output PNG file
    :param color: Text color
    :param bgcolor: Background color
    :param margin: Space around the text in the image
    :param chars_per_line: Number of chars per line in the image
    """
    # Convert input text to an array of lines
    lines = textwrap.wrap(text, chars_per_line)
    # Append signature to the text
    lines.append(" ")
    lines.append(text2image.DEFAULT_SIGNATURE)

    # Get sizes in order to calculate the result image size
    font = ImageFont.truetype(text2image.DEFAULT_FONT_FILE, text2image.DEFAULT_FONT_SIZE)
    line_widths = range(len(lines))
    line_heights = range(len(lines))
    for i in range(len(lines)):
        line_widths[i], line_heights[i] = font.getsize(lines[i])
    # In order to avoid lines to be cropped, max line sizes must be used
    text_width = max(line_widths)
    text_height = max(line_heights)

    # Get result image dimension
    width = text_width + (margin * 2)
    height = text_height * len(lines) + (margin * 2)

    # Create image and draw text lines
    img = Image.new('RGBA', (width, height), bgcolor)
    draw = ImageDraw.Draw(img)
    offset = margin
    for line in lines:
        draw.text((margin, offset), line.decode('utf-8'), color, font=font)
        offset += text_height
    img.save(filename)

if __name__ == '__main__':
    text2png("This is a test", 'test.png')