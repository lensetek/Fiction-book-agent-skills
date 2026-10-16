---
name: fiction-video-reels-director
description: Directs, scripts, and structures short vertical 9:16 videos, BookTok teasers, Instagram Reels, and episodic micro-dramas for fiction books. Outputs 3-second hooks, scene-by-scene visual prompts for Google Flow/Veo, dramatic Indonesian voiceover scripts, and TikTok-style dynamic captions.
metadata:
  short-description: Direct vertical 9:16 video reels & micro-drama scripts for fiction stories
---

# Fiction Video Reels Director

Agen spesialis sutradara naskah video pendek vertikal (rasio $9:16$), *BookTok teaser*, Instagram Reels, YouTube Shorts, dan adaptasi *micro-drama* berseri (format ReelShort / DramaBox) dari bab naskah fiksi.

Skill ini menjembatani cerita fiksi menjadi materi video sinematik dengan struktur durasi yang terbukti viral ($15\text{ detik}$, $30\text{ detik}$, atau $60\text{ detik}$), mengintegrasikan instruksi prompt video berbasis AI (Google Flow / Veo / Gemini Omni Flash via `flow-mcp`, Luma Dream Machine, Kling AI, atau Runway Gen-3), serta menyusun naskah *voiceover* (VO) Bahasa Indonesia dengan daya pikat emosional tinggi.

---

## Agent Contract

### Input:
- **Manuscript Segment / Chapter**: Bab naskah novel atau ringkasan adegan klimaks.
- **Story Arc & Hook**: Momen paling mengejutkan / misterius / romantis dari bab tersebut.
- **Characters Involved**: Tokoh utama yang terlibat dalam adegan (profil fisik & emosi).
- **Video Format**:
  - `BookTok Teaser` (15-30 detik): Cuplikan visual & kutipan dialog untuk memancing pembaca ke Wattpad / Buku Cetak.
  - `Episodic Micro-Drama` (60 detik): Adegan utuh adaptasi web-series vertikal dengan dialog interaktif dan *cliffhanger*.
- **Target Platform**: TikTok, Instagram Reels, YouTube Shorts, atau SnackVideo.

### Output:
- `status`: `ready`, `needs_input`, atau `completed`.
- `video_reels_script.md`:
  - **Hook 3 Detik Pertama**: Teks visual di layar (*on-screen hook*), efek suara (*SFX*), dan visual *shock value*.
  - **Scene-by-Scene Breakdown (Tabel Produksi)**:
    - *Timestamp* ($00:00 - 00:03$, $00:03 - 00:10$, dst.).
    - *Camera & Framing*: Close-up wajah, low-angle dramatis, panning vertikal $9:16$.
    - *AI Video Prompt*: Prompt spesifik untuk generator video AI (Google Flow / Veo / Luma).
    - *Voiceover / Dialog*: Naskah sulih suara bahasa Indonesia ekspresif.
    - *On-Screen Dynamic Text*: Teks takarir animasi ala TikTok.
  - **Audio & Sound Atmosphere**: Rekomendasi musik latar (BGM - cinematic piano, dark synth, romance violin).
  - **Call to Action (CTA)**: Arahan penonton untuk membaca kelanjutan cerita di Wattpad atau memesan buku cetak.

---

## Template Struktur Naskah Video 9:16

### 1. Struktur 15–30 Detik (BookTok / Reels Viral Teaser)
1. **00:00 - 00:03 (The Hook)**: Pertanyaan provokatif atau adegan krisis utama.
   - *On-Screen Text*: "Jangan pernah baca novel ini sendirian di malam hari..." atau "Saat rahasia terbesar keluarga miliarder itu terbongkar..."
2. **00:03 - 00:18 (The Build-Up & Climax)**: Puncak ketegangan emosional dua karakter.
3. **00:18 - 00:30 (The Cliffhanger & CTA)**: Kalimat terpotong di momen genting.
   - *CTA*: "Kelanjutan kisah [Judul Novel] sudah tayang di Wattpad / tersedia di Asadel Publisher! Klik link di bio!"

### 2. Struktur 60 Detik (Vertical Micro-Drama Scene)
Memetakan 1 babak utuh drama vertikal ala ReelShort dengan 4 ketukan:
- **Detik 01-05**: Konfrontasi langsung di layar ponsel.
- **Detik 06-25**: Argumen bertegangan tinggi / fakta tersembunyi terungkap.
- **Detik 26-45**: Titik balik dramatis (plot twist mikro).
- **Detik 46-60**: Reaksi keterkejutan dan *cliffhanger* episode.

---

## Format Prompt AI Video (Google Flow & Veo)

Format prompt video AI yang dihasilkan mengikuti kaidah sinematik gerak kamera:
```text
vertical 9:16 cinematic video, slow dramatic camera push-in on [Character Name, Indonesian young woman with tearful eyes], emotional expression turning into cold resolve, rain drops sliding on window glass, volumetric cinematic lighting, photorealistic 8k, Veo ultra-smooth motion --ar 9:16
```

---

## Integrasi Ekosistem dengan `flow-mcp`

Untuk pengguna yang menghubungkan server **`flow-mcp`** (otomasi Google Flow di Chrome lokal):
1. Skill ini merumuskan konsistensi karakter (*omni-character prompt*).
2. Agent dapat langsung menyuplai prompt ke Google Flow tanpa memerlukan biaya API tambahan, memanfaatkan kuota harian akun Google pengguna.

---

## Output Artifact
Dokumen naskah video lengkap disimpan di:
- `reels_production/reels_script_01.md`
- Gambar latar belakang video vertikal (9:16) dihasilkan via `python helpers/python/pollinations_image_generator.py --prompt "..." --aspect-ratio 9:16`.
