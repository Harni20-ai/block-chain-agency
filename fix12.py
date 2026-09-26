import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

opacity_fixes_css = """
  /* Fix opacity modifier backgrounds that were defaulting to light grey/white */
  html.dark .bg-surface-container-lowest\\/80 { background-color: rgba(44, 20, 36, 0.85) !important; box-shadow: 0 12px 40px rgba(0,0,0,0.5) !important; }
  html.dark .bg-surface-container\\/10 { background-color: rgba(44, 26, 38, 0.1) !important; }
  html.dark .bg-surface-container\\/5 { background-color: rgba(44, 26, 38, 0.05) !important; }
  html.dark .bg-surface-container-low\\/10 { background-color: rgba(34, 21, 29, 0.1) !important; }
  html.dark .bg-surface\\/90 { background-color: rgba(26, 16, 22, 0.9) !important; }
  html.dark .bg-surface\\/80 { background-color: rgba(26, 16, 22, 0.85) !important; }
</style>
"""

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "/* Fix opacity modifier backgrounds" not in content:
        content = content.replace("</style>", opacity_fixes_css)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Applied opacity modifier fixes to {filepath}")
