// // Js file for the base template page.

  // (function () {
  //   const btn = document.getElementById('hamburger');
  //   const menu = document.getElementById('navLinks');
  //   if (!btn || !menu) return;
  //   const icon = btn.querySelector('i');

  //   const mqDesktop = window.matchMedia('(min-width: 48em)'); 

  //   function setMenu(open) {
  //     menu.classList.toggle('show', open);
  //     btn.setAttribute('aria-expanded', String(open));
  //     if (icon)
  //     {
  //       icon.classList.toggle('fa-bars', !open);
  //       icon.classList.toggle('fa-xmark', open);
  //     }
  //     requestAnimationFrame(updateHeaderHeightVar);

  //   }

  //   // click the button (bars ↔ x)
  //   btn.addEventListener('click', () => {
  //     setMenu(!menu.classList.contains('show'));
  //   });

  //   // close when clicking a menu link
  //   menu.querySelectorAll('a').forEach(a =>
  //     a.addEventListener('click', () => setMenu(false))
  //   );

  //   // close on outside click
  //   document.addEventListener('click', (e) => {
  //     if (!menu.contains(e.target) && !btn.contains(e.target)) setMenu(false);
  //   });

  //   // close on Esc
  //   document.addEventListener('keydown', (e) => {
  //     if (e.key === 'Escape') setMenu(false);
  //   });

  //   // close when resizing to desktop
  //   mqDesktop.addEventListener('change', () => setMenu(false));
  // })();

  // (function () {
  //   const header = document.querySelector('header');
  //   const menu = document.getElementById('navLinks');        
  //   const btn  = document.getElementById('menuToggle') || document.getElementById('hamburger');
  
  //   function setHeaderHeightVar() {
  //     if (!header) return;
  //     const h = header.offsetHeight;
  //     document.documentElement.style.setProperty('--header-h', h + 'px');
  //   }
  
  //   // on load + resize
  //   window.addEventListener('load', setHeaderHeightVar);
  //   window.addEventListener('resize', setHeaderHeightVar);
  
  //   // when opening/closing the mobile menu, header height changes
  //   if (btn && menu) {
  //     btn.addEventListener('click', () => {
  //       menu.classList.toggle('show');
  //       requestAnimationFrame(setHeaderHeightVar);
  //     });
  //   }
  // })();
// base.js — unified, safe hamburger + header height update
// console.log('[base.js] loaded');
// window.addEventListener('DOMContentLoaded', ()=>console.log('[base.js] DOM ready'));

// (function () {
//   // Elements
//   const btn   = document.getElementById('hamburger');
//   const menu  = document.getElementById('navLinks');
//   // TEMP: force menu open on load at small widths
//   if (menu) { setTimeout(() => menu.classList.add('show'), 0); }

//   console.log('[base.js] btn:', !!btn, 'menu:', !!menu);
//   if (!btn || !menu) return; // hard stop if markup isn't present

//   const icon = btn.querySelector('i');
//   const mqDesktop = window.matchMedia('(min-width: 48em)');

//   // State -> DOM
//   function setMenu(open) {
//     menu.classList.toggle('show', open);
//     btn.setAttribute('aria-expanded', String(open));
//     if (icon) {
//       icon.classList.toggle('fa-bars', !open);
//       icon.classList.toggle('fa-xmark', open);
//     }
//     // header height may change when menu opens; recompute CSS var
//     requestAnimationFrame(updateHeaderHeightVar);
//   }

//   // Compute --header-h from actual header height
//   function updateHeaderHeightVar() {
//     const header = document.querySelector('header');
//     if (!header) return;
//     const h = header.offsetHeight;
//     document.documentElement.style.setProperty('--header-h', h + 'px');
//   }

//   // Events
//   btn.addEventListener('click', () => {
//     console.log('[base.js] hamburger clicked');
//     setMenu(!menu.classList.contains('show'));
//   });

//   // Close when clicking a menu link (mobile UX)
//   menu.querySelectorAll('a').forEach(a => {
//     a.addEventListener('click', () => setMenu(false));
//   });

//   // Close on outside click
//   document.addEventListener('click', (e) => {
//     if (!menu.contains(e.target) && !btn.contains(e.target)) setMenu(false);
//   });

//   // Close on Esc
//   document.addEventListener('keydown', (e) => {
//     if (e.key === 'Escape') setMenu(false);
//   });

//   // Close when switching to desktop layout
//   mqDesktop.addEventListener('change', () => setMenu(false));

//   // Initial layout pass
//   window.addEventListener('load', updateHeaderHeightVar);
//   window.addEventListener('resize', updateHeaderHeightVar);
// })();

(function () {
  const btn  = document.getElementById('hamburger');
  const menu = document.getElementById('navLinks');
  if (!btn || !menu) return;

  const icon = btn.querySelector('i');

  function updateHeaderHeightVar() {
    const header = document.querySelector('header');
    if (header) {
      document.documentElement.style.setProperty('--header-h', header.offsetHeight + 'px');
    }
  }

  function setMenu(open) {
    menu.classList.toggle('show', open);
    btn.setAttribute('aria-expanded', String(open));
    if (icon) {
      icon.classList.toggle('fa-bars', !open);
      icon.classList.toggle('fa-xmark', open);
    }
    // recalc after DOM paints new header height
    requestAnimationFrame(updateHeaderHeightVar);
  }

  btn.addEventListener('click', (e)=> {
    e.stopPropagation();
    setMenu(!menu.classList.contains('show'));
  });

  document.addEventListener('click', (e) => {
    if (!menu.contains(e.target) && !btn.contains(e.target)) setMenu(false);
  });

  // initial + resize
  window.addEventListener('load', updateHeaderHeightVar);
  window.addEventListener('resize', updateHeaderHeightVar);
})();
