# -*- coding: utf-8 -*-
import re
import text2image
import text2png


class Text2Image:
    def __init__(self):
        """
        Constructor. It does nothing.

        :return: A new instance of the class.
        """
        pass

    @staticmethod
    def extract_hashtags(text):
        # From http://stackoverflow.com/questions/8347567/how-can-i-grab-all-terms-beginning-with
        return [word for word in text.split() if word.startswith("#")]

    @staticmethod
    def extract_urls(text):
        # From http://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
        url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        return re.findall(url_pattern, text)

    @staticmethod
    def create_short_text(text_to_convert):
        """
        It creates a short text from a given text containing only its hashtags and urls.

        :param text_to_convert: Input text.
        :return: A string containing the extracted hashtags and urls from the input text.
        """
        # Extract hashtags and remove duplicates
        hashtags = set(Text2Image.extract_hashtags(text_to_convert))

        # Extract urls and remove duplicates
        urls = set(Text2Image.extract_urls(text_to_convert))

        # Create new text by concatenating hashtags and urls (separated by a blank space)
        text = " ".join(list(hashtags) + list(urls))
        return text if len(text) > 0 else text2image.DEFAULT_SIGNATURE

    @staticmethod
    def convert(config):
        """
        It converts a long text to an image. If text is shorter or equals to the TWITTER limit,
        nothing will be done.

        :param config: A dictionary containing all config parameters needed for the process.
        This parameters are: text, input_file and output_file.
        :return: If
        """
        # If an input file property is found, its content will be used as the input text
        if "input_file" in config:
            input_file = open(config["input_file"])
            text_to_convert = input_file.read()
            input_file.close()
        else:
            text_to_convert = config["text"]

        if len(text_to_convert) > text2image.TWITTER_LIMIT:
            text2png.text2png(text_to_convert, config["output_file"])
            return Text2Image.create_short_text(text_to_convert), config["output_file"]

        return text_to_convert, None