#!/usr/bin/env python3
"""
generate_market_keywords.py
Parses Market Research Markdown reports and extracts structured tags, category lists, and title options for KDP/Webtoon publishing.
"""

import sys
import os
import re
import json
import argparse

def parse_market_report(report_path, output_path):
    if not os.path.exists(report_path):
        print(f"Error: File not found: {report_path}")
        sys.exit(1)

    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    tags = re.findall(r'-\s*Tag \d+:\s*(.*)', content)
    titles = re.findall(r'-\s*\*\*Title\*\*:\s*(.*)', content)

    extracted_data = {
        "title_candidates": [t.strip() for t in titles if t.strip()],
        "search_keywords": [tag.strip() for tag in tags if tag.strip()]
    }

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Extracted market keywords to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Market Research Keyword Extractor")
    parser.add_argument("--input", required=True, help="Path to market research markdown report")
    parser.add_argument("--output", required=True, help="Path to output JSON file")
    args = parser.parse_args()
    parse_market_report(args.input, args.output)
