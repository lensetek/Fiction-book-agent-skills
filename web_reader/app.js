// Fiction Book Web Reader Engine

document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const menuBtn = document.getElementById('menu-btn');
  const closeDrawerBtn = document.getElementById('close-drawer');
  const drawerOverlay = document.getElementById('drawer-overlay');
  const tocDrawer = document.getElementById('toc-drawer');
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

  // Character Database Codex Mock
  const characterCodex = {
    'Eldrin': {
      name: 'Archmage Eldrin Vane',
      role: 'Protagonist / Kepala Akademi Arcanum',
      desc: 'Eldrin adalah archmage yang berpengalaman selama dua dekade memimpin Akademi Arcanum. Memiliki kecerdasan analitis yang tajam, namun menyimpan trauma mendalam atas kehancuran kota kelahirannya akibat sihir terlarang.'
    }
  };

  // State
  let currentFontSize = 18;

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

  // Character Pop-up Codex Trigger
  charMentionEls.forEach(el => {
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

  closeModalBtn.addEventListener('click', () => {
    charModal.classList.add('hidden');
  });
});
