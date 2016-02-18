# bandcamp-get (based on https://pypi.python.org/pypi/bandcamp_get)

## automated music downloading via selenium

bandcamp-get uses Selenium WebDriver to download free albums from the music website [bandcamp](https://bandcamp.com/). If run on default, bandcamp-get creates a disposable email address using [Guerrilla Mail](https://grr.la). Music sent to this inbox will be downloaded once all albums have been processed, no user interaction necessary.

## Installation

    git clone https://github.com/Ricardo-Silva91/bandcamp_downloader.git
    cd bandcamp-get
    python setup.py install

## Usage
    usage: bandcamp-get [-h] [-b BROWSER] [-d DISPLAY] [-e EMAIL] [-v] [-f FOLDER]
                        [-js]
                        [USER]

    automated music downloading via selenium

    positional arguments:
      USER                  bandcamp user to download from

    optional arguments:
      -h, --help            show this help message and exit
      -b BROWSER, --browser BROWSER
                            enter chrome or firefox, defaults to firefox
      -d DISPLAY, --display DISPLAY
                            show display, 0-no 1-yes , defaul=0
      -e EMAIL, --email EMAIL
                            use your own email instead of a throwaway
      -v, --version         display current version
      -f FOLDER, --folder FOLDER
                            choose folder to download (absolute path) (default:
                            /Downloads)
      -js, --json_file      load a list of artists from json folder (replace USER
                            with path to file)


## Author
* original - Hunter Hammond (huntrar@gmail.com)
* this version - Ricardo Silva

## Notes
* version - Python 3.x.
* If you choose to use a throwaway email (chosen by default unless --email flag is used), then all emails sent to the throwaway will be opened and the download links followed by the WebDriver. This occurs once all albums have been emailed/otherwise downloaded.
* Closing the bandcamp browser window before all albums have been downloaded is fine and will end processing early. The links which have been emailed already will still be downloaded as long as the Guerrilla Mail window is left open.
