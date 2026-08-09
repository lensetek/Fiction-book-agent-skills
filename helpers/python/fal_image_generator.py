#!/usr/bin/env python3
"""
fal_image_generator.py
Fal.ai (Flux.1 Schnell / Dev) Image Generation CLI Helper for Comic Panels, Storybooks, and Novel Covers.

Requires environment variable: FAL_KEY
Get key at: https://fal.ai/dashboard/keys
"""

import sys
import os
import json
import urllib.request
import urllib.error
import argparse

def generate_fal_image(prompt, output_path, model="fal-ai/flux/schnell", aspect_ratio="16:9"):
    fal_key = os.environ.get("FAL_KEY")
    if not fal_key:
        print("[WARNING] FAL_KEY environment variable is not set!")
        print("To enable automatic image generation via Fal.ai:")
        print("  1. Get your API key from https://fal.ai/dashboard/keys")
        print("  2. Set environment variable: export FAL_KEY=\"your_key_here\"")
        print("  3. Or add FAL_KEY=\"your_key_here\" in a local .env file")
        print(f"\nPrompt saved for manual generation: '{prompt}'")
        sys.exit(0)

    url = f"https://fal.run/{model}"
    
    # Map aspect ratio to Fal.ai image size
    size_map = {
      "16:9": "landscape_16_9",
      "9:16": "portrait_16_9",
      "1:1": "square_hd",
      "4:3": "landscape_4_3",
      "3:4": "portrait_4_3"
    }
    image_size = size_map.get(aspect_ratio, "landscape_16_9")

    payload = {
        "prompt": prompt,
        "image_size": image_size,
        "num_inference_steps": 4,
        "enable_safety_checker": True
    }

    headers = {
        "Authorization": f"Key {fal_key}",
        "Content-Type": "application/json"
    }

    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            res_json = json.loads(res_body)

        images = res_json.get("images", [])
        if not images or not images[0].get("url"):
            print("[ERROR] No image URL returned from Fal.ai API response.")
            sys.exit(1)

        img_url = images[0]["url"]
        
        # Download image file
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        urllib.request.urlretrieve(img_url, output_path)
        print(f"[SUCCESS] Fal.ai Image generated successfully: {output_path}")
        print(f"Model used: {model} | Aspect Ratio: {aspect_ratio}")

    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8')
        print(f"[ERROR] Fal.ai API Request Failed (HTTP {e.code}): {err_msg}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fal.ai Flux.1 Image Generator")
    parser.add_argument("--prompt", required=True, help="Text prompt for image generation")
    parser.add_argument("--output", required=True, help="Output image file path (.png / .jpg)")
    parser.add_argument("--model", default="fal-ai/flux/schnell", help="Fal.ai Model ID")
    parser.add_argument("--aspect-ratio", default="16:9", choices=["16:9", "9:16", "1:1", "4:3", "3:4"], help="Aspect Ratio")
    
    args = parser.parse_args()
    generate_fal_image(args.prompt, args.output, args.model, args.aspect_ratio)
