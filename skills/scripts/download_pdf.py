#!/usr/bin/env python3
import argparse
import logging
import sys
import urllib.request


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download a PDF from a URL.")
    parser.add_argument("--url", required=True, help="PDF URL to download")
    parser.add_argument("--output", required=True, help="Output file path")
    return parser.parse_args()


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    args = parse_args()

    try:
        urllib.request.urlretrieve(args.url, args.output)
        logging.info("Downloaded to %s", args.output)
        return 0
    except Exception as exc:
        logging.exception("Download failed: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
