// Js file for the base template page.

  (function () {
    const btn = document.getElementById('hamburger');
    const icon = btn.querySelector('i');
    const menu = document.getElementById('navLinks');
    const mqDesktop = window.matchMedia('(min-width: 48em)'); 

    function setMenu(open) {
      menu.classList.toggle('show', open);
      btn.setAttribute('aria-expanded', String(open));
      icon.classList.toggle('fa-bars', !open);
      icon.classList.toggle('fa-xmark', open);
    }

    // click the button (bars ↔ x)
    btn.addEventListener('click', () => {
      setMenu(!menu.classList.contains('show'));
    });

    // close when clicking a menu link
    menu.querySelectorAll('a').forEach(a =>
      a.addEventListener('click', () => setMenu(false))
    );

    // close on outside click
    document.addEventListener('click', (e) => {
      if (!menu.contains(e.target) && !btn.contains(e.target)) setMenu(false);
    });

    // close on Esc
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') setMenu(false);
    });

    // close when resizing to desktop
    mqDesktop.addEventListener('change', () => setMenu(false));
  })();
