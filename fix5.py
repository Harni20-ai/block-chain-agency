import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Fix dropdown text centering
    old_item1 = '<a class="px-4 py-3 text-sm text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface" data-path="home-engineering-authority" href="index.html">Home 1</a>'
    new_item1 = '<a class="px-4 py-3 text-sm text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface text-center" data-path="home-engineering-authority" href="index.html">Home 1</a>'
    
    old_item2 = '<a class="px-4 py-3 text-sm text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface" data-path="home-web3-studio" href="home2.html">Home 2</a>'
    new_item2 = '<a class="px-4 py-3 text-sm text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface text-center" data-path="home-web3-studio" href="home2.html">Home 2</a>'
    
    content = content.replace(old_item1, new_item1)
    content = content.replace(old_item2, new_item2)

    # Fix services.html swapBtn script
    if 'swapBtn' in content:
        old_selector = "const swapBtn = document.querySelector('button');"
        new_selector = "const swapBtn = Array.from(document.querySelectorAll('button')).find(btn => btn.textContent.includes('Execute Swap Transaction'));"
        content = content.replace(old_selector, new_selector)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {filepath}")
