import logging
import os
import glob
import shutil

logger = logging.getLogger("splitsong")


def splitsong_parser(subparser):
    """
    splitsong_parser Is the parser for splitsong with all the needed options to run the script.
    """
    cmd_parser = subparser.add_parser(
        "splitsong",
        help="Script to download and demucs a song."
    )

    cmd_parser.add_argument("-s", "--song_link", help="Song link.", type=str,
                            required=True)
    cmd_parser.set_defaults(func=splitsong)


def splitsong(args):

    song_link = args.song_link

    os.system(f'spotdl {song_link}')
    mp3_files = get_file_names()

    print ("Files found:")
    for file in mp3_files:
        print(file)

    for file in mp3_files:
        os.system(f'demucs "{file}"')
        print("Completed demucs!")
        shutil.move(file, f'data/{file}')
        print(f'{file} moved to data/')

def get_file_names():
    mylist = [f for f in glob.glob("*.mp3")]
    return mylist