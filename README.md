# python_scripts

### 1. Installation

Create python virtual environment:

```
python3 -m venv env
source env/bin/activate

on windows:
.\env\Scripts\activate
```

Install Python packages dependencies:

```
pip3 install -r $PWD/requirements.txt

```

### Use commands

To use the commands the user must call the main script, *scripts*. The script uses argparse and includes the helper that
shows how to use it and the multiple commands available, e.g.,

```
$ python scripts.py -h

usage: start [-h] [--verbose] {splitsong} ...

positional arguments:
  {splitsong}    sub-command help
    splitsong    Script to download and demucs a song.

optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v         Sets the verbose mode
```

#### Split song

Splits song given a song url link.
```
$ python scripts.py splitsong -h 
usage: start splitsong [-h] -s SONG_LINK

options:
  -h, --help            show this help message and exit
  -s SONG_LINK, --song_link SONG_LINK
                        Song link.

```
