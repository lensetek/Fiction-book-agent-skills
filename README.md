# Fiction Book Agent Skills

> Bilingual single-file README. Jump to language: [English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/lensetek/Fiction-book-agent-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills CLI Compatible](https://img.shields.io/badge/npx%20skills-compatible-brightgreen)](https://github.com/lensetek/Fiction-book-agent-skills)

---

## English

### Overview
**Fiction Book Agent Skills** is a specialized collection of 22 AI agent skills designed for authoring **novels**, **fiction books**, **manga & comic graphic novels**, **children's picture books**, **editorial magazines & zines**, **Wattpad web-novels**, **vertical micro-dramas (TikTok/Reels/ReelShort)**, and **inclusive Braille accessibility books**. Built on an **orchestrator + specialist agents** pattern, it guides authors from initial high-concept ideas, real-time market trend research, and worldbuilding to character psychology, 3-act narrative architecture, scene drafting, dynamic manga/comic framing (slanted cuts, frame-breaking, double-page splash), magazine editorial layouts (A4 multi-column, mastheads, pull-quotes), storybook formatting, Braille conversion, continuity checking, All-In-One Visual Production Bible (`visual_production_bible.md`), Zero-Key AI image generation (Pollinations FLUX), cover design specifications, Wattpad web-novel serialization, vertical micro-drama directing, automated daily updates, and publisher-grade print/digital layout export (including PT. Asadel Liamsindo Teknologi & Asadel Publisher presets).

### Installation

#### Primary CLI Installation
Install via the **`npx skills`** CLI:

```bash
npx skills add https://github.com/lensetek/Fiction-book-agent-skills
```

#### Alternative Prompt-Based Installation
Or copy and paste the repository URL directly into your AI Assistant prompt (Google Antigravity, Claude Code, Codex, Cursor, ChatGPT):

```text
https://github.com/lensetek/Fiction-book-agent-skills
```

---

### Agent Taxonomy (22 Specialist Skills)

| Agent / Skill | Description | Main Tasks | Main Output |
| :--- | :--- | :--- | :--- |
| `fiction-book-orchestrator` | Master workflow manager for fiction projects. | Project intake, routing specialist agents, manuscript coordination. | Combined fiction manuscript & project plan. |
| `story-concept-intake` | Refines core story ideas & premise. | Genre, sub-genre, 1-sentence logline, tropes, and moral theme. | `story_brief.md` |
| `fiction-market-trend-analyst` | Real-time web trend & trope researcher. | Live BookTok/Webtoon/KDP research, title generation, search tags, reference benchmarks. | `market_research_report.md` |
| `worldbuilding-architect` | Designs physical setting & world rules. | Magic/tech systems, geography, factions, sensory ambience. | `worldbuilding_codex.md` |
| `character-designer-psychologist` | Crafts deep character psychology. | Want vs Need, fatal flaw, trauma backstory, character arcs, dialogue voices. | `character_sheets/` |
| `plot-narrative-architect` | Structures story plot architecture. | Save the Cat, 3-Act Structure, Hero's Journey, subplots, foreshadowing map. | `plot_outline.md` |
| `storyboard-scene-planner` | Breaks chapters into scene beats. | Goal, Conflict, Disaster, Reaction, Dilemma, Decision (Swain's Method). | `scene_breakdown.md` |
| `novel-scene-writer` | Drafts rich narrative chapter prose. | "Show, Don't Tell" prose, 5-sensory palette, natural dialogue. | `chapters/chapter_01.md` |
| `comic-webtoon-scriptwriter` | Writes comic & vertical webtoon panel scripts. | Panel breakdown, camera angles, speech balloons, SFX, AI image prompts. | `comic_script.md` |
| `children-story-creator` | Authors children's picture books & fables. | Rhyming prose, age-appropriate vocabulary, page spreads, illustration briefs. | `children_storybook.md` |
| `braille-accessibility-formatter` | Formats books for blind & visually impaired readers. | Twin-Vision Braille Interlined (`⠁⠃⠉`), Audio-Tactile QR Bridges, Braille Embosser export, & EPUB3 accessibility. | `accessibility_plan.md` |
| `plot-hole-continuity-checker` | Audits narrative continuity & plot holes. | Timeline consistency, worldbuilding rule enforcement, character behavior integrity. | `continuity_report.md` |
| `prose-dialogue-polisher` | Polishes prose rhythm & dialogue subtext. | Trims purple prose, aligns character voice, refines dialogue tags. | `chapters_polished/` |
| `beta-reader-critique-simulator` | Simulates target demographic beta feedback. | Evaluates pacing, first-chapter hook, emotional payoff per reader persona. | `beta_reader_feedback.md` |
| `fiction-layout-exporter` | Formats print & digital e-book exports. | Publisher-grade DOCX (Asadel ID/INTL, Novel 13x19 cm, Manga B6, Square, A5, A4) + Mobile Web Reader. | `build/*.docx` & `web_reader/` |
| `fiction-agent-update-manager` | Automated Git update & security manager. | Pre-update credential leak scanning, guarded `git pull` confirmation, & daily cron checks. | Remote repo update status & prompt alerts. |
| `fiction-cover-designer` | Book cover, spine math, & AI prompt designer. | Front/back cover layouts, spine width calculations, typography, safe-area preflight, & AI image prompts. | Cover brief & image prompts. |
| `wattpad-publisher-formatter` | Wattpad web-novel episode serializer & tagger. | Episode splitting (1,500-2,500 words), cliffhanger check, 25 Wattpad search tags, A/N Vote ⭐ prompts, & 2:3 cover specs. | `wattpad_build/*.md` & setup metadata. |
| `fiction-video-reels-director` | Short video reels & micro-drama director. | 3-second viral hooks, 9:16 vertical scene breakdowns, Google Flow/Veo video prompts, Indonesian VO script, & dynamic captions. | `reels_production/*.md` |
| `manga-graphic-novel-artisan` | Japanese Manga & Graphic Novel specialist. | Tankobon B6/A5 sizes, dynamic slanted cuts, frame-breaking, double-page splash, screentone B&W, & negative space for balloons. | `manga_production/*.md` |
| `microdrama-webseries-director` | Vertical 9:16 micro-drama web series director. | 60-90s episode beats (Hook, micro-twist, extreme cliffhanger), safe UI zone, character consistency, & keyframe visual prompts. | `microdrama_production/*.md` |
| `magazine-layout-editor` | Editorial magazine & creative zine editor. | A4/US Letter multi-column grids, masthead cover anatomy, teasers, pull-quotes, drop-caps, & high-fashion editorial photo prompts. | `magazine_production/*.md` |

---

## Bahasa Indonesia

### Ringkasan
**Fiction Book Agent Skills** adalah koleksi 22 *AI Agent Skills* khusus untuk penulisan **novel**, **buku fiksi**, **manga & komik graphic novel**, **buku cerita anak bergambar**, **majalah editorial & zine**, **web-novel Wattpad**, **serial micro-drama vertikal (TikTok/Reels/ReelShort)**, dan **buku aksesibilitas Braille inklusif**. Menggunakan pola **orchestrator + spesialis**, repositori ini memandu penulis dari ide kasar, riset pasar & tren fiksi live di internet, perancangan dunia (*worldbuilding*), psikologi tokoh, arsitektur plot (3-Act / Save the Cat), penulisan adegan *"Show, Don't Tell"*, tata letak bingkai manga dinamis (*slanted cuts, frame-breaking, double-page splash*), tata letak majalah multi-kolom (A4/US Letter, masthead, pull-quotes), skrip panel komik & prompt AI, buku cerita anak berima, konversi Braille & Audio QR, audit kontinuitas garis waktu, desain sampul & perhitungan punggung buku, kit visual terpadu (*Visual Production Bible*), generator gambar gratis tanpa kunci (Pollinations FLUX), serialisasi Wattpad & pemicu Vote ⭐/Komentar, sutradara micro-drama vertikal 9:16, pemantauan pembaruan otomatis harian, hingga ekspor tata letak **buku cetak fisik** (preset PT. Asadel Liamsindo Teknologi & Asadel Publisher) maupun **e-book digital**.

### Panduan Instalasi

#### Cara Utama (CLI Installer)
Instal menggunakan CLI **`npx skills`**:

```bash
npx skills add https://github.com/lensetek/Fiction-book-agent-skills
```

#### Cara Alternatif (Prompt URL)
Or copy and paste the repository URL directly into your AI Assistant prompt (Google Antigravity, Claude Code, Codex, Cursor, ChatGPT):

```text
https://github.com/lensetek/Fiction-book-agent-skills
```

---

### Daftar Agen & Spesialisasi (22 Skills)

| Agent / Skill | Deskripsi | Tugas Utama | Output Utama |
| :--- | :--- | :--- | :--- |
| `fiction-book-orchestrator` | Koordinator utama alur proyek fiksi. | Intake, routing spesialis, koordinasi bab, pemeriksaan akhir. | Alur kerja proyek fiksi & gabungan naskah. |
| `story-concept-intake` | Menggali & mematangkan ide cerita fiksi. | Genre, sub-genre, *logline* 1 kalimat, *trope*, dan tema moral. | `story_brief.md` |
| `fiction-market-trend-analyst` | Riset tren fiksi & judul live di internet. | Riset BookTok/Webtoon/KDP live, formulasi judul, *tags*, benchmark cerita pembanding. | `market_research_report.md` |
| `worldbuilding-architect` | Merancang dunia & aturan fiksi (*worldbuilding*). | Sistem sihir/teknologi, geografi, faksi, lanskap sensori. | `worldbuilding_codex.md` |
| `character-designer-psychologist` | Merancang profil psikologis tokoh. | *Want vs Need*, *fatal flaw*, luka trauma, *character arc*, gaya dialog. | `character_sheets/` |
| `plot-narrative-architect` | Menyusun arsitektur plot cerita. | Kerangka *Save the Cat*, 3-Act, *Hero's Journey*, *subplot*, *foreshadowing*. | `plot_outline.md` |
| `storyboard-scene-planner` | Memecah bab menjadi *Scene Beats*. | *Goal, Conflict, Disaster, Reaction, Dilemma, Decision* (Swain's Method). | `scene_breakdown.md` |
| `novel-scene-writer` | Menulis draf prosa adegan. | Penulisan adegan *"Show, Don't Tell"*, detail sensori (5 indra), dialog alami. | `chapters/chapter_01.md` |
| `comic-webtoon-scriptwriter` | Menulis skrip komik & webtoon vertikal. | Pemecahan panel, sudut kamera, dialog balon, SFX, prompt AI gambar. | `comic_script.md` |
| `children-story-creator` | Menulis buku cerita anak & fabel. | Teks cerita berima per halaman, *brief* ilustrasi, kalibrasi kelompok usia. | `children_storybook.md` |
| `braille-accessibility-formatter` | Format buku cetak & digital ramah tunanetra. | Twin-Vision Braille Interlined (`⠁⠃⠉`), Audio-Tactile QR Bridges, ekspor Braille Embosser, & EPUB3 accessible. | `accessibility_plan.md` |
| `plot-hole-continuity-checker` | Audit kontinuitas & lubang plot. | Memeriksa garis waktu (*timeline*), aturan dunia, & *character behavior integrity*. | `continuity_report.md` |
| `prose-dialogue-polisher` | Menyunting gaya prosa & dialog. | Memangkas *purple prose*, menyelaraskan *character voice*, menghaluskan dialog. | `chapters_polished/` |
| `beta-reader-critique-simulator` | Mensimulasikan umpan balik pembaca target. | Evaluasi *pacing*, daya pikat (*hook*), & *emotional payoff* per persona pembaca. | `beta_reader_feedback.md` |
| `fiction-layout-exporter` | Penata letak **Buku Cetak** & **Digital**. | Ekspor `.docx` siap cetak (Preset Asadel ID/INTL, Novel 13x19 cm, Manga B6, Square, A5, A4) + Mobile Web Reader. | `build/*.docx` & `web_reader/` |
| `fiction-agent-update-manager` | Pengelola pembaruan Git & keamanan otomatis. | Pemindaian kebocoran kredensial, notifikasi persetujuan `git pull`, & jadwal cron harian. | Status update remote repo & prompt persetujuan. |
| `fiction-cover-designer` | Perancang sampul buku, punggung, & prompt AI. | Layout cover depan/belakang, rumus lebar punggung buku, tipografi, preflight cetak, & prompt gambar AI. | Brief cover & prompt gambar AI. |
| `wattpad-publisher-formatter` | Penata & serialisasi web-novel Wattpad. | Pemecahan episode (1.500-2.500 kata), pemicu cliffhanger, 25 tag rekomendasi, A/N pemicu Vote ⭐, & cover 2:3. | `wattpad_build/*.md` & metadata setup. |
| `fiction-video-reels-director` | Sutradara video reels & micro-drama vertikal. | Hook 3 detik viral, breakdown adegan vertikal 9:16, prompt video Google Flow/Veo, naskah VO Indonesia, & subtitle dinamis. | `reels_production/*.md` |
| `manga-graphic-novel-artisan` | Spesialis Manga Jepang & Graphic Novel. | Standar Tankobon B6/A5, framing miring aksi, efek tembus panel, double-page splash, screentone B&W, & negative space balon kata. | `manga_production/*.md` |
| `microdrama-webseries-director` | Sutradara serial micro-drama vertikal 9:16. | Struktur episode 60-90 detik (Hook, micro-twist, cliffhanger ekstrem), safe UI zone, konsistensi aktor, & keyframe visual AI. | `microdrama_production/*.md` |
| `magazine-layout-editor` | Editor tata letak majalah & zine editorial. | Grid 2-3 kolom A4/US Letter, anatomi cover masthead, teasers, pull-quotes, drop-caps, & prompt foto editorial majalah. | `magazine_production/*.md` |

---

## What's New in v1.8.0 (Changelog)

### 🌟 English
- **New Skill: `manga-graphic-novel-artisan`**: Dedicated manga and graphic novel structuring with Tankobon B6 and A5 trim standards, dynamic slanted action cuts, frame-breaking character pop-outs, two-page splash spreads, screentone shading prompts, and speech balloon negative space planning.
- **New Skill: `microdrama-webseries-director`**: Complete scriptwriting and directorial staging for ultra-short 9:16 vertical drama series (TikTok, Reels, Shorts, ReelShort, DramaBox). Engineered with 3-second hook formulas, 60–90 second episodes, micro-twists, safe UI zones (avoiding caption/button overlap), and multi-shot keyframe prompts for AI image/video generators.
- **New Skill: `magazine-layout-editor`**: Editorial magazine and zine design system featuring 2-column and 3-column A4/US Letter grids, masthead cover anatomy with teaser sub-headlines, pull-quotes, drop-caps, photo caption styling, and editorial photography prompts.
- **Enhanced Print Presets in Word DOCX Exporter**: `generate_fiction_docx.py` now includes native support for `manga_b6` (128x182 mm), `storybook_square` (200x200 mm), and `magazine_a4` (210x297 mm with 3-column editorial layout) presets.

### 🌟 Bahasa Indonesia
- **Skill Baru: `manga-graphic-novel-artisan`**: Penataan format Manga & Novel Grafis dengan standar ukuran cetak Tankobon B6 dan A5, pemotongan panel miring aksi (*slanted dynamic cuts*), karakter tembus batas panel (*frame-breaking pop-outs*), splash dua halaman (*spreads*), prompt screentone monokrom, dan alokasi ruang kosong (*negative space*) balon dialog.
- **Skill Baru: `microdrama-webseries-director`**: Penulisan skrip & penyutradaraan micro-drama vertikal 9:16 untuk platform modern (TikTok, IG Reels, YouTube Shorts, ReelShort). Pacing kilat 60–90 detik per episode, formula hook visual 3 detik, safe zone UI antarmuka, konsistensi aktor, dan prompt keyframe multi-shot untuk AI visual.
- **Skill Baru: `magazine-layout-editor`**: Tata letak majalah dan zine profesional berbasis grid 2 & 3 kolom A4/US Letter, struktur anatomi sampul dengan masthead & teaser judul, pull-quotes, huruf kapital awal (*drop-caps*), serta prompt fotografi editorial majalah.
- **Preset Format Baru pada Ekspor DOCX**: Pembaruan generator DOCX (`generate_fiction_docx.py`) dengan preset cetak `manga_b6`, buku cerita anak `storybook_square`, dan tata letak majalah `magazine_a4`.

---

## What's New in v1.7.0 (Changelog)

### 🌟 English
- **New Skill: `fiction-video-reels-director`**: Complete production scriptwriting for 9:16 vertical videos (BookTok, Instagram Reels, YouTube Shorts, & episodic micro-dramas). Includes 3-second viral hooks, Google Flow / Veo camera prompts, and dramatic Indonesian voiceover scripts.
- **All-In-One Visual Production Bible (`visual_production_bible.md`)**: A consolidated master prompt codex providing copy-paste-ready prompts for covers, 3-angle character turnaround consistency sheets, key environments, and climax moments.
- **Zero-Key AI Image Generator (`pollinations_image_generator.py`)**: 100% free, no-API-key image generation powered by Pollinations.ai (FLUX) with automatic high-fidelity prompt enhancement and multi-aspect ratio support (`1:1`, `2:3`, `3:4`, `9:16`, `16:9`).
- **Publisher HTML Cover Generator (`book_cover_template.html` & `generate_book_cover.py`)**: 300 DPI print-ready cover rendering with PT. Asadel Liamsindo Teknologi & Asadel Publisher branding presets.
- **Wattpad Publishing Engine (`wattpad-publisher-formatter`)**: Automated episode splitting (1,500-2,500 words), 25 trending hashtag tags, cliffhanger checks, and Vote ⭐ / Comment Author Notes.
- **Google Flow MCP Support**: Added `google-flow-mcp` integration in `mcp_config.json` for secure browser-based video character consistency generation.

### 🌟 Bahasa Indonesia
- **Skill Baru: `fiction-video-reels-director`**: Penulisan naskah video vertikal 9:16 untuk BookTok, Instagram Reels, dan adaptasi micro-drama berseri (format ReelShort/DramaBox).
- **Kit Visual Terpadu (`visual_production_bible.md`)**: Berkas panduan prompt visual all-in-one untuk sampul novel, lembar konsistensi karakter (3 sudut pandang), latar dunia fiksi, dan adegan klimaks.
- **Generator Gambar Gratis Tanpa Kunci (`pollinations_image_generator.py`)**: Panggilan HTTP langsung tanpa API key menggunakan model FLUX dari Pollinations.ai dengan fitur otomatis Prompt Enhancer.
- **Render Sampul Cetak HTML 300 DPI**: Template interaktif siap cetak dengan preset penerbit *PT. Asadel Liamsindo Teknologi* dan *Asadel Publisher*.
- **Mesin Penerbitan Wattpad (`wattpad-publisher-formatter`)**: Pemecahan bab otomatis (1.500–2.500 kata), pemicu Vote ⭐/Komentar, dan 25 tag rekomendasi algoritma.

---

## License
[MIT License](LICENSE)
