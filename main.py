import os
import sys

LINE = "My smart fridge locks at midnight, then its app offers to order more food I can't reach either."


def main():
    if not (1 <= len(LINE) <= 200) or "\n" in LINE or not LINE.strip():
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
