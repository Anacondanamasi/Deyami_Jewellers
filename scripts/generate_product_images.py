import os
import math
from PIL import Image, ImageDraw, ImageFont

os.makedirs('public/images/products', exist_ok=True)

# 12 Sample products definition
products = [
    # Rings
    {'slug': 'solitaire-spark-ring', 'category': 'Rings', 'name': 'Solitaire Spark Ring', 'type': 'ring'},
    {'slug': 'eternal-band-ring', 'category': 'Rings', 'name': 'Eternal Facet Band', 'type': 'band'},
    # Earrings
    {'slug': 'celestial-drop-earrings', 'category': 'Earrings', 'name': 'Celestial Drop Earrings', 'type': 'drop'},
    {'slug': 'minimalist-huggie-hoops', 'category': 'Earrings', 'name': 'Classic Silver Huggie Hoops', 'type': 'hoop'},
    # Necklaces
    {'slug': 'starlight-pendant-necklace', 'category': 'Necklaces', 'name': 'Starlight Four-Point Pendant', 'type': 'pendant'},
    {'slug': 'luminous-silver-choker', 'category': 'Necklaces', 'name': 'Luminous Herringbone Choker', 'type': 'chain'},
    # Bracelets
    {'slug': 'infinity-cuff-bracelet', 'category': 'Bracelets', 'name': 'Aura Sleek Open Cuff', 'type': 'cuff'},
    {'slug': 'sparkle-charm-tennis-bracelet', 'category': 'Bracelets', 'name': 'Pavé Sparkle Charm Bracelet', 'type': 'tennis'},
    # Anklets
    {'slug': 'moonlit-beaded-anklet', 'category': 'Anklets', 'name': 'Moonlit Double-Layer Anklet', 'type': 'anklet'},
    {'slug': 'whisper-bell-anklet', 'category': 'Anklets', 'name': 'Whisper Dainty Chain Anklet', 'type': 'anklet'},
    # Gifting Sets
    {'slug': 'everyday-elegance-gift-set', 'category': 'Gifting Sets', 'name': 'The Everyday Elegance Set (Pendant + Studs)', 'type': 'set'},
    {'slug': 'bridal-silver-keepsake-box', 'category': 'Gifting Sets', 'name': 'Silver Blossom Keepsake Set', 'type': 'box'}
]

def draw_sparkle(draw, cx, cy, r, color=(20, 20, 20, 240)):
    # 4-point star
    pts = [
        (cx, cy - r),
        (cx + r * 0.25, cy - r * 0.25),
        (cx + r, cy),
        (cx + r * 0.25, cy + r * 0.25),
        (cx, cy + r),
        (cx - r * 0.25, cy + r * 0.25),
        (cx - r, cy),
        (cx - r * 0.25, cy - r * 0.25),
    ]
    draw.polygon(pts, fill=color)

def draw_ring(draw, cx, cy):
    # Outer ellipse
    draw.ellipse([cx - 180, cy - 120, cx + 180, cy + 120], outline=(140, 150, 160), width=18)
    draw.ellipse([cx - 170, cy - 110, cx + 170, cy + 110], outline=(225, 232, 240), width=8)
    draw.ellipse([cx - 160, cy - 100, cx + 160, cy + 100], outline=(110, 120, 130), width=4)
    # Gem / Sparkle on top
    draw_sparkle(draw, cx, cy - 120, 50, color=(10, 10, 10, 255))
    draw_sparkle(draw, cx, cy - 120, 30, color=(240, 245, 250, 255))

def draw_band(draw, cx, cy):
    draw.ellipse([cx - 200, cy - 130, cx + 200, cy + 130], outline=(120, 130, 140), width=24)
    draw.ellipse([cx - 190, cy - 120, cx + 190, cy + 120], outline=(235, 240, 245), width=10)

def draw_drop(draw, cx, cy):
    # Two earrings
    for offset in [-110, 110]:
        x = cx + offset
        # Stud
        draw.ellipse([x - 12, cy - 180, x + 12, cy - 156], fill=(120, 130, 140))
        # Chain
        draw.line([x, cy - 156, x, cy + 60], fill=(160, 170, 180), width=6)
        # Teardrop/sparkle
        draw.ellipse([x - 40, cy + 50, x + 40, cy + 150], outline=(130, 140, 150), width=12, fill=(230, 235, 240))
        draw_sparkle(draw, x, cy + 100, 25, color=(10, 10, 10, 255))

def draw_hoop(draw, cx, cy):
    for offset in [-110, 110]:
        x = cx + offset
        draw.ellipse([x - 85, cy - 85, x + 85, cy + 85], outline=(130, 140, 150), width=18)
        draw.ellipse([x - 80, cy - 80, x + 80, cy + 80], outline=(235, 242, 248), width=8)

