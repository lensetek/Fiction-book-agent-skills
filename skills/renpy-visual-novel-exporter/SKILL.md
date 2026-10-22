---
name: renpy-visual-novel-exporter
description: Exports fiction manuscripts, dialogues, and branching storyboards into fully playable Ren'Py Visual Novel scripts (.rpy), ATL animations, camera effects, BGM/SFX audio cue sheets, and visual asset prompt packages.
---

# Ren'Py Visual Novel Exporter (`renpy-visual-novel-exporter`)

Agen spesialis konversi naskah fiksi, dialog tokoh, dan papan cerita percabangan (*branching interactive narrative*) menjadi proyek game visual novel siap jalan berbasis **Ren'Py Engine** (`.rpy`).

---

## Kemampuan Utama (*Core Capabilities*)

1. **Konversi Dialog & Narator ke Syntax Ren'Py**:
   - Mendefinisikan karakter dengan kode warna khas (`define a = Character("Arya", color="#4a90e2")`).
   - Memetakan dialog ucapan tokoh (`a "Dialog di sini..."`) dan narasi lingkungan tanpa pembicara.
   
2. **Interactive Choices & Narrative Branching**:
   - Struktur blok `menu:` dengan opsi pilihan pemain.
   - Variabel state hubungan atau plot flag (misal: `$ rina_affection += 1`, `$ key_found = True`).
   - Navigasi alur menggunakan `jump <label_name>`.

3. **Audio Management (BGM, SFX & Ambient Sound)**:
   - Pemutaran musik latar berulang dengan transisi halus: `play music "audio/bgm/theme.ogg" fadein 2.0 loop`.
   - Efek suara sekuensial: `play sound "audio/sfx/door_slam.ogg"`.
   - Audio atmospheric ambience: `play audio "audio/sfx/rain_ambient.ogg" volume 0.7`.
   - Menghentikan audio secara elegan: `stop music fadeout 1.5`.

4. **Kamera & Animasi ATL (Animation and Transformation Language)**:
   - Transisi layar dramatis: `scene bg library with fade`, `with dissolve`, `with flash_white`.
   - Efek goncangan kamera (*camera shake*): `with hpunch` (horizontal/benturan) dan `with vpunch` (vertikal/gempa).
   - Animasi gerakan sprite karakter (ATL):
     - Masuk panggung: `show rina normal at masuk_kiri_cepat`
     - Loncat kaget: `show rina kaget at lompat_kaget`
     - Gerakan bernapas atau idle: `show rina at sprite_idle`

5. **Spesifikasi & Cue Sheet Aset Otomatis**:
   - Menghasilkan daftar kebutuhan aset `asset_manifest.md` yang siap pakai untuk ilustrator maupun generator gambar AI (Pollinations FLUX, Midjourney, DALL-E) serta panduan prompt audio/BGM untuk Suno/Udio.

---

## Struktur Output Proyek Ren'Py

Ketika dieksekusi, agen menghasilkan berkas yang siap ditaruh langsung ke dalam direktori `game/` pada proyek Ren'Py Anda:

```text
renpy_project/
├── game/
│   ├── script.rpy            # Naskah cerita, label alur utama, dan pilihan menu percabangan
│   ├── definitions.rpy       # Deklarasi Karakter (nama, warna), variabel skor, audio channel
│   ├── transforms.rpy        # Animasi ATL kustom (lompat, goyang, zoom, slide-in)
│   ├── asset_manifest.md     # Panduan daftar background, sprite ekspresi, dan BGM/SFX
│   ├── audio/
│   │   ├── bgm/              # Musik latar (.ogg / .mp3)
│   │   └── sfx/              # Efek suara
│   └── images/
│       ├── bg/               # Background adegan (1920x1080 Full HD)
│       └── characters/       # Sprite PNG transparan (normal, senyum, kaget, marah)
```

---

## Helper Python Generator (`export_to_renpy.py`)

Anda dapat menjalankan helper skrip otomatis untuk mengubah berkas naskah Markdown menjadi script Ren'Py:

```bash
python helpers/python/export_to_renpy.py \
  --input chapters/chapter_01.md \
  --output renpy_build/game/script.rpy \
  --title "Judul Cerita Anda"
```

### Parameter Helper
- `--input` : File markdown naskah cerita atau storyboard.
- `--output`: File target `.rpy` (default: `renpy_build/game/script.rpy`).
- `--title` : Judul visual novel untuk label start.
- `--manifest`: Menghasilkan berkas `asset_manifest.md` secara otomatis.

---

## Contoh Template Script Output

### `definitions.rpy`
```renpy
# Definisi Karakter
define a = Character("Arya", color="#3b82f6")
define r = Character("Rina", color="#ec4899")
define narrator = Character(None, italic=True)

# Variabel State Permainan
default points_investigasi = 0
default rina_trust = False
```

### `transforms.rpy`
```renpy
# Animasi ATL
transform lompat_kaget:
    easein 0.12 yoffset -35
    easeout 0.12 yoffset 0

transform masuk_dari_kiri:
    xalign -0.3 yalign 1.0
    easein 0.4 xalign 0.15

transform masuk_dari_kanan:
    xalign 1.3 yalign 1.0
    easein 0.4 xalign 0.85
```

### `script.rpy`
```renpy
label start:
    play music "audio/bgm/misteri_perpustakaan.ogg" fadein 2.0 loop
    scene bg perpustakaan_kuno with fade

    "Malam itu, hembusan angin kencang menerpa jendela perpustakaan tua."
    play sound "audio/sfx/jendela_terbanting.ogg"
    with hpunch

    show rina cemas at masuk_dari_kanan
    r "Arya! Syukurlah kamu masih di sini. Ada dokumen yang hilang dari brankas!"

    menu:
        "Tenang Rina, kita cari bersama-sama.":
            $ rina_trust = True
            show rina lega at lompat_kaget
            r "Terima kasih, Arya... Aku tahu aku bisa mengandalkanmu."
            jump rute_investigasi_bersama

        "Sebaiknya kita laporkan ini ke penjaga malam dulu.":
            r "Tapi kalau penjaga tahu, reputasi klub kita bisa hancur!"
            jump rute_lapor_penjaga
```
