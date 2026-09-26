import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

fixed_colors_css = """
  /* Fix Fixed Color Badges (bg-primary-fixed, etc.) in Dark Mode */
  html.dark .bg-primary-fixed { background-color: rgba(224, 64, 160, 0.15) !important; }
  html.dark .text-on-primary-fixed { color: #ffb3e6 !important; }
  
  html.dark .bg-secondary-fixed { background-color: rgba(124, 82, 170, 0.15) !important; }
  html.dark .text-on-secondary-fixed { color: #d3a8ff !important; }
  
  html.dark .bg-tertiary-fixed { background-color: rgba(82, 160, 190, 0.15) !important; }
  html.dark .text-on-tertiary-fixed { color: #80d0f0 !important; }
</style>
"""

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "/* Fix Fixed Color Badges" not in content:
        content = content.replace("</style>", fixed_colors_css)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Applied fixed color badge fixes to {filepath}")
