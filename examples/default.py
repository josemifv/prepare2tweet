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
    \t -o \t --output-dir  \t Output directory where the generated image will be stored
    """


def main(argv):
    try:
        options, args = getopt.gnu_getopt(argv, "hi:o:", ["help", "input-file=", "output-dir="])
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
        elif option in ("-o", "--output-dir"):
            config["output_dir"] = argument
        else:
            usage()
            sys.exit(2)

    my_converter = Text2Image(config)
    my_converter.convert()

if __name__ == '__main__':
    main(sys.argv[1:])