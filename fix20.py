import os
import glob

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

old_script = """      // LTR / RTL toggle button in header
      const globeToggle = Array.from(document.querySelectorAll('header button')).find(btn => btn.textContent.includes('globe'));
      if (globeToggle) {
        globeToggle.addEventListener('click', () => {
          const currentDir = document.documentElement.getAttribute('dir');
          document.documentElement.setAttribute('dir', currentDir === 'rtl' ? 'ltr' : 'rtl');
        });
      }"""

new_script = """      // LTR / RTL toggle button in header
      if (localStorage.getItem('dir') === 'rtl') {
          document.documentElement.setAttribute('dir', 'rtl');
      }
      const globeToggle = Array.from(document.querySelectorAll('header button')).find(btn => btn.textContent.includes('globe'));
      if (globeToggle) {
        globeToggle.addEventListener('click', () => {
          const currentDir = document.documentElement.getAttribute('dir');
          const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
          document.documentElement.setAttribute('dir', newDir);
          localStorage.setItem('dir', newDir);
        });
      }"""

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_script in content:
        content = content.replace(old_script, new_script)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated RTL toggle in {filepath}")
    else:
        print(f"Old script not found in {filepath}")
