import os
import glob

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Fix the dropdown text
    content = content.replace("Home 1: Engineering", "Home 1")
    content = content.replace("Home 2: Studio", "Home 2")
    
    # 2. Fix the globeToggle and themeToggle selectors
    # The previous script had:
    # const themeToggle = document.querySelector('header button:nth-child(2)');
    # const globeToggle = document.querySelector('header button:nth-child(1)');
    
    bad_theme_selector = "const themeToggle = document.querySelector('header button:nth-child(2)');"
    good_theme_selector = "const themeToggle = Array.from(document.querySelectorAll('header button')).find(btn => btn.textContent.includes('light_mode') || btn.textContent.includes('dark_mode'));"
    
    bad_globe_selector = "const globeToggle = document.querySelector('header button:nth-child(1)');"
    good_globe_selector = "const globeToggle = Array.from(document.querySelectorAll('header button')).find(btn => btn.textContent.includes('globe'));"
    
    content = content.replace(bad_theme_selector, good_theme_selector)
    content = content.replace(bad_globe_selector, good_globe_selector)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {filepath}")
