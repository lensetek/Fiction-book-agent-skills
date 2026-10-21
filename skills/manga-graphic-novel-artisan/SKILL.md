---
name: manga-graphic-novel-artisan
description: Designs and scripts Japanese Manga (Tankobon B6/A5), Manhwa, and Graphic Novels. Formulates dynamic panel framing (slanted cuts, frame-breaking, double-page splash), black & white screentone inking prompts, speedlines, and direct image generation for AI visual models.
metadata:
  short-description: Manga B6/A5 panel framing, screentone, & direct AI visual generation
---

# Manga & Graphic Novel Artisan

Agen spesialis pembuatan naskah, tata letak bingkai (*panel framing*), dan generasi visual langsung untuk **Manga Jepang Klasik (Tankobon)**, **Manhwa Webtoon Berwarna**, dan **Graphic Novel**.

Skill ini dioptimalkan khusus untuk model AI berkemampuan *direct image generation* (seperti ChatGPT / DALL-E 3, Google Antigravity / Gemini Multimodal Canvas, dan Midjourney), memastikan gaya tinta hitam-putih (*B&W screentone*), sudut kamera dramatis, serta konsistensi karakter tetap terjaga di setiap panel.

---

## Standar Ukuran Fisik Manga & Graphic Novel

| Format Manga | Ukuran Standar (cm) | Target Halaman & Format | Rasio Aspek Gambar |
| :--- | :--- | :--- | :--- |
| **Tankobon Standar (Shonen / Shojo)** | **B6** ($12.8 \times 18.2\text{ cm}$) | 180–200 halaman per volume | `--ar 2:3` atau `--ar 1:1.41` |
| **Manga Deluxe / Kanzenban / Seinen** | **A5** ($14.8 \times 21.0\text{ cm}$) | Kertas tebal bertekstur, format premium | `--ar 2:3` |
| **Western Graphic Novel / US Comic** | **US Standard** ($17.0 \times 26.0\text{ cm}$) | Cetak berwarna / hitam-putih | `--ar 2:3` |
| **Webtoon Vertikal** | Lebar **$800\text{ px}$** | Format gulir vertikal tak terbatas | `--ar 9:16` per slice |

- **Marjin Jilid Dalam (*Gutter Margin*)**: $2.2\text{ cm} - 2.5\text{ cm}$ (agar aksi dekat punggung buku tidak terpotong saat dijilid).
- **Area Potong (*Bleed Margin*)**: $3\text{ mm}$ di sekeliling halaman.

---

## Arsitektur Framing & Grid Panel Dinamis

Manga profesional tidak menggunakan panel kotak yang kaku. Agen ini menyusun panel menggunakan kaidah visual dinamis:

### 1. Dynamic Slanted Cut (Panel Miring untuk Aksi)
- Membagi halaman dengan garis diagonal tegas untuk adegan adu kecepatan, serangan pedang, atau kejar-kejaran.
- Arah kemiringan garis mengarahkan mata pembaca dari panel kanan atas ke kiri bawah (alur baca Manga Jepang).

### 2. Frame-Breaking (*Tsuru-koshi*)
- Elemen karakter (ujung pedang, kepalan tangan, rambut yang berkibar, atau efek ledakan) sengaja digambar **menembus keluar dari garis batas bingkai panel** untuk menciptakan ilusi kedalaman 3 dimensi.

### 3. Double-Page Splash (Bentangan Spektakuler)
- 1 ilustrasi masif membentang di dua halaman berdampingan (halaman ganjil dan genap) tanpa garis bingkai, khusus untuk adegan pengungkapan monster raksasa, kota impian, atau jurus puncak.

### 4. Negative Space for Speech Balloons
- Setiap prompt panel mewajibkan minimal **20% area latar belakang polos / bersih** di sudut panel untuk penempatan balon kata (*speech bubble*) vertikal atau horizontal tanpa menutupi ekspresi wajah tokoh.

---

## Formula Prompt Manga Siap Eksekusi (Direct Image Generation)

Gunakan formula prompt ini secara langsung di lingkungan AI yang bisa generate gambar (ChatGPT / Antigravity / Midjourney):

### A. Panel Manga Aksi Dinamis (Shonen B&W):
```text
japanese manga page panel, dynamic action scene, black and white manga illustration, authentic screentone textures, clean deep black inking, [Character Name, 17-year-old boy with spiky black hair and glowing katana], dynamic low-angle perspective, dynamic speedlines radiating from center, intense facial expression, sharp ink crosshatching, negative space in top left corner for dialogue bubble, studio manga art style, 8k resolution --ar 2:3
```

### B. Momen Emosional Shojo / Romance:
```text
manga panel close-up, black and white screentone aesthetic, soft emotional lighting, delicate ink lines, [Female protagonist with wide expressive eyes, blushing screentone pattern on cheeks, wind blowing strands of hair], floating sparkle particles and flower petal screentone background, clean manga book art, 8k resolution --ar 1:1
```

### C. Double-Page Splash Spread:
```text
epic manga double-page splash spread, wide cinematic composition, monochrome screentone with dramatic high contrast ink, [giant mythical dragon coiled around a ruined floating castle above a sea of clouds], breathtaking scale, extreme detail, masterpiece manga illustration, ready for print --ar 16:9
```

---

## Output Artifact
- `manga_production/manga_script_chapter_01.md`: Naskah panel terperinci lengkap dengan jenis shot, sudut potong framing, dialog, SFX, dan prompt gambar per panel.
- File gambar yang digenerate disimpan ke folder `build/manga_panels/`.
