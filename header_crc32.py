#!/usr/bin/env python3

import sys
import binascii
import argparse
import os

def calculate_jamcrc(file_path, header_size=512):
    try:
        with open(file_path, 'rb') as f:
            header = f.read(header_size)
            # Compute CRC32 using binascii
            crc = binascii.crc32(header) & 0xFFFFFFFF
            # Compute JAMCRC by applying bitwise NOT
            jamcrc = ~crc & 0xFFFFFFFF
            return jamcrc
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return None

def main():
    parser = argparse.ArgumentParser(description='Calculate JAMCRC (bitwise NOT of CRC-32) of file headers (first 512 bytes).')
    parser.add_argument('files', metavar='FILE', nargs='+', help='Files to process')
    args = parser.parse_args()

    for file_path in args.files:
        if not os.path.isfile(file_path):
            print(f"Skipping {file_path}: Not a regular file.", file=sys.stderr)
            continue

        jamcrc = calculate_jamcrc(file_path)
        if jamcrc is not None:
            print(f"{file_path}: 0x{jamcrc:08X}")

if __name__ == "__main__":
    main()
