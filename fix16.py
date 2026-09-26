import os
import glob
import re
import urllib.parse

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

# Create the exact SVG drawing of a hub network
svg = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>
  <circle cx='50' cy='50' r='50' fill='#e040a0'/>
  <line x1='50' y1='50' x2='50' y2='25' stroke='#ffffff' stroke-width='6'/>
  <line x1='50' y1='50' x2='28' y2='65' stroke='#ffffff' stroke-width='6'/>
  <line x1='50' y1='50' x2='72' y2='65' stroke='#ffffff' stroke-width='6'/>
  <circle cx='50' cy='50' r='10' fill='#e040a0' stroke='#ffffff' stroke-width='5'/>
  <circle cx='50' cy='25' r='8' fill='#ffffff'/>
  <circle cx='28' cy='65' r='8' fill='#ffffff'/>
  <circle cx='72' cy='65' r='8' fill='#ffffff'/>
</svg>"""

# URL encode the SVG for the data URI
encoded_svg = urllib.parse.quote(svg)
new_favicon_tag = f'<link rel="icon" href="data:image/svg+xml,{encoded_svg}">'

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove the old favicon link
    # The old one had the unicode character
    old_favicon_pattern = re.compile(r'<link rel="icon" href="data:image/svg\+xml,[^>]+>')
    content = re.sub(old_favicon_pattern, new_favicon_tag, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated favicon in {filepath}")
