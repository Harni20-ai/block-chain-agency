import os

filepath = r"d:\DUMP WEB\web3craft\portfolio.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# The old layout:
old_layout = """<!-- Split Intro Header -->
<div class="flex flex-col lg:flex-row lg:items-end justify-between gap-8">
<div class="flex flex-col gap-6 max-w-3xl">
<div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/20 text-primary-fixed border border-primary/30 text-xs font-headline font-bold uppercase tracking-wider w-fit">
<span class="material-symbols-outlined text-[16px]">verified</span>
          Engineering Authority
        </div>
<h1 class="text-4xl sm:text-6xl lg:text-7xl font-headline font-extrabold text-inverse-on-surface tracking-tight leading-[1.1]">
          Blockchain Products We've <span class="text-primary-container">Engineered</span>
</h1>
<p class="text-lg sm:text-xl text-outline-variant leading-relaxed">
          Explore our portfolio of high-performance decentralized applications, automated DeFi protocols, enterprise-grade NFT marketplaces, and scalable Web3 platforms built with rigorous precision.
        </p>
</div>
<div class="flex flex-col sm:flex-row items-center gap-4 shrink-0">
<a class="w-full sm:w-auto px-8 py-4 rounded-full bg-primary text-on-primary font-headline font-bold shadow-[0_4px_20px_rgba(224,64,160,0.4)] hover:scale-103 transition-transform flex items-center justify-center gap-2" href="#gallery">
            Explore Portfolio
            <span class="material-symbols-outlined text-[18px]">arrow_downward</span>
</a>
<a class="w-full sm:w-auto px-8 py-4 rounded-full bg-surface-container/10 border border-outline/30 text-inverse-on-surface font-headline font-bold hover:bg-surface-container/20 transition-colors text-center" data-path="contact" href="#">
            Request Architecture Audit
          </a>
</div>
</div>"""

new_layout = """<!-- Split Intro Header -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
<div class="flex flex-col gap-6 max-w-3xl">
<div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/20 text-primary-fixed border border-primary/30 text-xs font-headline font-bold uppercase tracking-wider w-fit">
<span class="material-symbols-outlined text-[16px]">verified</span>
          Engineering Authority
        </div>
<h1 class="text-4xl sm:text-6xl lg:text-7xl font-headline font-extrabold text-inverse-on-surface tracking-tight leading-[1.1]">
          Blockchain Products We've <span class="text-primary-container">Engineered</span>
</h1>
<p class="text-lg sm:text-xl text-outline-variant leading-relaxed">
          Explore our portfolio of high-performance decentralized applications, automated DeFi protocols, enterprise-grade NFT marketplaces, and scalable Web3 platforms built with rigorous precision.
        </p>
<div class="flex flex-col sm:flex-row items-center gap-4 shrink-0 pt-4">
<a class="w-full sm:w-auto px-8 py-4 rounded-full bg-primary text-on-primary font-headline font-bold shadow-[0_4px_20px_rgba(224,64,160,0.4)] hover:scale-103 transition-transform flex items-center justify-center gap-2" href="#gallery">
            Explore Portfolio
            <span class="material-symbols-outlined text-[18px]">arrow_downward</span>
</a>
<a class="w-full sm:w-auto px-8 py-4 rounded-full bg-surface-container/10 border border-outline/30 text-inverse-on-surface font-headline font-bold hover:bg-surface-container/20 transition-colors text-center" data-path="contact" href="#">
            Request Architecture Audit
          </a>
</div>
</div>
<div class="relative w-full h-[300px] sm:h-[400px] lg:h-[500px] rounded-3xl overflow-hidden shadow-2xl group border border-outline/20">
    <img src="hero_image.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Web3 Portfolio Visualization" />
    <div class="absolute inset-0 bg-gradient-to-t from-surface-container-lowest/80 to-transparent pointer-events-none mix-blend-overlay"></div>
</div>
</div>"""

if old_layout in content:
    content = content.replace(old_layout, new_layout)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated portfolio.html layout!")
else:
    print("Could not find the old layout block in portfolio.html.")
