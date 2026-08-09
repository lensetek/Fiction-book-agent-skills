#!/usr/bin/env python3
"""
generate_braille_text.py
Converts standard fiction prose (Indonesian & English) into Unicode Braille Patterns (U+2800..U+28FF).
Supports Dual-Format (Twin-Vision: Text + Braille below) or Braille-Only output.
"""

import sys
import os
import argparse

# Standard Grade-1 Braille Unicode Character Map (Bahasa Indonesia & UEB)
LATIN_TO_BRAILLE = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠯',
    'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏',
    'q': '⠟', 'r': '⠌', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵',
    'A': '⠁', 'B': '⠃', 'C': '⠉', 'D': '⠙', 'E': '⠑', 'F': '⠋', 'G': '⠛', 'H': '⠯',
    'I': '⠊', 'J': '⠚', 'K': '⠅', 'L': '⠇', 'M': '⠍', 'N': '⠝', 'O': '⠕', 'P': '⠏',
    'Q': '⠟', 'R': '⠌', 'S': '⠎', 'T': '⠞', 'U': '⠥', 'V': '⠧', 'W': '⠺', 'X': '⠭',
    'Y': '⠽', 'Z': '⠵',
    '0': '⠼⠚', '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑',
    '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠯', '9': '⠼⠊',
    ' ': ' ', ',': '⠂', '.': '⠲', '!': '⠔', '?': '⠦', ';': '⠆', ':': '⠿',
    '-': '⠤', '"': '⠶', "'": '⠄', '(': '⠶', ')': '⠶'
}

def convert_to_braille(text):
    """Translates a text string into Grade-1 Unicode Braille characters."""
    braille_chars = []
    for char in text:
        braille_chars.append(LATIN_TO_BRAILLE.get(char, char))
    return "".join(braille_chars)

def process_manuscript(input_path, output_path, mode="dual"):
    if not os.path.exists(input_path):
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    for line in lines:
        raw_text = line.strip()
        if not raw_text:
            output_lines.append("\n")
            continue

        braille_text = convert_to_braille(raw_text)

        if mode == "dual":
            # Interlined Twin-Vision: Original text + Braille Unicode below
            output_lines.append(f"{raw_text}\n")
            output_lines.append(f"⠎⠞⠁⠌⠞ [Braille]: {braille_text}\n\n")
        else:
            # Braille-Only
            output_lines.append(f"{braille_text}\n")

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"[SUCCESS] Braille conversion complete ({mode} mode): {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prose to Braille Unicode Converter")
    parser.add_argument("--input", required=True, help="Path to input markdown file")
    parser.add_argument("--output", required=True, help="Path to output markdown/text file")
    parser.add_argument("--mode", default="dual", choices=["dual", "braille-only"], help="Conversion mode")
    
    args = parser.parse_args()
    process_manuscript(args.input, args.output, args.mode)
