# bandcamp-get [![Build Status](https://travis-ci.org/huntrar/bandcamp-get.svg?branch=master)](https://travis-ci.org/huntrar/bandcamp-get) [![PyPI](https://img.shields.io/pypi/dm/bandcamp-get.svg?style=flat)]()

## automated music downloading via selenium

bandcamp-get uses Selenium WebDriver to download free albums from the music website [bandcamp](https://bandcamp.com/). If run on default, bandcamp-get creates a disposable email address using [Guerrilla Mail](https://grr.la). Music sent to this inbox will be downloaded once all albums have been processed, no user interaction necessary.

## Installation
    pip install bandcamp-get

or

    pip install git+https://github.com/huntrar/bandcamp-get.git#egg=bandcamp-get

or

    git clone https://github.com/huntrar/bandcamp-get
    cd bandcamp-get
    python setup.py install

## Usage
    usage: bandcamp-get [-h] [-b BROWSER] [-e EMAIL] [-v] [USER]
    
    automated music downloading via selenium
    
    positional arguments:
      USER                  bandcamp user to download from
    
    optional arguments:
      -h, --help            show this help message and exit
      -b BROWSER, --browser BROWSER
                            enter chrome or firefox, defaults to firefox
      -e EMAIL, --email EMAIL
                            use your own email instead of a throwaway
      -v, --version         display current version

## Author
* Hunter Hammond (huntrar@gmail.com)

## Notes
* Supports both Python 2.x and Python 3.x.
* If you choose to use a throwaway email (chosen by default unless --email flag is used), then all emails sent to the throwaway will be opened and the download links followed by the WebDriver. This occurs once all albums have been emailed/otherwise downloaded.
* Closing the bandcamp browser window before all albums have been downloaded is fine and will end processing early. The links which have been emailed already will still be downloaded as long as the Guerrilla Mail window is left open.
