#!/usr/bin/env python3

import sys
import subprocess
import argparse
import os
import binascii

def extract_game_code(file_path):
    """
    Extracts the Game Code from the ROM using ndstools.

    Args:
        file_path (str): Path to the ROM file.

    Returns:
        str: The Game Code (e.g., 'IPKE') or None if extraction fails.
    """
    try:
        # Run the ndstools command
        result = subprocess.run(
            ['ndstool', '-i', file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        
        # Parse the output to find the Game Code line
        for line in result.stdout.splitlines():
            if 'Game code' in line:
                # Example line:
                # 0x0C	Game code                	IPKE (NTR-IPKE-USA)
                parts = line.split('\t')
                if len(parts) >= 3:
                    game_code_full = parts[2].strip()
                    # Extract the first 4 characters as Game Code
                    game_code = game_code_full[:4]
                    return game_code.upper()
        print(f"Error: Game code not found in ndstools output for '{file_path}'.", file=sys.stderr)
        return None
    except FileNotFoundError:
        print("Error: 'ndstool' command not found. Please ensure ndstools is installed and in your PATH.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error running ndstools on '{file_path}': {e.stderr}", file=sys.stderr)
        return None

def calculate_jamcrc(file_path, header_size=512):
    """
    Calculates the JAMCRC (bitwise NOT of CRC-32) of the ROM header.

    Args:
        file_path (str): Path to the ROM file.
        header_size (int): Number of bytes to read from the header (default: 512).

    Returns:
        str: The JAMCRC as an 8-character hexadecimal string (e.g., '4DFFBF91') or None if calculation fails.
    """
    try:
        with open(file_path, 'rb') as f:
            header = f.read(header_size)
            if not header:
                print(f"Error: File '{file_path}' is empty or cannot be read.", file=sys.stderr)
                return None
            # Compute CRC32
            crc32 = binascii.crc32(header) & 0xFFFFFFFF
            # Compute JAMCRC by applying bitwise NOT
            jamcrc = (~crc32) & 0xFFFFFFFF
            # Format as uppercase hexadecimal without '0x', zero-padded to 8 characters
            return f"{jamcrc:08X}"
    except Exception as e:
        print(f"Error calculating JAMCRC for '{file_path}': {e}", file=sys.stderr)
        return None

def generate_gameid(file_path):
    """
    Generates the GameID by extracting the Game Code and calculating the JAMCRC.

    Args:
        file_path (str): Path to the ROM file.

    Returns:
        str: The GameID in the format '<GameCode> <JAMCRC>' or None if any step fails.
    """
    game_code = extract_game_code(file_path)
    if not game_code:
        return None
    jamcrc = calculate_jamcrc(file_path)
    if not jamcrc:
        return None
    return f"{game_code} {jamcrc}"

def main():
    parser = argparse.ArgumentParser(description='Generate GameID by extracting Game Code and calculating JAMCRC.')
    parser.add_argument('files', metavar='FILE', nargs='+', help='Nintendo DS ROM files to process')
    args = parser.parse_args()

    for file_path in args.files:
        if not os.path.isfile(file_path):
            print(f"Skipping '{file_path}': Not a regular file.", file=sys.stderr)
            continue

        gameid = generate_gameid(file_path)
        if gameid:
            print(gameid)
        else:
            print(f"Failed to generate GameID for '{file_path}'.", file=sys.stderr)

if __name__ == "__main__":
    main()
