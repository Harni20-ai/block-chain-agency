import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Remove the 80px gap (pt-20) from the main wrapper
    content = content.replace('class="w-full pt-20 bg-surface"', 'class="w-full bg-surface"')
    
    # 2. Adjust the first <section> to have adequate top padding so content clears the fixed header
    # We will find the first <section ...> and replace its vertical padding with pt-32 pb-16 or similar.
    # To do this safely, we find the first <section ...> tag.
    first_section_match = re.search(r'<section[^>]*class="([^"]*)"[^>]*>', content)
    
    if first_section_match:
        original_class = first_section_match.group(1)
        new_class = original_class
        
        # Remove existing vertical paddings
        new_class = re.sub(r'\bpy-\d+\b', '', new_class)
        new_class = re.sub(r'\blg:py-\d+\b', '', new_class)
        new_class = re.sub(r'\bpt-\d+\b', '', new_class)
        new_class = re.sub(r'\bpb-\d+\b', '', new_class)
        
        # Add pt-32 pb-16
        new_class = new_class.strip() + " pt-32 pb-16"
        
        # Clean up any double spaces
        new_class = re.sub(r'\s+', ' ', new_class)
        
        # Replace only the first occurrence of the original class string in the file 
        # (assuming the first section is unique enough, but let's replace the whole tag to be safe)
        original_tag = first_section_match.group(0)
        new_tag = original_tag.replace(original_class, new_class)
        
        content = content.replace(original_tag, new_tag, 1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Removed gap and adjusted hero padding in {filepath}")
