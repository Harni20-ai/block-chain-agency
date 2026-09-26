import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

new_script = """
<script>
    document.addEventListener('DOMContentLoaded', () => {
      // Light / Dark mode toggle button in header
      const themeToggle = Array.from(document.querySelectorAll('header button')).find(btn => btn.textContent.includes('light_mode') || btn.textContent.includes('dark_mode'));
      
      // Load saved theme from localStorage
      if (localStorage.getItem('theme') === 'dark') {
          document.documentElement.classList.add('dark');
          if (themeToggle) {
              const icon = themeToggle.querySelector('.material-symbols-outlined');
              if (icon) icon.textContent = 'light_mode';
          }
      }

      if (themeToggle) {
        themeToggle.addEventListener('click', () => {
          document.documentElement.classList.toggle('dark');
          const isDark = document.documentElement.classList.contains('dark');
          
          // Save theme to localStorage
          localStorage.setItem('theme', isDark ? 'dark' : 'light');
          
          const icon = themeToggle.querySelector('.material-symbols-outlined');
          if (icon) {
            icon.textContent = isDark ? 'light_mode' : 'dark_mode';
          }
        });
      }

      // LTR / RTL toggle button in header
      const globeToggle = Array.from(document.querySelectorAll('header button')).find(btn => btn.textContent.includes('globe'));
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

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the old script block with the new one
    script_pattern = re.compile(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => {\s*// Light / Dark mode toggle.*?<\/script>', re.DOTALL)
    
    content = re.sub(script_pattern, new_script, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Added theme persistence to {filepath}")