def draw_pendant(draw, cx, cy):
    # V chain
    draw.arc([cx - 220, cy - 260, cx + 220, cy + 100], 0, 180, fill=(160, 170, 180), width=6)
    # Pendant
    draw_sparkle(draw, cx, cy + 100, 70, color=(10, 10, 10, 255))
    draw_sparkle(draw, cx, cy + 100, 40, color=(240, 245, 250, 255))

def draw_chain(draw, cx, cy):
    draw.arc([cx - 240, cy - 200, cx + 240, cy + 160], 0, 180, fill=(140, 150, 160), width=16)
    draw.arc([cx - 236, cy - 196, cx + 236, cy + 156], 0, 180, fill=(240, 245, 250), width=6)

def draw_cuff(draw, cx, cy):
    draw.arc([cx - 210, cy - 140, cx + 210, cy + 140], 30, 330, fill=(130, 140, 150), width=22)
    draw.arc([cx - 200, cy - 130, cx + 200, cy + 130], 30, 330, fill=(240, 246, 250), width=10)

def draw_tennis(draw, cx, cy):
    draw.ellipse([cx - 220, cy - 140, cx + 220, cy + 140], outline=(180, 190, 200), width=10)
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        px = cx + int(220 * math.cos(rad))
        py = cy + int(140 * math.sin(rad))
        draw_sparkle(draw, px, py, 14, color=(10, 10, 10, 240))

def draw_anklet(draw, cx, cy):
    draw.ellipse([cx - 240, cy - 100, cx + 240, cy + 100], outline=(170, 180, 190), width=8)
    draw.ellipse([cx - 230, cy - 90, cx + 230, cy + 90], outline=(190, 200, 210), width=4)
    # little charms
    for x in [-120, -40, 40, 120]:
        draw.line([cx + x, cy + 95, cx + x, cy + 130], fill=(160, 170, 180), width=4)
        draw_sparkle(draw, cx + x, cy + 135, 12, color=(10, 10, 10, 255))

def draw_set(draw, cx, cy):
    draw_pendant(draw, cx, cy - 70)
    draw_sparkle(draw, cx - 140, cy + 110, 30, color=(10, 10, 10, 255))
    draw_sparkle(draw, cx + 140, cy + 110, 30, color=(10, 10, 10, 255))

def draw_box(draw, cx, cy):
    draw.rectangle([cx - 180, cy - 140, cx + 180, cy + 140], outline=(40, 40, 40), width=4, fill=(245, 247, 250))
    draw.rectangle([cx - 160, cy - 120, cx + 160, cy + 120], outline=(200, 210, 220), width=2)
    draw_sparkle(draw, cx, cy, 60, color=(10, 10, 10, 255))

for p in products:
    # 800x800 square
    img = Image.new('RGB', (800, 800), (248, 249, 250))
    draw = ImageDraw.Draw(img)

    # Subtle vignette / pedestal platform
    draw.ellipse([140, 520, 660, 720], fill=(236, 239, 242))
    draw.ellipse([170, 535, 630, 705], fill=(242, 244, 247))

    # Outer decorative luxury border
    draw.rectangle([24, 24, 776, 776], outline=(226, 232, 238), width=1)
    draw.rectangle([32, 32, 768, 768], outline=(240, 243, 246), width=1)

    cx, cy = 400, 390
    t = p['type']
    if t == 'ring': draw_ring(draw, cx, cy)
    elif t == 'band': draw_band(draw, cx, cy)
    elif t == 'drop': draw_drop(draw, cx, cy)
    elif t == 'hoop': draw_hoop(draw, cx, cy)
    elif t == 'pendant': draw_pendant(draw, cx, cy)
    elif t == 'chain': draw_chain(draw, cx, cy)
    elif t == 'cuff': draw_cuff(draw, cx, cy)
    elif t == 'tennis': draw_tennis(draw, cx, cy)
    elif t == 'anklet': draw_anklet(draw, cx, cy)
    elif t == 'set': draw_set(draw, cx, cy)
    elif t == 'box': draw_box(draw, cx, cy)
    else: draw_sparkle(draw, cx, cy, 80, color=(10, 10, 10, 255))

    # Badge in bottom corner: 925 HALLMARKED
    draw.rectangle([48, 48, 220, 84], outline=(200, 210, 220), width=1, fill=(255, 255, 255))
    draw_sparkle(draw, 64, 66, 8, color=(10, 10, 10, 255))

    # Category tag top right
    draw.rectangle([580, 48, 752, 84], outline=(200, 210, 220), width=1, fill=(255, 255, 255))

    # Save primary image
    p_path = f"public/images/products/{p['slug']}-1.jpg"
    img.save(p_path, 'JPEG', quality=90)

    # Save angle 2 (detail shot)
    img2 = img.crop((120, 120, 680, 680)).resize((800, 800), Image.Resampling.LANCZOS)
    p_path2 = f"public/images/products/{p['slug']}-2.jpg"
    img2.save(p_path2, 'JPEG', quality=90)

print(f"Generated 24 product images for {len(products)} products!")
