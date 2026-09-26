import os
import glob

dir_path = r"d:\DUMP WEB\web3craft"
files = glob.glob(os.path.join(dir_path, "*.html"))

old_brand = '<div class="flex items-center gap-3"><div class="w-10 h-10 rounded-full bg-primary flex items-center justify-center shadow-[0_4px_16px_rgba(224,64,160,0.2)]"><span class="material-symbols-outlined text-on-primary text-[20px]">hub</span></div><span class="text-xl font-headline font-bold tracking-tight text-on-surface">CHAINMIND LABS</span></div>'
new_brand = '<a href="index.html" class="flex items-center gap-3 cursor-pointer hover:opacity-80 transition-opacity"><div class="w-10 h-10 rounded-full bg-primary flex items-center justify-center shadow-[0_4px_16px_rgba(224,64,160,0.2)]"><span class="material-symbols-outlined text-on-primary text-[20px]">hub</span></div><span class="text-xl font-headline font-bold tracking-tight text-on-surface">CHAINMIND LABS</span></a>'

favicon_tag = """<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='%23e040a0'/><text y='75' x='50' font-size='70' text-anchor='middle' fill='%23ffffff' font-family='sans-serif'>⚇</text></svg>">
<title>ChainMind Labs</title>
"""

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Replace brand div with anchor tag
    content = content.replace(old_brand, new_brand)
    
    # 2. Inject favicon in head if not exists
    if "<link rel=\"icon\"" not in content:
        # replace <title> tag with favicon + title
        if "<title>" in content:
            # We don't want to replace all titles if they have specific page names, so let's just insert before </head>
            content = content.replace("</head>", favicon_tag + "</head>")
        else:
            content = content.replace("</head>", favicon_tag + "</head>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated brand link and favicon in {filepath}")
