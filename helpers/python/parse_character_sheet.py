#!/usr/bin/env python3
"""
parse_character_sheet.py
Parses Markdown character profile sheets and extracts structured character data for consistency auditing.
"""

import sys
import os
import re
import json
import argparse

def parse_character_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found {file_path}")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    character_data = {}
    
    # Extract fields based on bold headers e.g. **Full Name**: John Doe
    field_matches = re.findall(r'\*\*(.*?)\*\*:\s*(.*)', content)
    for key, val in field_matches:
        character_data[key.strip()] = val.strip()

    print(json.dumps(character_data, indent=2, ensure_ascii=False))
    return character_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Character Sheet Parser")
    parser.add_argument("--input", required=True, help="Path to character sheet markdown file")
    args = parser.parse_args()
    parse_character_file(args.input)
