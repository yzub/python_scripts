#!/usr/bin/env python
import argparse
import logging

from commands.splitsong import splitsong_parser

logger = logging.getLogger("script-start")


def main():
    """
    Main is the entry point for the client interface.
    It configures a main argparse and the logging based on one of the arguments provided.
    """
    parser = argparse.ArgumentParser(prog="start")
    parser.add_argument("--verbose", "-v", help="Sets the verbose mode", action="store_true")

    subparser = parser.add_subparsers(help="sub-command help")

    # Config parsers
    splitsong_parser(subparser)

    args = parser.parse_args()

    # Set the verbose level
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=log_level
    )
    logger.debug("verbose mode set")

    args.func(args)


if __name__ == "__main__":
    main()
