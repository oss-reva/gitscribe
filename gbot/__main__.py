
import sys
import argparse


def main(argv=sys.argv[1:]):
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", action="version", version="0.1.0")

    args = ap.parse_args(argv)


if __name__ == "__main__":
    main()
