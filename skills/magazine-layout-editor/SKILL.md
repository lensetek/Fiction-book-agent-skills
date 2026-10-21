---
name: magazine-layout-editor
description: Designs and formats editorial magazines, fiction zines, and periodicals. Directs magazine cover anatomy (masthead, cover lines, barcodes), 2-3 column editorial spreads, drop-caps, pull-quotes, and high-fashion/editorial photography prompts for visual AI models.
metadata:
  short-description: Magazine & zine layout design, mastheads, multi-column spreads, & editorial prompts
---

# Magazine & Periodical Layout Editor

Agen spesialis perancang tata letak majalah, zine fiksi independen, berkala budaya pop, dan jurnal kreatif. Menguasai anatomi sampul majalah komersial (*masthead, cover lines, feature teasers*), tata letak isi multi-kolom (*multi-column editorial spreads*), serta generasi prompt foto editorial bergaya *Vogue, Time, National Geographic, atau Anime Animage*.

Skill ini dioptimalkan khusus untuk model AI berkemampuan *direct image generation* untuk langsung memproduksi foto sampul majalah dan ilustrasi editorial berkualitas studio cetak.

---

## Standar Ukuran Fisik Majalah (Magazine Trim Sizes)

| Format Majalah | Ukuran Standar (cm / in) | Standar Industri | Rasio Aspek Gambar |
| :--- | :--- | :--- | :--- |
| **Majalah Standar Nasional / Global** | **A4** ($21.0 \times 29.7\text{ cm}$) | Tempo, National Geographic, majalah cetak umum | `--ar 3:4` atau `--ar 2:3` |
| **Majalah Standar Amerika** | **US Letter** ($21.59 \times 27.94\text{ cm}$ / $8.5 \times 11\text{ in}$) | Vogue, Time, Wired, Forbes | `--ar 3:4` |
| **Indie Zine / Mini-Magazine** | **A5** ($14.8 \times 21.0\text{ cm}$) | Zine fiksi, artbook komunitas, pamflet sastra | `--ar 2:3` |

- **Marjin Jilid (*Binding Gutter*)**: $2.0\text{ cm} - 2.5\text{ cm}$ untuk jilid kawat (*saddle-stitch*) atau jilid lem panas (*perfect bound*).
- **Bleed Area**: $3\text{ mm}$ di setiap sisi luar halaman cetak.

---

## Anatomi Sampul Majalah (Magazine Cover Anatomy)

Sampul majalah yang menjual disusun dari 5 elemen hierarki visual:
1. **The Masthead**: Judul nama majalah di bagian paling atas (font display besar, tegas, dan ikonik).
2. **The Lead Hero Shot**: Foto editorial atau lukisan karakter utama dengan kontak mata langsung (*eye contact*) yang menembus pembaca.
3. **The Main Cover Line**: Judul artikel utama edisi tersebut dengan ukuran font kedua terbesar (misal: *"RAHASIA KLAN TERAKHIR: Pengakuan Eksklusif Sang Pewaris"*).
4. **Supporting Teaser Lines**: 3–5 kutipan topik artikel sampingan di sisi kiri dan kanan cover untuk mengisi keseimbangan visual.
5. **Issue Dateline & Barcode**: Tanggal terbit, nomor edisi (Vol. 12 No. 4), harga eceran, dan barcode ISSN resmi di sudut bawah.

---

## Tata Letak Halaman Isi (Editorial Spread Layout Architecture)

Halaman artikel majalah memiliki aturan desain yang khas:
- **Grid 2 atau 3 Kolom Simetris**: Teks artikel mengalir dalam kolom vertikal dengan lebar yang nyaman dibaca ($45-60$ karakter per baris).
- **The Drop-Cap (Inisial Pembuka)**: Huruf pertama artikel diperbesar setinggi 3 baris paragraf dengan warna aksen majalah.
- **The Pull-Quote (Kutipan Tembus)**: 1–2 kalimat paling kontroversial atau puitis ditarik keluar, dibesarkan hingga 24pt, dan diapit garis batas aksen warna di tengah dua kolom.
- **Sidebar Box / Infografis Mini**: Kotak informasi berlatar abu-abu/krem lembut berisi biodata tokoh, kronologi fakta, atau glosarium istilah fiksi.

---

## Formula Prompt Foto Editorial Majalah Siap Eksekusi (Direct Image Generation)

Gunakan formula prompt ini secara langsung di lingkungan AI yang bisa generate gambar (ChatGPT / Antigravity / Midjourney):

### A. Cover Majalah Gaya High-Fashion Editorial (Vogue/Vanity Fair Style):
```text
high-fashion magazine cover photograph, professional editorial portrait of [Character Name, 22-year-old elegant Indonesian woman with sleek high bun and crimson silk dress], striking direct eye contact, studio beauty dish lighting, soft specular highlights on skin, clean solid dark teal background leaving ample negative space at top for magazine masthead typography, photographed on Hasselblad 100MP, 8k resolution, award-winning editorial fashion photography --ar 3:4
```

### B. Cover Majalah Anime / Pop-Culture Zine (Animage/Newtype Style):
```text
japanese anime magazine cover illustration, dynamic portrait of [Anime protagonist holding glowing mecha sword], vibrant studio key visual art, clean cel-shaded coloring, bold dramatic lighting, colorful dynamic graphic elements in background, ample space for bold Japanese typography headers, masterpiece anime art, 8k resolution --ar 3:4
```

### C. Halaman Pembuka Artikel Editorial (Double-Page Feature Spread):
```text
magazine double-page editorial spread photograph, cinematic wide environmental portrait, [Male detective in trench coat smoking under a vintage street lamp in rainy Jakarta old town], misty moody atmospheric lighting, film noir aesthetic, negative space on right page for two-column article text and pull-quote, 8k resolution, award-winning photojournalism --ar 16:9
```

---

## Output Artifact
- `magazine_production/issue_01_editorial_spread.md`: Naskah majalah lengkap dengan masthead cover, teks artikel 2 kolom, pull-quotes, dan prompt foto editorial.
- Gambar cover dan foto artikel disimpan di `build/magazine_assets/`.
