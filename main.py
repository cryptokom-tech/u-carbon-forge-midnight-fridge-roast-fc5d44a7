import os
import sys

LINE = "My smart fridge locks at midnight, then its app offers to order more food I can't reach either."


def validate(line):
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


def main():
    try:
        validate(LINE)
    except ValueError:
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
