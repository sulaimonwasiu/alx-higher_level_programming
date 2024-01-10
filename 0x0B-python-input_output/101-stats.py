#!/usr/bin/env python3
"""Log parsing"""

import sys


def print_stats(total_size, status_codes):
    """Print stats"""
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """Parse a line"""
    parts = line.split()
    if len(parts) >= 7:
        return int(parts[-2]), parts[-1]
    return None, None


def main():
    """Main function"""
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            size, code = parse_line(line)
            if size is not None and code is not None:
                total_size += size
                status_codes[code] = status_codes.get(code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
