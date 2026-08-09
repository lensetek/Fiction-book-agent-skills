#!/usr/bin/env python3
"""
generate_comic_prompts.py
Parses comic/webtoon scripts in Markdown format and extracts AI image generation prompts for artists/illustrators.
Outputs a JSON / Markdown file with visual prompts per panel.
"""

import sys
import os
import re
import json
import argparse

def extract_prompts(script_path, output_path):
    if not os.path.exists(script_path):
        print(f"Error: File not found: {script_path}")
        sys.exit(1)

    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()

    panels = re.findall(r'### Panel (\d+)[\s\S]*?- \*\*AI Visual Prompt\*\*:\s*(`.*`|.*)', content)
    
    extracted_data = []
    for panel_num, prompt_text in panels:
        clean_prompt = prompt_text.strip('` ').strip()
        extracted_data.append({
            "panel": f"Panel {panel_num}",
            "prompt": clean_prompt
        })

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Extracted {len(extracted_data)} panel visual prompts to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Comic Panel AI Prompt Extractor")
    parser.add_argument("--input", required=True, help="Path to comic script markdown file")
    parser.add_argument("--output", required=True, help="Path to output JSON file")
    args = parser.parse_args()
    extract_prompts(args.input, args.output)
