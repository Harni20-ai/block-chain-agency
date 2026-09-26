import os
import glob

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # The current button class:
    # class="transition-all text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high font-bold rounded-full px-4 py-2 flex items-center gap-1"
    
    # We want to replace it to match the other links (removing font-bold unless it's active, and adding text-sm)
    # Let's just make it perfectly match the normal state:
    old_btn_class = 'class="transition-all text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high font-bold rounded-full px-4 py-2 flex items-center gap-1"'
    new_btn_class = 'class="text-sm text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high px-4 py-2 rounded-full transition-all flex items-center gap-1"'
    
    content = content.replace(old_btn_class, new_btn_class)
    
    # Also ensure the dropdown items are aligned nicely
    # Currently: <div class="absolute left-0 top-full mt-2 w-48 ...
    # We can center the dropdown menu relative to the button
    old_dropdown_container = '<div class="absolute left-0 top-full mt-2 w-48 bg-surface border border-outline-variant rounded-xl shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all flex flex-col overflow-hidden">'
    new_dropdown_container = '<div class="absolute left-1/2 -translate-x-1/2 top-full mt-2 w-40 bg-surface border border-outline-variant rounded-xl shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all flex flex-col overflow-hidden">'
    
    content = content.replace(old_dropdown_container, new_dropdown_container)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed alignment in {filepath}")
