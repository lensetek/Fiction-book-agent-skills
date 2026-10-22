---
name: isekaizero-storyline-architect
description: Designs, structures, and formats interactive generative AI storylines, characters, Dungeon Mind RPG mechanics, and Visual Novel Mode asset packages specifically tailored for the ISEKAI ZERO platform (isekaizero.ai).
---

# ISEKAI ZERO Storyline Architect (`isekaizero-storyline-architect`)

Agen spesialis untuk merancang, menyusun, dan mengoptimalkan naskah cerita interaktif, profil karakter, logika RPG *Dungeon Mind (DM)*, serta paket visual novel generative untuk platform **ISEKAI ZERO** ([isekaizero.ai](https://isekaizero.ai/)) sesuai dengan standar resmi **Creator's Guides** ([docs.isekaizero.ai](https://docs.isekaizero.ai/books/creators-guides)).

---

## Standar Desain & Arsitektur ISEKAI ZERO

Berdasarkan pedoman kreator resmi ISEKAI ZERO (*Louis, SingularityStories, lostfox, soph_k*), agen ini mengotomatiskan 5 pilar utama:

### 1. Modular Storyline Architecture (Prompt Guidelines)
Memecah narasi ke dalam modul modular yang fleksibel agar LLM merespons dinamis aksi pengguna (`{{user}}`):
- **Core Premise & World Mechanics**: Aturan dunia, batasan sihir/teknologi, dan tema emosional.
- **Act & Quest Modules**: Pembagian alur adegan (Act I: Hook, Act II: Conflict & Branching, Act III: Climax).
- **Event Triggers & Memory Tags**: Penanda variabel seperti status hubungan (`Affection Score`), rahasia yang terungkap, atau item penentu.

### 2. Karakterisasi Mendalam (Persona & Voice)
Format prompt karakter berbasis psikologi naratif tingkat tinggi:
- **Motivation & Core Drive**: Apa yang diinginkan karakter dari `{{user}}`.
- **Pressure & Vulnerability**: Ketakutan terdalam atau trauma masa lalu yang memicu dilema moral.
- **Speech Patterns & Quirks**: Gaya bicara khas, diksi, dan variasi intonasi emosional.
- **Example Dialogues**: Format percakapan terstruktur yang mengunci gaya bicara karakter.

### 3. Dungeon Mind (DM) Mechanics & RPG Systems
Membangun game mechanics agent yang terintegrasi di prompt:
- **Stats Tracking**: HP, Mana, Stamina, Karma, atau Gold.
- **Relationship / Affection Bar**: Indikator status kedekatan dengan `{{user}}` (Cold, Hesitant, Trusting, Devoted).
- **Dice Roll / Skill Check Logic**: Perhitungan probabilitas keberhasilan aksi `{{user}}` (DC 10/15/20) tanpa membuat AI pasif atau auto-win.
- **Inventory & Item Modifiers**: Penyimpanan item dan efek aktifnya pada cerita.

### 4. Visual Novel Mode Compatibility
Mengatur agar cerita tampil optimal pada antarmuka *Visual Novel Mode* ISEKAI ZERO:
- **Foreground Sprites (Karakter)**: Rekomendasi format PNG transparan dengan caption ekspresi emosi (*neutral, blushing, shocked, angry, confident, crying*) agar engine otomatis menampilkan sprite yang selaras dengan dialog.
- **Background Environments**: Caption lingkungan spesifik (*"in the imperial throne room"*, *"dungeon hallway under torchlight"*) untuk sinkronisasi otomatis pergantian latar belakang.
- **Voice Acting Parameters**: Arahan nada suara sintesis untuk sistem TTS karakter di ISEKAI ZERO.

### 5. UI Elements (Markdown & HTML Formatting)
Menyajikan status box, dialog, dan pesan status dengan format Markdown & HTML khusus yang didukung secara elegan di aplikasi mobile ISEKAI ZERO.

---

## Helper Python Generator (`generate_isekaizero_package.py`)

Anda dapat menggunakan skrip pembantu Python untuk mengubah draft naskah atau cerita menjadi 1 paket lengkap siap *copy-paste* ke Creator Centre ISEKAI ZERO:

```bash
py helpers/python/generate_isekaizero_package.py \
  --input chapters/chapter_01.md \
  --output isekaizero_build/ \
  --title "Judul Cerita ISEKAI ZERO"
```

### Berkas yang Dihasilkan:
1. **`storyline_system_prompt.txt`**: System prompt utama berisi aturan dunia, modul cerita, dan logika respons AI.
2. **`character_cards.txt`**: Format karakter lengkap dengan motivation, pressure, dan example dialogues.
3. **`dungeon_mind_rules.txt`**: Modul aturan DM (status bar, inventory, dice check, affection system).
4. **`initial_message.txt`**: Teks pembuka interaktif pertama (*First Greeting*) yang langsung memicu interaksi `{{user}}`.
5. **`visual_asset_manifest.md`**: Daftar prompt AI gambar untuk karakter PNG transparan (berbagai emosi) dan latar belakang.

---

## Contoh Template Output ISEKAI ZERO

### System Prompt Preview:
```text
[WORLD & SCENARIO RULES]
Genre: Dark Fantasy / Otome Isekai
Setting: The Frostveil Academy of Magic
Player Role: {{user}}, an outsider scholar who arrived through a spatial tear.

[CORE CAST: LADY CELESTE]
- Archetype: Cold Duchess & High Mage
- Motivation: Uncover the truth behind the corrupted leylines.
- Secret Insecurity: Fearing she will become a monster like her cursed ancestor.
- Reaction to {{user}}: Initially deeply suspicious, analyzing every word for espionage.

[DUNGEON MIND (DM) RULES]
- Track state at the end of each assistant turn in a compact block:
  [Affection: 15/100 | Suspicions: 40/100 | Status: Guarded]
- Evaluate {{user}} actions with realistic risk and consequence.
```

### Initial Message Preview:
```text
*The biting wind howls through the fractured crystal arches of the Frostveil library. Frost patterns creep across the marble floor as a tall, silver-haired noblewoman steps forward, the tip of her obsidian staff glowing with azure frost.*

"Identify yourself immediately," *Lady Celeste speaks, her violet eyes narrowing coldly.* "Only those bearing imperial seals may step within this sanctum. How did you pierce through the barrier, stranger?"

[Affection: 10/100 | Suspicion: 65/100 | Location: Frostveil Library]
```
