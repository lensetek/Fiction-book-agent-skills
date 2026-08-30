#!/usr/bin/env python3
"""
format_wattpad_chapters.py
Automated Wattpad Episode Serializer & Metadata Generator for Fiction Manuscripts.

Features:
- Splits long markdown manuscript files into Wattpad-friendly episodes (1,500 - 2,500 words).
- Appends top/bottom Author Notes (A/N) with Vote ⭐ & Comment Call-To-Actions.
- Generates wattpad_story_setup.md with Wattpad Hook Synopsis, 25 Trending Tags, Rating, and 2:3 Cover Specs.
"""

import sys
import os
import argparse
import re

DEFAULT_WATTPAD_TAGS = [
    "#indonesia", "#wattpadindonesia", "#fiksi", "#novel", "#romance",
    "#teenfiction", "#fantasy", "#slowburn", "#badboy", "#ceo",
    "#enemiestolovers", "#fakerelationship", "#marriagelife", "#bikinbaper",
    "#drama", "#angst", "#chicklit", "#love", "#fiction", "#youngadult",
    "#popular", "#bestseller", "#series", "#webnovel", "#mustread"
]

TOP_AN_TEMPLATE = """> **Author Note (A/N):**
> Selamat membaca **{chapter_title}**! ❤️
> Jangan lupa klik tombol **Bintang ⭐ (Vote)** di bawah sebelum membaca ya!

---

"""

BOTTOM_AN_TEMPLATE = """

---

***
> **Gimana menurut kalian bab ini?** Sampaikan pendapat dan teori kalian di kolom komentar ya! 💬
> Jangan lupa tekan tombol **VOTE ⭐** dan tambahkan cerita ini ke **Library / Reading List** kalian agar tidak ketinggalan kelanjutan bab selanjutnya!
> 
> *Sampai jumpa di bab berikutnya! ✨*
"""

def split_into_chapters(md_content):
    # Regex split by level 1 or 2 headings (e.g. # Bab 1 or ## Chapter 1)
    chapter_blocks = re.split(r'(?m)^(?:#|##)\s+(.+)$', md_content)
    chapters = []
    
    if len(chapter_blocks) == 1:
        # No headings found, treat whole text as one chapter
        chapters.append(("Bab 1: Episode Utama", chapter_blocks[0].strip()))
    else:
        # Block 0 is text before first heading
        preamble = chapter_blocks[0].strip()
        if preamble:
            chapters.append(("Prolog / Pendahuluan", preamble))
            
        for i in range(1, len(chapter_blocks), 2):
            title = chapter_blocks[i].strip()
            content = chapter_blocks[i+1].strip() if i+1 < len(chapter_blocks) else ""
            chapters.append((title, content))
            
    return chapters

def split_long_chapter(title, content, target_words=2000):
    words = content.split()
    total_words = len(words)
    
    if total_words <= 3000:
        return [(title, content)]
        
    # Split into 2 parts
    mid_point = total_words // 2
    paragraphs = content.split('\n\n')
    
    part1_paras = []
    part2_paras = []
    current_count = 0
    
    for p in paragraphs:
        p_words = len(p.split())
        if current_count < mid_point:
            part1_paras.append(p)
            current_count += p_words
        else:
            part2_paras.append(p)
            
    part1_text = '\n\n'.join(part1_paras)
    part2_text = '\n\n'.join(part2_paras)
    
    return [
        (f"{title} (Bagian 1)", part1_text),
        (f"{title} (Bagian 2)", part2_text)
    ]

def generate_wattpad_setup(title, author, tags=None):
    if not tags:
        tags = DEFAULT_WATTPAD_TAGS
        
    tag_str = " ".join(tags)
    
    setup_md = f"""# Wattpad Story Setup & Metadata

## General Metadata
- **Judul Wattpad**: {title}
- **Penulis**: {author}
- **Kategori Utama**: Romance / Teen Fiction / Fantasy
- **Content Rating**: General (Semua Umur) / Mature (18+)
- **Bahasa**: Bahasa Indonesia

---

## Wattpad Hook Synopsis (Sinopsis Wattpad)
> *"Kutipan dialog paling berkesan / misterius dari cerita Anda."*

[Tulis sinopsis ringkas 2 paragraf di sini. Paragraf 1: Pengenalan konflik & karakter utama. Paragraf 2: Pertanyaan taruhan tinggi yang membuat pembaca penasaran!]

---

## Trending Wattpad Search Hashtags (25 Tags)
```text
{tag_str}
```

---

## Wattpad Cover Specification (Rasio 2:3 / 512x800 px)
- **Dimensi Rekomendasi**: 512 x 800 piksel atau 1024 x 1600 piksel (Rasio 2:3).
- **FAL.ai / Midjourney Prompt**:
  `vibrant wattpad book cover art, {title}, main character portrait in dramatic lighting, emotional atmosphere, 8k resolution, aspect ratio 2:3`
"""
    return setup_md

def format_wattpad(input_path, output_dir, title, author):
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)
        
    with open(input_path, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Generate Story Setup
    setup_content = generate_wattpad_setup(title, author)
    setup_path = os.path.join(output_dir, "wattpad_story_setup.md")
    with open(setup_path, "w", encoding="utf-8") as f:
        f.write(setup_content)
    print(f"[CREATED] Wattpad setup metadata: {setup_path}")
    
    # 2. Split Chapters into Episodes
    raw_chapters = split_into_chapters(md_content)
    final_episodes = []
    
    for c_title, c_content in raw_chapters:
        eps = split_long_chapter(c_title, c_content)
        final_episodes.extend(eps)
        
    # 3. Write Episode Files
    for idx, (ep_title, ep_body) in enumerate(final_episodes, start=1):
        filename = f"episode_{idx:03d}.md"
        filepath = os.path.join(output_dir, filename)
        
        top_an = TOP_AN_TEMPLATE.format(chapter_title=ep_title)
        bottom_an = BOTTOM_AN_TEMPLATE
        
        full_episode_text = f"# {ep_title}\n\n{top_an}{ep_body}{bottom_an}"
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_episode_text)
            
        word_count = len(ep_body.split())
        print(f"  -> Generated {filename}: {ep_title} ({word_count} words)")
        
    print(f"\n[SUCCESS] Wattpad serialization completed! {len(final_episodes)} episodes written to '{output_dir}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wattpad Episode Serializer & Metadata Generator")
    parser.add_argument("--input", required=True, help="Path to manuscript Markdown file")
    parser.add_argument("--output-dir", default="wattpad_build", help="Output directory for Wattpad files")
    parser.add_argument("--title", default="Judul Novel Wattpad", help="Wattpad Story Title")
    parser.add_argument("--author", default="Penulis", help="Author Name")
    
    args = parser.parse_args()
    format_wattpad(args.input, args.output_dir, args.title, args.author)
