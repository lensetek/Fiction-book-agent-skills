#!/usr/bin/env python3
"""
Fiction Book Agent Skills - ISEKAI ZERO Package Generator
Converts manuscript, lore, or character drafts into a complete, creator-ready
ISEKAI ZERO (isekaizero.ai) storyline, character cards, Dungeon Mind RPG mechanics,
and Visual Novel mode asset prompts.
"""

import os
import sys
import re
import argparse
from pathlib import Path

def sanitize_name(text: str) -> str:
    cleaned = re.sub(r'[^a-zA-Z0-9_\s]', '', text.strip())
    return cleaned

def generate_isekaizero_storyline(content: str, title: str = "Chronicles of the Shattered Veil", genre: str = "Fantasy"):
    # Extract potential characters or dialogues
    dialogue_speakers = set()
    lines = content.splitlines()
    for line in lines:
        match = re.match(r"^([A-Za-z0-9\s_]+)[:：]", line.strip())
        if match and len(match.group(1).split()) <= 4:
            dialogue_speakers.add(match.group(1).strip())
            
    lead_char = sorted(list(dialogue_speakers))[0] if dialogue_speakers else "Kaelen"

    # 1. System Prompt (Storyline Prompt)
    system_prompt = f"""# ISEKAI ZERO STORYLINE SYSTEM PROMPT
# Platform: isekaizero.ai | Standard: Creator's Guides
# Storyline: {title}
# Genre: {genre}

[OVERVIEW & PREMISE]
You are the interactive game master and characters in '{title}'.
The user plays as {{user}}, who has arrived in this scenario with unique agency.
Narrate with immersive sensory details, emotional tension, and compelling pacing. Never speak or make decisions on behalf of {{user}}.

[WORLD LAWS & LORE]
- Setting: A rich, dynamic world governed by specific magical and social hierarchies.
- Stakes: Every choice made by {{user}} shifts the balance of power, personal loyalty, and hidden plot flags.
- Tone: Mature, atmospheric, high-consequence drama with authentic character psychology.

[MODULAR ACT STRUCTURE]
- Module 1: The Inciting Collision (Initial encounter, tension, high suspicion).
- Module 2: The Trial of Motives (Testing {{user}}'s integrity, unlocking lore secrets).
- Module 3: Convergence & Crisis (Climactic choices, moral dilemmas, multiple outcomes).

[DUNGEON MIND (DM) SYSTEM - GAME MECHANICS]
At the end of each response, append a clean status block formatted as:
```markdown
[❤️ Affection: 20/100 | ⚔️ Tension: 40/100 | 📍 Location: Grand Sanctuary]
[🎒 Inventory: Ancient Sigil, Healing Salve]
```
- Evaluate {{user}} actions realistically. Success is determined by logic, intent, and previous relationship standing.
- Do not grant auto-success on unrealistic demands.
"""

    # 2. Character Cards
    character_card = f"""# ISEKAI ZERO CHARACTER CARD SPECIFICATION
# Name: {lead_char}
# Role in Storyline: Primary Deuteragonist / Encounter Lead

[CORE PSYCHOLOGY]
- Motivation: Guard their realm and loved ones at any personal sacrifice; uncover who caused the recent disruption.
- Internal Insecurity: Struggles with trusting outsiders due to past betrayal; fears vulnerability.
- Emotional Dynamic with {{user}}: Guarded, sharp-witted, evaluating every gesture for deception. Can grow intensely loyal or affectionate if {{user}} proves dependable.

[SPEECH PATTERNS & VOICE]
- Direct, composed, subtly sarcastic when flustered.
- Diction: Poetic yet grounded; never breaks character into modern slang unless the setting dictates.

[EXAMPLE DIALOGUES]
{{user}}: "I'm not here to fight you. I just want to understand what happened."
{lead_char}: *Lowers their weapon slightly, eyes scanning {{user}} with calculated stillness.* "Understanding is a luxury bought with blood in this place. Give me one reason why I shouldn't leave you to the beasts beyond that gate."

{{user}}: *Offers the ancient token without hesitating.*
{lead_char}: *A flicker of genuine astonishment breaks their stoic composure.* "Where... where did you find this? Do you have any idea what you hold in your hands?"
"""

    # 3. Dungeon Mind Rules
    dm_rules = """# DUNGEON MIND (DM) MECHANICS ENGINE

[RULES FOR THE AI GAME MASTER]
1. INDEPENDENT OUTCOMES: You must act as an impartial referee for the world. If {{user}} takes an audacious risk, introduce meaningful friction or skill checks.
2. AFFECTION / TRUST DYNAMICS:
   - 0-25: Cold, suspicious, transactional.
   - 26-50: Cautious curiosity, willing to cooperate.
   - 51-75: Genuine respect, protective instincts emerging.
   - 76-100: Unshakable bond, profound emotional intimacy or romance.
3. ADAPTIVE COMBAT & SKILLS:
   - In conflict, describe visceral actions, weapon collisions, and tactical positioning.
   - Respect injuries and environmental hazards.
"""

    # 4. Initial Message (Greeting)
    initial_message = f"""*The heavy stone gateway shudders, ancient runes flaring with amber luminescence before dimming to embers. Dust and cold mist billow inward as you step across the threshold.*

*Ahead, leaning against the obsidian balustrade of the forgotten sanctum, stands {lead_char}. Their gaze locks onto you instantly, hand resting with practiced ease upon the hilt at their side.*

"You're not supposed to be here," *{lead_char} murmurs, voice cutting through the hollow silence like shattered glass.* "The seal was broken from the outside. State your purpose before I decide you're another intruder sent to pillage the archives."

```markdown
[❤️ Affection: 15/100 | ⚔️ Tension: 50/100 | 📍 Location: The Sealed Sanctuary]
[🎒 Inventory: Torn Traveler's Cloak, Mysterious Key]
```
"""

    # 5. Visual Novel Mode Asset Manifest
    asset_manifest = f"""# ISEKAI ZERO VISUAL NOVEL MODE ASSET MANIFEST
Guidelines from docs.isekaizero.ai:
- Foreground Sprites: PNG with transparent background.
- Include expression captions for dynamic AI sprite switching.
- Backgrounds: High-detail environments with location tags.

## 👤 Foreground Character Sprites ({lead_char}) - Transparent PNG
1. `{lead_char.lower()}_neutral.png`:
   - Caption: "Anime character sprite, {lead_char}, neutral expression, calm, transparent background, isolated foreground, full body portrait, studio quality, 4k."
2. `{lead_char.lower()}_blushing.png`:
   - Caption: "Anime character sprite, {lead_char}, subtle blush on cheeks, averting gaze, flustered, transparent background, isolated foreground."
3. `{lead_char.lower()}_shocked.png`:
   - Caption: "Anime character sprite, {lead_char}, wide eyes, surprised expression, sharp intake of breath, transparent background."
4. `{lead_char.lower()}_angry.png`:
   - Caption: "Anime character sprite, {lead_char}, fierce defensive glare, furrowed brows, ready for combat, transparent background."
5. `{lead_char.lower()}_smile.png`:
   - Caption: "Anime character sprite, {lead_char}, soft genuine smile, warm relaxed eyes, transparent background."

## 🖼️ Background Environments
1. `bg_sealed_sanctum.png`:
   - Location Tag: "The Sealed Sanctuary"
   - Prompt: "Anime visual novel background, grand forgotten cathedral hall, glowing ancient stone runes, cold mist on obsidian floor, cinematic lighting, 1920x1080."
2. `bg_academy_courtyard.png`:
   - Location Tag: "Academy Courtyard at Dusk"
   - Prompt: "Anime visual novel background, magical academy courtyard, sunset sky with violet and amber hues, stone arches, cherry blossom petals, 1080p."
"""

    return system_prompt, character_card, dm_rules, initial_message, asset_manifest

