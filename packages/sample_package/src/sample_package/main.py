"""Placeholder docstring."""

import argparse


def main() -> None:
    """Print a greeting message from the datagen module."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--message", default="not provided")
    args = parser.parse_args()

    print(f"Hello from sample package! message: {args.message}")


if __name__ == "__main__":
    main()
