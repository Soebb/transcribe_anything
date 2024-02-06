"""
    Entry point for running the transcribe-anything prgram.
"""

import argparse
import sys

from transcribe_anything.api import transcribe


def main() -> None:
    """Main entry point for the command line tool."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "url_or_file",
        help="Provide file path or url (includes youtube/facebook/twitter/etc)",
    )
    parser.add_argument(
        "--out",
        help="Output text file name",
        default=None,
    )
    args = parser.parse_args()
    transcribe(url_or_file=args.url_or_file, output_file=args.out if args.out else False)


if __name__ == "__main__":
    main()
    sys.exit(0)
