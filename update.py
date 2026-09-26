import os
import urllib.request
import re

dir_path = r"d:\DUMP WEB\web3craft"

urls = {
    "contact.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1YzY0N2U3ZGNlZGUwMjhmMDkyMTM0MDMzNzQ4EgsSBxDnmen76R0YAZIBIwoKcHJvamVjdF9pZBIVQhMxMTY4MDA5MzAwMDA0MDE2Mzkx&filename=&opi=89354086",
    "technologies.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1YzY0N2UyODBjNWMwNzNhZmI1YTNjMDUxY2JjEgsSBxDnmen76R0YAZIBIwoKcHJvamVjdF9pZBIVQhMxMTY4MDA5MzAwMDA0MDE2Mzkx&filename=&opi=89354086",
    "index.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1YzY0N2JlZWU2MTcwN2M0ZTBlN2QwMWExOTQwEgsSBxDnmen76R0YAZIBIwoKcHJvamVjdF9pZBIVQhMxMTY4MDA5MzAwMDA0MDE2Mzkx&filename=&opi=89354086",
    "home2.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1YzY0N2JjM2UwNTkwN2M0ZWMxN2QxMzQzNDlhEgsSBxDnmen76R0YAZIBIwoKcHJvamVjdF9pZBIVQhMxMTY4MDA5MzAwMDA0MDE2Mzkx&filename=&opi=89354086",
    "portfolio.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1YzY0N2Y3ZjJiZGEwNTc2MzE1NWNiMzAwYTkwEgsSBxDnmen76R0YAZIBIwoKcHJvamVjdF9pZBIVQhMxMTY4MDA5MzAwMDA0MDE2Mzkx&filename=&opi=89354086",
    "services.html": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1YzY0N2I5YWRlMjIwN2M0ZjM1YjY2MTBjMzczEgsSBxDnmen76R0YAZIBIwoKcHJvamVjdF9pZBIVQhMxMTY4MDA5MzAwMDA0MDE2Mzkx&filename=&opi=89354086"
}

new_script = """
<script>
    document.addEventListener('DOMContentLoaded', () => {
      // Light / Dark mode toggle button in header
      const themeToggle = Array.from(document.querySelectorAll('header button')).find(btn => btn.textContent.includes('light_mode') || btn.textContent.includes('dark_mode'));
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

home_dropdown = """<div class="relative group">
    <button class="text-sm text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high px-4 py-2 rounded-full transition-all flex items-center gap-1">Home <span class="material-symbols-outlined text-[16px]">expand_more</span></button>
    <div class="absolute left-1/2 -translate-x-1/2 top-full mt-2 w-40 bg-surface border border-outline-variant rounded-xl shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all flex flex-col overflow-hidden">
        <a class="px-4 py-3 text-sm text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface" data-path="home-engineering-authority" href="index.html">Home 1</a>
        <a class="px-4 py-3 text-sm text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface" data-path="home-web3-studio" href="home2.html">Home 2</a>
    </div>
</div>"""

for filename, url in urls.items():
    filepath = os.path.join(dir_path, filename)
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, filepath)
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Strip the original buggy interactivity script from Stitch (if present)
    old_script_pattern = re.compile(r'<!-- Embedded script for interactivity.*?</script>', re.DOTALL)
    content = re.sub(old_script_pattern, '', content)
    
    # 2. Add Dropdown to the Header nav
    home_link_pattern1 = re.compile(r'<a[^>]*data-path="home-engineering-authority"[^>]*>Home</a>')
    home_link_pattern2 = re.compile(r'<a[^>]*data-path="home-web3-studio"[^>]*>Home</a>')
    
    content = re.sub(home_link_pattern1, home_dropdown, content)
    content = re.sub(home_link_pattern2, home_dropdown, content)
    
    # 3. Add the interactivity script before </body>
    content = content.replace("</body>", new_script + "</body>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Processed and updated {filename}")

print("Update complete!")
