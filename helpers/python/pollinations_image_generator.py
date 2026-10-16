#!/usr/bin/env python3
"""
pollinations_image_generator.py
Zero-Key, Free AI Image Generator for Fiction Book Covers, Character Sheets, Comic Panels, and Reels Backgrounds.
Uses Pollinations.ai (FLUX / SDXL models) with an integrated High-Fidelity Prompt Enhancer.

Zero API Key Required. Works out of the box using Python standard library (urllib).

Usage:
  python pollinations_image_generator.py --prompt "fantasy castle floating above clouds" --output cover.png --aspect-ratio 2:3
"""

import sys
import os
import argparse
import urllib.request
import urllib.parse
import time

ASPECT_RATIOS = {
    "1:1": (1024, 1024),      # Square (Avatar, Character Portrait, Icon)
    "2:3": (1024, 1536),      # Portrait (Novel Cover, Wattpad Poster)
    "3:4": (960, 1280),       # Standard Book Print / Illustration
    "9:16": (768, 1360),      # Vertical Video (Reels, TikTok, Micro-Drama)
    "16:9": (1360, 768)       # Landscape (Cinematic Environment, Banner)
}

QUALITY_MODIFIERS = {
    "fantasy": "epic fantasy digital painting, cinematic volumetric lighting, ethereal magical glow, extremely detailed, artstation trending, 8k resolution, masterpiece",
    "romance": "cinematic romantic atmosphere, soft golden hour lighting, 85mm portrait photography, shallow depth of field, delicate emotional expressions, 8k, photorealistic",
    "scifi": "hyper-detailed sci-fi concept art, neon cyberpunk reflections, intricate mechanical details, cinematic widescreen lighting, 8k, unreal engine 5 render",
    "horror": "dark grim atmospheric horror, chiaroscuro dramatic shadows, foggy cold mist, hyper-detailed eerie digital art, cinematic suspense lighting, 8k",
    "anime": "high-end anime key visual, Makoto Shinkai aesthetic, vibrant emotional lighting, crisp line art, studio anime illustration, 8k resolution",
    "storybook": "charming children's book illustration, whimsical watercolor and soft pastel tones, cozy warm lighting, delightful character design, 8k, storybook masterpiece"
}

def enhance_prompt(base_prompt, style="fantasy"):
    """
    Enhances a simple prompt into an industry-grade, high-fidelity prompt.
    """
    modifier = QUALITY_MODIFIERS.get(style.lower(), QUALITY_MODIFIERS["fantasy"])
    if any(q_word in base_prompt.lower() for q_word in ["8k", "masterpiece", "trending", "cinematic"]):
        return base_prompt
    return f"{base_prompt}, {modifier}"

def generate_image(prompt, output_path, aspect_ratio="2:3", style="fantasy", model="flux", seed=None):
    width, height = ASPECT_RATIOS.get(aspect_ratio, (1024, 1536))
    final_prompt = enhance_prompt(prompt, style)
    
    encoded_prompt = urllib.parse.quote(final_prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&model={model}&nologo=true"
    if seed:
        url += f"&seed={seed}"
        
    print(f"\n[POLLINATIONS-AI] Requesting image...")
    print(f"  - Model: {model} (Zero-Key)")
    print(f"  - Aspect Ratio: {aspect_ratio} ({width}x{height}px)")
    print(f"  - Style: {style}")
    print(f"  - Enhanced Prompt: {final_prompt[:120]}...")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        start_time = time.time()
        with urllib.request.urlopen(req, timeout=60) as response:
            image_data = response.read()
            
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(image_data)
            
        duration = round(time.time() - start_time, 2)
        print(f"[SUCCESS] Image generated & saved to: {output_path} ({len(image_data)/1024:.1f} KB in {duration}s)\n")
        return output_path
    except Exception as e:
        print(f"[ERROR] Failed to fetch image from Pollinations.ai: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zero-Key AI Image Generator using Pollinations.ai")
    parser.add_argument("--prompt", required=True, help="Visual description prompt")
    parser.add_argument("--output", default="output.png", help="Path to save output image")
    parser.add_argument("--aspect-ratio", default="2:3", choices=list(ASPECT_RATIOS.keys()), help="Aspect ratio")
    parser.add_argument("--style", default="fantasy", choices=list(QUALITY_MODIFIERS.keys()), help="Art style modifier")
    parser.add_argument("--model", default="flux", choices=["flux", "turbo"], help="AI Model")
    parser.add_argument("--seed", type=int, default=None, help="Fixed random seed for consistency")
    
    args = parser.parse_args()
    generate_image(args.prompt, args.output, args.aspect_ratio, args.style, args.model, args.seed)
