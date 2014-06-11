# -*- coding: utf-8 -*-
import re
import text2image
import text2png


class Extractor:

    def __init__(self):
        pass

    def extract(self, text):
        pass


class URLExtractor(Extractor):

    def __init__(self):
        # From http://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
        self.url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    def extract(self, text):
        return re.findall(self.url_pattern, text)


class HashtagExtractor(Extractor):
    def __init__(self):
        pass

    def extract(self, text):
        # From http://stackoverflow.com/questions/8347567/how-can-i-grab-all-terms-beginning-with
        return [word for word in text.split() if word.startswith("#")]


class Text2Image:
    def __init__(self, config):
        self.config = config
        self.url_extractor = URLExtractor()
        self.hashtag_extractor = HashtagExtractor()

    def create_short_text(self, text_to_convert):
        # Extract hashtags and remove duplicates
        hashtags = set(self.hashtag_extractor.extract(text_to_convert))
        # Extract urls and remove duplicates
        urls = set(self.url_extractor.extract(text_to_convert))
        # Create new text by concatenating hashtags and urls (separated by a blank space)
        text = " ".join(list(hashtags) + list(urls))
        return text if len(text) > 0 else text2image.DEFAULT_SIGNATURE

    def convert(self):
        if "input_file" in self.config:
            input_file = open(self.config["input_file"])
            text_to_convert = input_file.read()
            input_file.close()
        else:
            text_to_convert = self.config["text"]

        if len(text_to_convert) > text2image.TWITTER_LIMIT:
            text2png.text2png(text_to_convert, self.config["output_file"])
            return self.create_short_text(text_to_convert), self.config["output_file"]

        return text_to_convert, None