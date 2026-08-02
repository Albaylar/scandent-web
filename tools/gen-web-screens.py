#!/usr/bin/env python3
"""
ScanDent web sitesi için app ekran görüntülerini optimize eder.
Kaynak: ~/Desktop/ScanDent-AppStore/selected/  → çıktı: scandent-web/assets/screens/

Çalıştırma (Mac'te):
    cd ~/Developer/scandent-web
    pip3 install pillow      # bir kez
    python3 tools/gen-web-screens.py
"""
import os, sys
from PIL import Image

SRC = os.path.expanduser("~/Desktop/ScanDent-AppStore/selected")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "screens")
WIDTH = 560          # web görüntü genişliği (retina için 2x ~ 280px gösterim)
QUALITY = 82

# kaynak dosya  ->  web dosya adı (index.html bunlara bakıyor)
MAPPING = {
    "02-home-scored.png":            "home.jpg",
    "01-result-hero.png":            "score.jpg",
    "03-whitening-before-after.png": "whitening.jpg",
    "05-plan-streak.png":            "plan.jpg",
    "06-food-analyzer.png":          "food.jpg",
    "07-progress-chart.png":         "progress.jpg",
}

def main():
    os.makedirs(OUT, exist_ok=True)
    missing = []
    for src, dst in MAPPING.items():
        sp = os.path.join(SRC, src)
        if not os.path.exists(sp):
            missing.append(src); continue
        im = Image.open(sp).convert("RGB")
        h = int(im.height * WIDTH / im.width)
        im = im.resize((WIDTH, h), Image.LANCZOS)
        dp = os.path.join(OUT, dst)
        im.save(dp, "JPEG", quality=QUALITY, optimize=True)
        print(f"  {dst}  {im.size}  {os.path.getsize(dp)//1024}KB")
    if missing:
        print("UYARI: bulunamayan kaynaklar:", ", ".join(missing))
        print("Kaynak klasörü:", SRC)
    print("Bitti. assets/screens/ hazır. Sonra: git add -A && git commit -m 'Add app screenshots' && git push")

if __name__ == "__main__":
    main()