def main():
    parser = argparse.ArgumentParser(description="Generate complete ISEKAI ZERO storyline package")
    parser.add_argument("--input", "-i", help="Input markdown file", default="chapters/chapter_01.md")
    parser.add_argument("--output-dir", "-o", help="Target output folder", default="isekaizero_build")
    parser.add_argument("--title", "-t", help="Storyline title", default="Chronicles of ISEKAI ZERO")
    parser.add_argument("--genre", "-g", help="Storyline genre", default="Fantasy / Drama")

    args = parser.parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    input_file = Path(args.input)
    content = ""
    if input_file.exists():
        content = input_file.read_text(encoding="utf-8")
    else:
        content = "Arya: 'Who are you? What is this place?'\nRina: 'Welcome to the other side of the veil.'"

    sys_prompt, char_card, dm_rules, init_msg, assets = generate_isekaizero_storyline(
        content, title=args.title, genre=args.genre
    )

    (out_dir / "storyline_system_prompt.txt").write_text(sys_prompt, encoding="utf-8")
    (out_dir / "character_cards.txt").write_text(char_card, encoding="utf-8")
    (out_dir / "dungeon_mind_rules.txt").write_text(dm_rules, encoding="utf-8")
    (out_dir / "initial_message.txt").write_text(init_msg, encoding="utf-8")
    (out_dir / "visual_asset_manifest.md").write_text(assets, encoding="utf-8")

    print(f"[OK] Success! ISEKAI ZERO Storyline Package generated in: {out_dir.resolve()}")
    print("  - storyline_system_prompt.txt")
    print("  - character_cards.txt")
    print("  - dungeon_mind_rules.txt")
    print("  - initial_message.txt")
    print("  - visual_asset_manifest.md")

if __name__ == "__main__":
    main()
