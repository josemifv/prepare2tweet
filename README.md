# Prepare2Tweet
=============

Python scripts that converts a long text message to an image (so it can be tweeted ^^)

## Directory structure
===================

examples/ - Directory containing sample input text files that can be used to test the script.

text2image/ - It contains the library implemented to convert text to an image.

prepare2tweet.py - main script.

pytest.ini - PyTest configuration file

setup.py - Script to install text2image library

requirements.txt - Text file containing the program required to run.

AUTHORS - Authors file

CHANGES - Changes from each release.

LICENSE - License file.

README.md - This file.


## Installation

The first step to using any software package is getting it properly installed. The project is developed in GitHub, so it can be downloaded anytime or checkout to work with the sources. The following steps describes the installation from GitHub.

.. code-block:: console

    $ git clone https://github.com/josemifv/python-text-2-image.git
    $ cd python-text-2-image
    $ virtualenv venv --distribute
    Installing distribute............done.
    $ . venv/bin/activate
    $ python setup.py install
    ...
    Finished processing dependencies for Prepare2Tweet

