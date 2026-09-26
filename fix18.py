import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Reduce top padding from pt-32 to pt-24 in the first section to tighten the gap
    first_section_match = re.search(r'<section[^>]*class="([^"]*)"[^>]*>', content)
    if first_section_match:
        original_class = first_section_match.group(1)
        if "pt-32" in original_class:
            new_class = original_class.replace("pt-32", "pt-24")
            
            # If it's home2.html, change the gradient to start with some color so it doesn't look like a white void
            if "home2.html" in filepath:
                new_class = new_class.replace("from-surface", "from-primary/10")
                
            # If it's index.html, also make sure it's snug
            if "index.html" in filepath:
                # no background gradient classes to fix in index.html section tag
                pass

            original_tag = first_section_match.group(0)
            new_tag = original_tag.replace(original_class, new_class)
            content = content.replace(original_tag, new_tag, 1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Tightened padding in {filepath}")
