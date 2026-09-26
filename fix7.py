import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

new_dark_mode_css = """<style id="dark-mode-styles">
  html.dark body, html.dark main, html.dark .bg-surface { background-color: #1a1016 !important; color: #ffffff !important; }
  html.dark .bg-surface-container-lowest { background-color: #120a10 !important; }
  html.dark .bg-surface-container-low { background-color: #22151d !important; }
  html.dark .bg-surface-container { background-color: #2c1a26 !important; }
  html.dark .bg-surface-container-high { background-color: #382030 !important; }
  html.dark .bg-surface-container-highest { background-color: #45283a !important; }
  
  html.dark .text-on-surface { color: #ffffff !important; }
  html.dark .text-on-surface-variant { color: #d4a9c5 !important; }
  
  html.dark .border-outline-variant { border-color: #553548 !important; }
  html.dark .text-outline { color: #885577 !important; }
  
  html.dark header { background-color: rgba(26, 16, 22, 0.8) !important; }
  
  /* Fix text readability inside some cards if needed */
  html.dark .bg-primary-container { background-color: #59003b !important; color: #ffd6ee !important; }
  html.dark .text-on-primary-container { color: #ffd6ee !important; }
  
  html.dark .group-hover\:bg-surface-container-high:hover { background-color: #382030 !important; }
  html.dark .hover\:bg-surface-container-high:hover { background-color: #382030 !important; }
</style>"""

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace old dark mode CSS with new one
    old_css_pattern = re.compile(r'<style id="dark-mode-styles">.*?</style>', re.DOTALL)
    content = re.sub(old_css_pattern, new_dark_mode_css, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated dark mode colors in {filepath}")
