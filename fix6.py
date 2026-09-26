import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

dark_mode_css = """
<style id="dark-mode-styles">
  html.dark body, html.dark main, html.dark .bg-surface { background-color: #121212 !important; color: #ffffff !important; }
  html.dark .bg-surface-container-lowest { background-color: #000000 !important; }
  html.dark .bg-surface-container-low { background-color: #1e1e1e !important; }
  html.dark .bg-surface-container { background-color: #282828 !important; }
  html.dark .bg-surface-container-high { background-color: #333333 !important; }
  html.dark .bg-surface-container-highest { background-color: #3e3e3e !important; }
  
  html.dark .text-on-surface { color: #ffffff !important; }
  html.dark .text-on-surface-variant { color: #aaaaaa !important; }
  
  html.dark .border-outline-variant { border-color: #444444 !important; }
  
  html.dark header { background-color: rgba(18, 18, 18, 0.8) !important; }
  
  /* Fix text readability inside some cards if needed */
  html.dark .bg-primary-container { background-color: #59003b !important; color: #ffd6ee !important; }
  html.dark .text-on-primary-container { color: #ffd6ee !important; }
  
  html.dark .group-hover\:bg-surface-container-high:hover { background-color: #333333 !important; }
  html.dark .hover\:bg-surface-container-high:hover { background-color: #333333 !important; }
</style>
"""

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove the invert filter logic from the script
    bad_script_logic = """
          if(isDark) {
            document.documentElement.style.setProperty('filter', 'invert(1) hue-rotate(180deg)');
            document.querySelectorAll('img, .bg-primary, .text-primary').forEach(el => el.style.setProperty('filter', 'invert(1) hue-rotate(180deg)'));
          } else {
            document.documentElement.style.setProperty('filter', 'none');
            document.querySelectorAll('img, .bg-primary, .text-primary').forEach(el => el.style.setProperty('filter', 'none'));
          }
"""
    content = content.replace(bad_script_logic, "")
    
    # Inject the dark mode CSS into <head> if not already there
    if '<style id="dark-mode-styles">' not in content:
        content = content.replace("</head>", dark_mode_css + "</head>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {filepath}")
