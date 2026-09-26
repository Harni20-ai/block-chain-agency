import os
import glob
import re
import urllib.parse

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

# Create the EXACT SVG drawing of the 5-node hub network from the screenshot
svg = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>
  <circle cx='50' cy='50' r='50' fill='#e040a0'/>
  
  <!-- Connecting lines drawn first so they sit under the circles -->
  <g stroke='#ffffff' stroke-width='6' stroke-linecap='round'>
    <line x1='50' y1='50' x2='50' y2='25'/>
    <g transform='rotate(72 50 50)'><line x1='50' y1='50' x2='50' y2='25'/></g>
    <g transform='rotate(144 50 50)'><line x1='50' y1='50' x2='50' y2='25'/></g>
    <g transform='rotate(216 50 50)'><line x1='50' y1='50' x2='50' y2='25'/></g>
    <g transform='rotate(288 50 50)'><line x1='50' y1='50' x2='50' y2='25'/></g>
  </g>
  
  <!-- Hollow rings drawn on top (filled with background color so lines don't show inside) -->
  <g stroke='#ffffff' stroke-width='5' fill='#e040a0'>
    <circle cx='50' cy='50' r='8'/>
    <circle cx='50' cy='25' r='7'/>
    <g transform='rotate(72 50 50)'><circle cx='50' cy='25' r='7'/></g>
    <g transform='rotate(144 50 50)'><circle cx='50' cy='25' r='7'/></g>
    <g transform='rotate(216 50 50)'><circle cx='50' cy='25' r='7'/></g>
    <g transform='rotate(288 50 50)'><circle cx='50' cy='25' r='7'/></g>
  </g>
</svg>"""

# URL encode the SVG for the data URI
encoded_svg = urllib.parse.quote(svg)
new_favicon_tag = f'<link rel="icon" href="data:image/svg+xml,{encoded_svg}">'

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove the old favicon link
    old_favicon_pattern = re.compile(r'<link rel="icon" href="data:image/svg\+xml,[^>]+>')
    content = re.sub(old_favicon_pattern, new_favicon_tag, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated favicon to exact replica in {filepath}")
