#!/usr/bin/env python

import argparse
import os
import sys

import dotenv
dotenv.load_dotenv()


def run(token):
    from gitscribe import bot

    bot.run(token)


def main(argv=sys.argv[1:]):
    ap = argparse.ArgumentParser(description='Runtime for the Discord Bot')
    ap.add_argument(
        '--token',
        default=os.getenv("DISCORD_BOT_TOKEN"),
        type=str,
        help='The Discord Bot Token'
    )

    args = ap.parse_args(argv)

    if args.token is None:
        raise ValueError(
            "A Discord Bot token is required (--token HERE), or a .env file works")

    # Run the bot
    run(args.token)


if __name__ == '__main__':
    main()
