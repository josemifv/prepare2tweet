# -*- coding: utf-8 -*-
import text2image
import text2png

class Text2Image:
    def __init__(self, config):
        self.config = config

    def convert(self):
        text_to_convert = None
        if "input_file" in self.config:
            input_file = open(self.config["input_file"])
            text_to_convert = input_file.read()
            input_file.close()
        else:
            text_to_convert = self.config["text"]

        if len(text_to_convert) < text2image.TWITTER_LIMIT:
            print "Text message shorter than %d characters. Nothing to do here..." % text2image.TWITTER_LIMIT

        return text2png.text2png(text_to_convert, self.config['output_file'])