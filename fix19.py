import os
import re

filepath = r"d:\DUMP WEB\web3craft\home2.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the placement of the decorative background circle that was leaving a void at the top
content = content.replace("top-1/3 left-1/4", "top-10 left-1/4")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated decorative background placement in home2.html")
