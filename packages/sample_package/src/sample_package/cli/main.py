"""Placeholder docstring."""

import argparse
from typing import Optional, Sequence


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Print a greeting message from the datagen module."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", default="not provided")
    args, _ = parser.parse_known_args(argv)

    print(f"Hello from sample package! message: {args.message}")


if __name__ == "__main__":
    main()
