# Fiction Book Agent Skills

> Bilingual single-file README. Jump to language: [English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/lensetek/Fiction-book-agent-skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills CLI Compatible](https://img.shields.io/badge/npx%20skills-compatible-brightgreen)](https://github.com/lensetek/Fiction-book-agent-skills)

---

## English

### Overview
**Fiction Book Agent Skills** is a specialized collection of 16 AI agent skills designed for authoring **novels**, **fiction books**, **comic/webtoon scripts**, **children's storybooks**, and **inclusive Braille accessibility books**. Built on an **orchestrator + specialist agents** pattern, it guides authors from initial high-concept ideas, real-time market trend research, and worldbuilding to character psychology, 3-act narrative architecture, scene drafting, comic scripting, storybook formatting, Braille conversion, continuity checking, automated daily updates, and publisher-grade print/digital layout export.

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

### Agent Taxonomy (16 Specialist Skills)

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
| `fiction-layout-exporter` | Formats print & digital e-book exports. | Publisher-grade DOCX (Novel 13x19 cm, A5, A4) with gutter margins + Mobile Web Reader. | `build/*.docx` & `web_reader/` |
| `fiction-agent-update-manager` | Automated Git update & security manager. | Pre-update credential leak scanning, guarded `git pull` confirmation, & daily cron checks. | Remote repo update status & prompt alerts. |

---

## Bahasa Indonesia

### Ringkasan
**Fiction Book Agent Skills** adalah koleksi 16 *AI Agent Skills* khusus untuk penulisan **novel**, **buku fiksi**, **skrip komik/webtoon**, **buku cerita anak**, dan **buku aksesibilitas Braille inklusif**. Menggunakan pola **orchestrator + spesialis**, repositori ini memandu penulis dari ide kasar, riset pasar & tren fiksi live di internet, perancangan dunia (*worldbuilding*), psikologi tokoh, arsitektur plot (3-Act / Save the Cat), penulisan adegan *"Show, Don't Tell"*, skrip panel komik & prompt AI, buku cerita anak berima, konversi Braille & Audio QR, audit kontinuitas garis waktu, pemantauan pembaruan otomatis harian, hingga ekspor tata letak **buku cetak fisik** maupun **e-book digital**.

### Panduan Instalasi

#### Cara Utama (CLI Installer)
Instal menggunakan CLI **`npx skills`**:

```bash
npx skills add https://github.com/lensetek/Fiction-book-agent-skills
```

#### Cara Alternatif (Prompt URL)
Atau salin tautan repositori ini langsung ke dalam prompt AI Assistant Anda (Google Antigravity, Claude Code, Codex, Cursor, ChatGPT):

```text
https://github.com/lensetek/Fiction-book-agent-skills
```

---

### Daftar Agen & Spesialisasi (16 Skills)

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
| `fiction-layout-exporter` | Penata letak **Buku Cetak** & **Digital**. | Ekspor `.docx` siap cetak (Novel 13x19 cm, A5, A4) + Mobile Web Reader. | `build/*.docx` & `web_reader/` |
| `fiction-agent-update-manager` | Pengelola pembaruan Git & keamanan otomatis. | Pemindaian kebocoran kredensial, notifikasi persetujuan `git pull`, & jadwal cron harian. | Status update remote repo & prompt persetujuan. |

---

## License
[MIT License](LICENSE)
