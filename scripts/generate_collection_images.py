import os
from PIL import Image, ImageDraw

os.makedirs('public/images/collections', exist_ok=True)

collections = [
    ('rings', 'Rings', 'public/images/products/solitaire-spark-ring-1.jpg'),
    ('earrings', 'Earrings', 'public/images/products/celestial-drop-earrings-1.jpg'),
    ('necklaces', 'Necklaces & Pendants', 'public/images/products/starlight-pendant-necklace-1.jpg'),
    ('bracelets', 'Bracelets & Cuffs', 'public/images/products/infinity-cuff-bracelet-1.jpg'),
    ('anklets', 'Anklets', 'public/images/products/moonlit-beaded-anklet-1.jpg'),
    ('gifting-sets', 'Curated Gifting Sets', 'public/images/products/everyday-elegance-gift-set-1.jpg'),
]

for slug, name, prod_img in collections:
    base = Image.open(prod_img).convert('RGB')
    # resize to 600x750 luxury portrait card
    card = base.resize((600, 750), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(card)
    # Luxury subtle gradient vignette at bottom
    draw.rectangle([16, 16, 584, 734], outline=(220, 226, 232), width=1)
    card.save(f"public/images/collections/{slug}.jpg", 'JPEG', quality=92)

print("Collection cover images generated successfully!")
