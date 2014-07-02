# -*- coding: utf-8 -*-
import getopt
import sys
from text2image import Text2Image


def usage():
    """
    It prints the script usage and the parameters needed to work properly.
    """
    print """
    Name
    \t prepare2tweet.py - Converts a long text message to an image (so you can tweet it ^^)\n
    Usage
    \t prepare2tweet.py [-h] [-i] <input_file> -o <output_file> <Long text to prepare>\n
    Options
    \t -h \t --help        \t Shows usage
    \t -i \t --input-file  \t Input file which contains the text message. If added text added as a program argument will be ignored
    \t -o \t --output-file \t Output file of the generated image
    """


def main(argv):
    """
    Main function.

    :param argv: Program parameters.
    """
    # Get and check program parameters
    try:
        options, args = getopt.gnu_getopt(argv, "hi:o:", ["help", "input-file=", "output-file="])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)

    config = {}
    for option, argument in options:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ("-i", "--input-file"):
            config["input_file"] = argument
        elif option in ("-o", "--output-file"):
            config["output_file"] = argument
        else:
            usage()
            sys.exit(2)

    if len(args) > 0:
        config["text"] = args[0]

    # If all dependencies are satisfied, the image generation process is started
    if config.has_key("output_file") and (config.has_key("text") or config.has_key("input_file")):
        text_tweetable, image_file = Text2Image.convert(config)

        if image_file is None:
            print "Your text message is shorter than 140 characters. Nothing to do here..."
        else:
            print "Now you can tweet it: %s" % text_tweetable
            print "The image is stored in %s" % image_file
    else:
        print "Error: Not enough parameters"
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])