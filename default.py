# -*- coding: utf-8 -*-
import getopt
import sys
from text2image import Text2Image


def usage():
    print """
    Name
    \t default.py - Converts a text message to an image\n
    Usage
    \t python default.py [-h] [-i] -o\n
    Options
    \t -h \t --help        \t Shows usage
    \t -i \t --input-file  \t Input file which contains the text message
    \t -o \t --output-file  \t Output file of the generated image
    """


def main(argv):
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
        config['text'] = args[0]

    my_converter = Text2Image(config)
    my_converter.convert()

if __name__ == '__main__':
    main(sys.argv[1:])