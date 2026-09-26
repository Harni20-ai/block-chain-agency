import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

new_script = """
<script>
    document.addEventListener('DOMContentLoaded', () => {
      // Light / Dark mode toggle button in header
      const themeToggle = document.querySelector('header button:nth-child(2)');
      if (themeToggle) {
        themeToggle.addEventListener('click', () => {
          document.documentElement.classList.toggle('dark');
          const isDark = document.documentElement.classList.contains('dark');
          const icon = themeToggle.querySelector('.material-symbols-outlined');
          if (icon) {
            icon.textContent = isDark ? 'dark_mode' : 'light_mode';
          }
          
          if(isDark) {
            document.documentElement.style.setProperty('filter', 'invert(1) hue-rotate(180deg)');
            document.querySelectorAll('img, .bg-primary, .text-primary').forEach(el => el.style.setProperty('filter', 'invert(1) hue-rotate(180deg)'));
          } else {
            document.documentElement.style.setProperty('filter', 'none');
            document.querySelectorAll('img, .bg-primary, .text-primary').forEach(el => el.style.setProperty('filter', 'none'));
          }
        });
      }

      // LTR / RTL toggle button in header
      const globeToggle = document.querySelector('header button:nth-child(1)');
      if (globeToggle) {
        globeToggle.addEventListener('click', () => {
          const currentDir = document.documentElement.getAttribute('dir');
          document.documentElement.setAttribute('dir', currentDir === 'rtl' ? 'ltr' : 'rtl');
        });
      }

      // Fix links
      const navLinks = document.querySelectorAll('nav a, footer a[data-path], a[data-path]');
      navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
          const path = link.getAttribute('data-path');
          if (path) {
            e.preventDefault();
            const routes = {
              'home-engineering-authority': 'index.html',
              'home-web3-studio': 'home2.html',
              'home-web3-product-studio': 'home2.html',
              'services': 'services.html',
              'portfolio': 'portfolio.html',
              'technologies': 'technologies.html',
              'contact': 'contact.html'
            };
            if (routes[path]) {
                window.location.href = routes[path];
            }
          }
        });
      });
    });
</script>
"""

home_dropdown = """<div class="relative group">
    <button class="transition-all text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high font-bold rounded-full px-4 py-2 flex items-center gap-1">Home <span class="material-symbols-outlined text-[16px]">expand_more</span></button>
    <div class="absolute left-0 top-full mt-2 w-48 bg-surface border border-outline-variant rounded-xl shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all flex flex-col overflow-hidden">
        <a class="px-4 py-3 text-sm text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface" data-path="home-engineering-authority" href="index.html">Home 1: Engineering</a>
        <a class="px-4 py-3 text-sm text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface" data-path="home-web3-studio" href="home2.html">Home 2: Studio</a>
    </div>
</div>"""

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Add Dropdown to the Header nav if not there
    home_link_pattern1 = re.compile(r'<a[^>]*data-path="home-engineering-authority"[^>]*>Home</a>')
    home_link_pattern2 = re.compile(r'<a[^>]*data-path="home-web3-studio"[^>]*>Home</a>')
    
    content = re.sub(home_link_pattern1, home_dropdown, content)
    content = re.sub(home_link_pattern2, home_dropdown, content)
    
    # 2. Add the interactivity script before </body> if it's not present
    if "// Fix links" not in content:
        content = content.replace("</body>", new_script + "</body>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Processed {filepath}")
