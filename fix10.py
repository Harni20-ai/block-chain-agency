import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

improved_dark_mode_css = """<style id="dark-mode-styles">
  /* Base Backgrounds */
  html.dark body, html.dark main, html.dark section, html.dark .bg-surface { background-color: #1a1016 !important; color: #ffffff !important; }
  
  /* Flatten Tailwind Gradients in Dark Mode so they don't use light mode hex colors */
  html.dark .bg-gradient-to-b, 
  html.dark .bg-gradient-to-br, 
  html.dark .bg-gradient-to-tr, 
  html.dark .bg-gradient-to-t,
  html.dark .bg-gradient-to-r,
  html.dark .bg-gradient-to-l { 
      background-image: none !important; 
      background-color: transparent !important;
  }
  
  /* Surface Containers */
  html.dark .bg-surface-container-lowest { background-color: #120a10 !important; }
  html.dark .bg-surface-container-low { background-color: #22151d !important; }
  html.dark .bg-surface-container { background-color: #2c1a26 !important; }
  html.dark .bg-surface-container-high { background-color: #382030 !important; }
  html.dark .bg-surface-container-highest { background-color: #45283a !important; }
  
  /* Text Colors */
  html.dark .text-on-surface { color: #ffffff !important; }
  html.dark .text-on-surface-variant { color: #d4a9c5 !important; }
  html.dark .text-primary { color: #ffb3e6 !important; } /* Brighter pink for dark mode contrast */
  html.dark .text-secondary { color: #d3a8ff !important; } /* Brighter purple */
  html.dark .text-tertiary { color: #80d0f0 !important; } /* Brighter blue */
  html.dark .text-outline { color: #aa7799 !important; }
  
  /* Borders */
  html.dark .border-outline-variant { border-color: #553548 !important; }
  html.dark .border-outline { border-color: #aa7799 !important; }
  
  /* Header */
  html.dark header { background-color: rgba(26, 16, 22, 0.85) !important; }
  
  /* Specific Fixes */
  html.dark .bg-primary-container { background-color: #59003b !important; color: #ffd6ee !important; }
  html.dark .text-on-primary-container { color: #ffd6ee !important; }
  
  html.dark .group-hover\:bg-surface-container-high:hover { background-color: #382030 !important; }
  html.dark .hover\:bg-surface-container-high:hover { background-color: #382030 !important; }
  
  /* Ensure spans inside headings inherit colors properly */
  html.dark h1 span.text-primary, html.dark h2 span.text-primary { color: #ffb3e6 !important; }
</style>"""

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace old dark mode CSS with the improved one
    old_css_pattern = re.compile(r'<style id="dark-mode-styles">.*?</style>', re.DOTALL)
    
    if '<style id="dark-mode-styles">' in content:
        content = re.sub(old_css_pattern, improved_dark_mode_css, content)
    else:
        content = content.replace("</head>", improved_dark_mode_css + "</head>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Applied improved dark mode CSS to {filepath}")
