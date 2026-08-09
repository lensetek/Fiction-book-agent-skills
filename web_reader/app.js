// Fiction Book Web Reader Engine - 12 Sample Chapters Demo

document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const menuBtn = document.getElementById('menu-btn');
  const closeDrawerBtn = document.getElementById('close-drawer');
  const drawerOverlay = document.getElementById('drawer-overlay');
  const tocDrawer = document.getElementById('toc-drawer');
  const tocList = document.getElementById('toc-list');
  const settingsBtn = document.getElementById('settings-btn');
  const settingsPanel = document.getElementById('settings-panel');
  const themeBtns = document.querySelectorAll('.theme-btn');
  const fontDecBtn = document.getElementById('font-dec');
  const fontIncBtn = document.getElementById('font-inc');
  const fontSizeLabel = document.getElementById('font-size-label');
  const fontFamilySelect = document.getElementById('font-family-select');
  const charMentionEls = document.querySelectorAll('.character-mention');
  const charModal = document.getElementById('character-modal');
  const closeModalBtn = document.getElementById('close-modal');
  const charNameEl = document.getElementById('char-name');
  const charRoleEl = document.getElementById('char-role');
  const charDescEl = document.getElementById('char-desc');
  const manuscriptViewport = document.getElementById('manuscript-viewport');
  const prevChapterBtn = document.getElementById('prev-chapter-btn');
  const nextChapterBtn = document.getElementById('next-chapter-btn');
  const chapterIndicator = document.getElementById('chapter-indicator');
  const progressFill = document.getElementById('progress-fill');

  // 12 Sample Chapters Data
  const manuscriptChapters = [
    {
      number: 1,
      title: "Bab 1: Bisikan di Tengah Malam",
      content: `
        <p class="chapter-opener-p">Darahnya terasa membeku. Keringat dingin membasahi tengkuknya saat derap langkah berat itu berhenti tepat di balik pintu kayu ek tua yang melapuk.</p>
        <p>Lampu gantung tembaga bergetar pelan, memantulkan bayangan samar di atas lantai batu dingin. Selama sepuluh tahun memimpin Akademi Arcanum, <span class="character-mention" data-char="Eldrin">Eldrin</span> tidak pernah merasakan desakan firasat buruk sedahsyat malam ini.</p>
        <div class="scene-break">* * *</div>
        <p>Hujan deras mengguyur atap menara. Di balik kegelapan malam, sebuah rahasia kuno yang terpendam rapat mulai menampakkan dirinya kembali.</p>
      `
    },
    {
      number: 2,
      title: "Bab 2: Pintu yang Terbuka",
      content: `
        <p class="chapter-opener-p">Engsel besi tua berderit keras memecah keheningan menara. Sosok tinggi berjubah hitam melangkah masuk, membiarkan angin malam menerbangkan lembaran peta di meja.</p>
        <p>"Aku sudah memperingatkanmu sepuluh tahun lalu, <span class="character-mention" data-char="Eldrin">Eldrin</span>," bisik suara serak di balik tudung. Segel Kristal Hitam telah retak.</p>
        <div class="scene-break">* * *</div>
        <p>Eldrin mengepalkan tangannya di atas tongkat perak. Ia tahu malam ini adalah awal dari pertarungan terbesar dalam hidupnya.</p>
      `
    },
    {
      number: 3,
      title: "Bab 3: Rahasia Arcanum",
      content: `
        <p class="chapter-opener-p">Perpustakaan bawah tanah Akademi Arcanum menyimpan ribuan manuskrip terlarang yang tak pernah disentuh cahaya matahari.</p>
        <p>Dengan lilin di tangan kanan, Eldrin menelusuri lorong batu berlumut hingga berhenti di depan sebuah pintu besi berukirkan naga kembar.</p>
        <div class="scene-break">* * *</div>
        <p>Hanya kunci darah kuno yang bisa membuka gerbang misteri ini.</p>
      `
    },
    {
      number: 4,
      title: "Bab 4: Bayangan di Balik Cermin",
      content: `
        <p class="chapter-opener-p">Cermin perak tua di sudut ruangan memantulkan ilusi yang tidak sesuai dengan kenyataan.</p>
        <p>Saat Eldrin mendekat, bayangan dirinya di cermin bergerak sendiri dan tersenyum dingin.</p>
        <div class="scene-break">* * *</div>
        <p>"Waktu tidak lagi berpihak padamu," bisik bayangan itu.</p>
      `
    },
    {
      number: 5,
      title: "Bab 5: Utusan dari Selatan",
      content: `
        <p class="chapter-opener-p">Fajar menyingsing di Ujung Selatan. Seekor burung rajawali emas membawa pesan rahasia bertempelkan segel kerajaan.</p>
        <p>Pasukan perbatasan melaporkan pergerakan aneh di lembah kabut.</p>
        <div class="scene-break">* * *</div>
        <p>Perang yang ditakutkan kini tinggal menghitung hari.</p>
      `
    },
    {
      number: 6,
      title: "Bab 6: Jejak yang Hilang",
      content: `
        <p class="chapter-opener-p">Jejak kaki di atas tanah berlumpur terhenti tepat di tepi jurang terjal.</p>
        <p>Eldrin berlutut, menyentuh sisa energi sihir yang tertinggal di udara dingin.</p>
        <div class="scene-break">* * *</div>
        <p>Seseorang telah melompati dimensi tanpa meninggalkan bekas.</p>
      `
    },
    {
      number: 7,
      title: "Bab 7: Pesta di Istana Perak",
      content: `
        <p class="chapter-opener-p">Dentang musik harpa memenuhi aula besar Istana Perak. Para bangsawan berdansa di bawah ribuan lampu kristal.</p>
        <p>Namun di balik senyuman indah dan cangkir anggur emas, intrik politik sedang dirancang di sudut kegelapan.</p>
        <div class="scene-break">* * *</div>
        <p>Pengkhianatan terbesar akan terjadi di tengah kemegahan pesta ini.</p>
      `
    },
    {
      number: 8,
      title: "Bab 8: Nyala Api Ilusi",
      content: `
        <p class="chapter-opener-p">Api biru membumbung tinggi di alun-alun kota, membakar patung pahlawan masa lalu.</p>
        <p>Jeritan warga memecah malam saat mantra ilusi menguasai pikiran mereka.</p>
        <div class="scene-break">* * *</div>
        <p>Eldrin harus memilih: menyelamatkan naskah kuno atau nyawa ratusan warga.</p>
      `
    },
    {
      number: 9,
      title: "Bab 9: Pelarian di Lembah Kelam",
      content: `
        <p class="chapter-opener-p">Kuda hitam itu berlari kencang menembus pepohonan lebat di Lembah Kelam.</p>
        <p>Suara lolongan serigala sihir menggema dari kejauhan, mengejar langkah mereka.</p>
        <div class="scene-break">* * *</div>
        <p>Tidak ada tempat bersembunyi selain reruntuhan kuil tua di puncak bukit.</p>
      `
    },
    {
      number: 10,
      title: "Bab 10: Pengakuan Sang Pengkhianat",
      content: `
        <p class="chapter-opener-p">"Aku tidak punya pilihan lain," bisik sahabat lama Eldrin dengan tangan gemetar terikat rantai sihir.</p>
        <p>Kebenaran yang selama sepuluh tahun tersembunyi akhirnya terungkap di ruang interogasi.</p>
        <div class="scene-break">* * *</div>
        <p>Musuh sejati ternyata adalah sosok yang selama ini paling dipercayai.</p>
      `
    },
    {
      number: 11,
      title: "Bab 11: Badai di Puncak Menara",
      content: `
        <p class="chapter-opener-p">Petir menyambar pilar perak menara utama. Langit berwarna merah keunguan menandakan gerbang dua dunia telah terbuka lebar.</p>
        <p>Eldrin berdiri di tengah lingkaran sihir, merapalkan mantra terkuat yang pernah dicatat sejarah.</p>
        <div class="scene-break">* * *</div>
        <p>Ini adalah saat penentuan yang akan mengubah takdir seluruh kerajaan.</p>
      `
    },
    {
      number: 12,
      title: "Bab 12: Fajar Baru",
      content: `
        <p class="chapter-opener-p">Kabut tebal perlahan terangkat saat sinar matahari pertama menembus sisa-sisa awan kelabu.</p>
        <p>Keheningan kembali menyelimuti Akademi Arcanum. Eldrin memandang ke arah horizon yang luas dengan senyuman lega.</p>
        <div class="scene-break">* * *</div>
        <p>Pertempuran telah usai, namun kisah perjalanan dan harapan baru bagi dunia fiksi ini baru saja dimulai.</p>
      `
    }
  ];

  // Character Database Codex Mock
  const characterCodex = {
    'Eldrin': {
      name: 'Archmage Eldrin Vane',
      role: 'Protagonist / Kepala Akademi Arcanum',
      desc: 'Eldrin adalah archmage yang berpengalaman selama dua dekade memimpin Akademi Arcanum. Memiliki kecerdasan analitis yang tajam, namun menyimpan trauma mendalam atas kehancuran kota kelahirannya akibat sihir terlarang.'
    }
  };

  // State
  let currentChapterIndex = 0;
  let currentFontSize = 18;

  // Render Table of Contents Items dynamically
  function buildTOC() {
    tocList.innerHTML = '';
    manuscriptChapters.forEach((ch, idx) => {
      const a = document.createElement('a');
      a.href = '#';
      a.className = `toc-item ${idx === currentChapterIndex ? 'active' : ''}`;
      a.textContent = ch.title;
      a.addEventListener('click', (e) => {
        e.preventDefault();
        loadChapter(idx);
        closeDrawer();
      });
      tocList.appendChild(a);
    });
  }

  // Load Chapter Function
  function loadChapter(index) {
    if (index < 0 || index >= manuscriptChapters.length) return;
    currentChapterIndex = index;
    const ch = manuscriptChapters[index];

    manuscriptViewport.innerHTML = `
      <section class="chapter-content">
        <h1 class="chapter-title">${ch.title}</h1>
        ${ch.content}
      </section>
    `;

    // Re-bind character mention popups
    const mentions = manuscriptViewport.querySelectorAll('.character-mention');
    mentions.forEach(el => {
      el.addEventListener('click', () => {
        const charKey = el.getAttribute('data-char');
        const charData = characterCodex[charKey] || {
          name: el.textContent,
          role: 'Tokoh Cerita',
          desc: 'Informasi rincian profil tokoh dapat ditemukan di file character_sheet.'
        };
        charNameEl.textContent = charData.name;
        charRoleEl.textContent = charData.role;
        charDescEl.textContent = charData.desc;
        charModal.classList.remove('hidden');
      });
    });

    // Update UI controls
    chapterIndicator.textContent = `Bab ${index + 1} dari ${manuscriptChapters.length}`;
    prevChapterBtn.disabled = index === 0;
    nextChapterBtn.disabled = index === manuscriptChapters.length - 1;
    prevChapterBtn.style.opacity = index === 0 ? '0.5' : '1';
    nextChapterBtn.style.opacity = index === manuscriptChapters.length - 1 ? '0.5' : '1';

    // Update Progress Bar
    const progressPct = ((index + 1) / manuscriptChapters.length) * 100;
    progressFill.style.width = `${progressPct}%`;

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
    buildTOC();
  }

  // Navigation Event Listeners
  prevChapterBtn.addEventListener('click', () => loadChapter(currentChapterIndex - 1));
  nextChapterBtn.addEventListener('click', () => loadChapter(currentChapterIndex + 1));

  // Drawer Toggle
  menuBtn.addEventListener('click', () => {
    tocDrawer.classList.add('open');
    drawerOverlay.classList.add('active');
  });

  const closeDrawer = () => {
    tocDrawer.classList.remove('open');
    drawerOverlay.classList.remove('active');
  };

  closeDrawerBtn.addEventListener('click', closeDrawer);
  drawerOverlay.addEventListener('click', closeDrawer);

  // Settings Panel Toggle
  settingsBtn.addEventListener('click', () => {
    settingsPanel.classList.toggle('hidden');
  });

  // Theme Switcher
  themeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      themeBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const theme = btn.getAttribute('data-theme-val');
      document.documentElement.setAttribute('data-theme', theme);
    });
  });

  // Font Size Adjuster
  fontDecBtn.addEventListener('click', () => {
    if (currentFontSize > 14) {
      currentFontSize -= 2;
      document.body.style.fontSize = `${currentFontSize}px`;
      fontSizeLabel.textContent = `${currentFontSize}px`;
    }
  });

  fontIncBtn.addEventListener('click', () => {
    if (currentFontSize < 26) {
      currentFontSize += 2;
      document.body.style.fontSize = `${currentFontSize}px`;
      fontSizeLabel.textContent = `${currentFontSize}px`;
    }
  });

  // Font Family Selector
  fontFamilySelect.addEventListener('change', (e) => {
    document.body.style.fontFamily = e.target.value;
  });

  closeModalBtn.addEventListener('click', () => {
    charModal.classList.add('hidden');
  });

  // Initial Load
  loadChapter(0);
});
