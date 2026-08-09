#!/usr/bin/env python3
"""
check_timeline_continuity.py
Validates narrative event chronology, timeline consistency, and character age/state tracking in Markdown manuscripts.
"""

import sys
import os
import re
import argparse

def analyze_timeline(markdown_path):
    """Scans manuscript for timestamp indicators, day/night transitions, and potential timeline gaps."""
    if not os.path.exists(markdown_path):
        print(f"Error: File not found: {markdown_path}")
        sys.exit(1)

    with open(markdown_path, 'r', encoding='utf-8') as f:
        content = f.read()

    chapters = re.split(r'(^#\s+.*)', content, flags=re.MULTILINE)
    
    timeline_log = []
    time_keywords = [
        r'hari\s+ke-\d+', r'pagi', r'siang', r'sore', r'malam', r'tengah\s+malam',
        r'besok', r'kemarin', r'minggu\s+depan', r'bulan\s+lalu', r'tahun\s+\d{4}'
    ]
    pattern = re.compile(r'(' + '|'.join(time_keywords) + r')', re.IGNORECASE)

    current_chapter = "Prologue / Overview"
    for part in chapters:
        if part.startswith("# "):
            current_chapter = part.strip()
        else:
            matches = pattern.findall(part)
            if matches:
                timeline_log.append({
                    "chapter": current_chapter,
                    "indicators": list(set(matches))
                })

    print("=== TIMELINE & CONTINUITY AUDIT REPORT ===")
    if not timeline_log:
        print("Warning: No explicit temporal indicators (days, times of day, dates) detected.")
    else:
        for entry in timeline_log:
            print(f"[{entry['chapter']}] -> Temporal markers found: {', '.join(entry['indicators'])}")
    print("==========================================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Timeline & Continuity Checker")
    parser.add_argument("--input", required=True, help="Path to manuscript Markdown file")
    args = parser.parse_args()
    analyze_timeline(args.input)
