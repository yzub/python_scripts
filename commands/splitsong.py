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
        help="Script to download and demucs song(s)."
    )

    cmd_parser.add_argument("-s", "--song_links", type=str, default=None,
                            help="Comma separated string containing song links.")
    cmd_parser.set_defaults(func=splitsong)


def splitsong(args):
    input = args.song_links

    if input:
        songs_list = input.split(",")

        for song_url in songs_list:
            os.system(f'spotdl {song_url}')

    mp3_files = get_file_names()

    print("Files found:")
    for file in mp3_files:
        print(file)

    for file in mp3_files:
        os.system(f'demucs "{file}"')
        print("Completed demucs!")
        shutil.move(file, f'data/{file}')
        print(f'{file} moved to data/')


def get_file_names():
    return [f for f in glob.glob("*.mp3")]
