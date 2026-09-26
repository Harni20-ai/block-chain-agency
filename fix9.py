import os
import glob
import re

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace overly tall minimum heights with a more reasonable responsive minimum
    # or remove them completely to let padding dictate height.
    content = content.replace("min-h-[921px]", "")
    content = content.replace("min-h-[900px]", "")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Removed large min-heights from {filepath}")
