import json
from engine import *
from utils import *
import argparse
import os

def compress_file(input_path, output_path):
    try:
        with open(input_path, 'r') as f:
            text = f.read()

        root = build_tree(text)
        codes = get_codes(root)

        encoded_text = "".join([codes[char]for char in text])
        compressed_data = pack_bits(encoded_text)

        with open(output_path, 'wb') as f:
            header = json.dumps(codes).encode('utf-8')
            f.write(header)
            f.write(b"###")
            f.write(compressed_data)
            print(f"Compression complete! Saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing the files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    orig_size = os.path.getsize(input_path)
    comp_size = os.path.getsize(output_path)
    savings = (1 - (comp_size / orig_size)) * 100

    print(f"Original Size: {orig_size} bytes")
    print(f"Compressed Size: {comp_size} bytes")
    print(f"Space Saved: {savings:.2f}%")

def decompress_file(input_path, output_path):
    with open(input_path, 'rb') as f:
        content = f.read()
    try:
        header_data, compressed_data = content.split(b'###', 1)
    except ValueError:
        print("Error: This file is not a valid Huffman archive (missing '###' separator).")
        return
    codes = json.loads(header_data.decode('utf-8'))

    reverse_codes = {v: k for k, v in codes.items()}

    bit_string = unpack_bits(compressed_data)

    decoded_text = ""
    current_bits = ""
    for bit in bit_string:
        current_bits += bit
        if current_bits in reverse_codes:
            decoded_text += reverse_codes[current_bits]
            current_bits = ""

    with open(output_path, 'w') as f:
        f.write(decoded_text)
    print(f"Decompression complete! Saved to {output_path}")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Huffman Coding File Archiver")
    parser.add_argument("action", choices=["compress", "decompress"], help="Choose action")
    parser.add_argument("input", help="Path to the input file")
    parser.add_argument("output", help="Path to save the result")

    args = parser.parse_args()

    if args.action == "compress":
        compress_file(args.input, args.output)
    else:
        decompress_file(args.input, args.output)