# Prepare2Tweet

Python scripts that converts a long text message to an image (so it can be tweeted ^^)

## Directory structure

docs/ - It contains the project documentation.

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

```console
    $ git clone https://github.com/josemifv/prepare2tweet.git
    $ cd prepare2tweet
    $ virtualenv venv --distribute
	New python executable in venv/bin/python
	Installing setuptools, pip...done.    
	$ . venv/bin/activate
    $ python setup.py install
    ...
    Finished processing dependencies for text2image
```

## Usage

Prepare2Tweet is very easy to use. Just execute the command as follows to convert a text to an image:

```console
    $ python prepare2tweet.py -o output.png "I want to convert this text to an image"
```

As the text is shorter that 140 characters, the program will do nothing :). The console will show the following:

```console
	$ Your text message is shorter than 140 characters. Nothing to do here...
```

But you can exeecute one of the examples included in the examples/ directory as follows. The parameter ```-f``` specifies an input file.

```console
    $ python prepare2tweet.py -i examples/hashtags_message.txt -o output.png
```

And now the console output will be like this:

```console
Now you can tweet it: #book #hidalgo #quotes
The image is stored in output.png
```

It must be said that if both the input file and the text is present in the script invocation, the latter will be ignored.

And that's all. I hope you enjoy it ^^
