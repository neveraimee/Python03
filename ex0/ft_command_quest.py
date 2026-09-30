#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    args = len(sys.argv) - 1
    print(f"Program name: {sys.argv[0]}")
    if (args == 0):
        print("No arguments provided!")
    else:
        print(f"Arguments recieved: {args}")
        i = 1
        while (i <= args):
            print(f"Arguement {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {args + 1}")


if __name__ == "__main__":
    main()
