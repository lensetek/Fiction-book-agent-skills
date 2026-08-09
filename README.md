# Fiction Book Agent Skills

> Bilingual README. English first, Bahasa Indonesia below.

Language: [English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

---

## English

**Fiction Book Agent Skills** is a comprehensive collection of AI agent skills for authoring **novels**, **fiction books**, **comic/webtoon scripts**, and **children's storybooks**. It uses an **orchestrator + specialist agents** pattern to guide authors from initial high-concept ideas, real-time market trend research, and worldbuilding to character psychology, 3-act narrative architecture, scene drafting, comic scripting, storybook formatting, continuity checking, and publisher-grade print/digital layout export.

### CLI Installation

Install via **`npx skills`** CLI:

```bash
npx skills add https://github.com/lensetek/Fiction-book-agent-skills
```

Or reference the GitHub repository URL in your AI coding environment (Google Antigravity, Claude Code, Codex, Cursor):

```text
https://github.com/lensetek/Fiction-book-agent-skills
```

---

## Bahasa Indonesia

**Fiction Book Agent Skills** adalah koleksi *AI Agent Skills* khusus untuk penulisan **novel**, **buku fiksi**, **skrip komik/webtoon**, dan **buku cerita anak**. Menggunakan pola **orchestrator + spesialis**, repositori ini memandu penulis dari ide kasar, riset pasar & tren fiksi live di internet, perancangan dunia (*worldbuilding*), psikologi tokoh, arsitektur plot (3-Act / Save the Cat), penulisan adegan *"Show, Don't Tell"*, skrip panel komik & prompt AI, buku cerita anak berima, audit kontinuitas garis waktu, hingga ekspor tata letak **buku cetak fisik** maupun **e-book digital**.

---

## Agent List & Taxonomy (14 Skills)

| Agent / Skill | Description | Main Tasks | Main Output |
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
| `plot-hole-continuity-checker` | Audit kontinuitas & lubang plot. | Memeriksa garis waktu (*timeline*), aturan dunia, & *character behavior integrity*. | `continuity_report.md` |
| `prose-dialogue-polisher` | Menyunting gaya prosa & dialog. | Memangkas *purple prose*, menyelaraskan *character voice*, menghaluskan dialog. | `chapters_polished/` |
| `beta-reader-critique-simulator` | Mensimulasikan umpan balik pembaca target. | Evaluasi *pacing*, daya pikat (*hook*), & *emotional payoff* per persona pembaca. | `beta_reader_feedback.md` |
| `fiction-layout-exporter` | Penata letak **Buku Cetak** & **Digital**. | Ekspor `.docx` siap cetak (Novel 13x19 cm, A5, A4) + Mobile Web Reader. | `build/*.docx` & `web_reader/` |

---

## Lisensi

[MIT License](LICENSE)
