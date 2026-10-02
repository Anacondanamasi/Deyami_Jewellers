import json
import os

os.makedirs('src/content/collections', exist_ok=True)
os.makedirs('src/content/products', exist_ok=True)

collections_data = [
    {
        "id": "rings",
        "name": "Rings",
        "slug": "rings",
        "tagline": "Circles of Promise & Everyday Grace",
        "description": "From minimalist solitaire bands to pavé eternity rings, each piece is forged in certified 925 sterling silver to celebrate self-love and cherished bonds.",
        "image": "/images/collections/rings.jpg",
        "featured": True,
        "order": 1
    },
    {
        "id": "earrings",
        "name": "Earrings",
        "slug": "earrings",
        "tagline": "Subtle Sparks Beside Your Face",
        "description": "Feather-light huggies, sleek drops, and celestial studs designed for effortless all-day wear and hypoallergenic comfort.",
        "image": "/images/collections/earrings.jpg",
        "featured": True,
        "order": 2
    },
    {
        "id": "necklaces",
        "name": "Necklaces & Pendants",
        "slug": "necklaces",
        "tagline": "Carried Close to the Heart",
        "description": "Delicate sterling silver chains, glowing chokers, and signature four-point sparkle pendants that layer seamlessly.",
        "image": "/images/collections/necklaces.jpg",
        "featured": True,
        "order": 3
    },
    {
        "id": "bracelets",
        "name": "Bracelets & Cuffs",
        "slug": "bracelets",
        "tagline": "Grace in Every Movement",
        "description": "Sleek sculptural cuffs, shimmering tennis links, and charm bracelets that capture the rhythm of your hands.",
        "image": "/images/collections/bracelets.jpg",
        "featured": True,
        "order": 4
    },
    {
        "id": "anklets",
        "name": "Anklets",
        "slug": "anklets",
        "tagline": "Whispers with Every Step",
        "description": "Dainty double-layered chains and playful silver droplets celebrating quiet joys and breezy wanderlust.",
        "image": "/images/collections/anklets.jpg",
        "featured": True,
        "order": 5
    },
    {
        "id": "gifting-sets",
        "name": "Curated Gifting Sets",
        "slug": "gifting-sets",
        "tagline": "Unbox an Unforgettable Feeling",
        "description": "Thoughtfully paired pendant and earring sets nestled in keepsake packaging, ready to commemorate birthdays, anniversaries, and personal victories.",
        "image": "/images/collections/gifting-sets.jpg",
        "featured": True,
        "order": 6
    }
]

for col in collections_data:
    with open(f"src/content/collections/{col['slug']}.json", 'w', encoding='utf-8') as f:
        json.dump(col, f, indent=2)

products_data = [
    # Rings
    {
        "id": "solitaire-spark-ring",
        "name": "Solitaire Spark 925 Ring",
        "slug": "solitaire-spark-ring",
        "category": "Rings",
        "collectionSlug": "rings",
        "description": "A refined solitaire design set with a radiant bezel-set brilliance accent atop a polished sterling silver band. Effortless everyday luxury.",
        "story": "Inspired by the quiet clarity of midnight stars, designed to remind you of your own steady brilliance.",
        "images": [
            "/images/products/solitaire-spark-ring-1.jpg",
            "/images/products/solitaire-spark-ring-2.jpg"
        ],
        "price": 1850,
        "sku": "DYM-RNG-001",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked",
            "weight": "2.8g approx.",
            "size": "Adjustable / Standard Sizes 10 - 18 Available",
            "finish": "High-Polish Rhodium Plated (Anti-Tarnish)",
            "gemstone": "Hand-Cut AAA Swiss Zirconia",
            "clasp": "Seamless Comfort Fit"
        },
        "tags": ["Best Seller", "Everyday Wear", "Minimalist"],
        "featured": True,
        "newArrival": False,
        "inStock": True
    },
    {
        "id": "eternal-band-ring",
        "name": "Eternal Facet Sterling Band",
        "slug": "eternal-band-ring",
        "category": "Rings",
        "collectionSlug": "rings",
        "description": "Geometric facets carved into solid 925 silver catch and reflect light with every gesture. Clean, gender-neutral, and timeless.",
        "story": "Each hand-finished facet reflects a different perspective of life's continuing journey.",
        "images": [
            "/images/products/eternal-band-ring-1.jpg",
            "/images/products/eternal-band-ring-2.jpg"
        ],
        "price": 2200,
        "sku": "DYM-RNG-002",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked",
            "weight": "3.6g approx.",
            "size": "Sizes 12, 14, 16, 18, 20 Available",
            "finish": "Mirror Polish with Anti-Tarnish E-Coating",
            "gemstone": "None (Solid Silver)",
            "clasp": "Comfort Edge"
        },
        "tags": ["Modern", "Band", "Stackable"],
        "featured": False,
        "newArrival": True,
        "inStock": True
    },

    # Earrings
    {
        "id": "celestial-drop-earrings",
        "name": "Celestial Drop Star Earrings",
        "slug": "celestial-drop-earrings",
        "category": "Earrings",
        "collectionSlug": "earrings",
        "description": "Linear sterling silver drops culminating in our signature DEYAMI four-point star sparkle. Lightweight, movement-loving, and hypoallergenic.",
        "story": "Created to dance with your natural posture, providing an elongated, luminous contour to your face.",
        "images": [
            "/images/products/celestial-drop-earrings-1.jpg",
            "/images/products/celestial-drop-earrings-2.jpg"
        ],
        "price": 2450,
        "sku": "DYM-EAR-001",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked",
            "weight": "3.2g (pair)",
            "size": "45mm drop length",
            "finish": "High-Polish Rhodium Plated",
            "gemstone": "Fine Pavilion Zirconia Sparkle",
            "clasp": "Secure Push-Back with Butterfly"
        },
        "tags": ["Signature", "Party Wear", "Evening"],
        "featured": True,
        "newArrival": True,
        "inStock": True
    },
    {
        "id": "minimalist-huggie-hoops",
        "name": "Classic 925 Huggie Hoops",
        "slug": "minimalist-huggie-hoops",
        "category": "Earrings",
        "collectionSlug": "earrings",
        "description": "Buttery-smooth click-top huggies that embrace the earlobe. The ultimate sleep-in, shower-safe everyday companion.",
        "story": "Designed so comfortably you will never need to take them off.",
        "images": [
            "/images/products/minimalist-huggie-hoops-1.jpg",
            "/images/products/minimalist-huggie-hoops-2.jpg"
        ],
        "price": 1400,
        "sku": "DYM-EAR-002",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked",
            "weight": "2.1g (pair)",
            "size": "12mm outer diameter",
            "finish": "High-Polish Rhodium Plated",
            "gemstone": "None (Solid Silver)",
            "clasp": "Click-In Latch Lock"
        },
        "tags": ["Essential", "Everyday", "Hypoallergenic"],
        "featured": False,
        "newArrival": False,
        "inStock": True
    },

    # Necklaces
    {
        "id": "starlight-pendant-necklace",
        "name": "Starlight Four-Point Pendant",
        "slug": "starlight-pendant-necklace",
        "category": "Necklaces",
        "collectionSlug": "necklaces",
        "description": "The quintessential DEYAMI emblem in miniature. A four-point sparkle pendant strung upon a diamond-cut sterling silver cable chain.",
        "story": "Embodying our motto 'Wear Your Moments' — keep the memory that shaped you closest to your pulse.",
        "images": [
            "/images/products/starlight-pendant-necklace-1.jpg",
            "/images/products/starlight-pendant-necklace-2.jpg"
        ],
        "price": 2650,
        "sku": "DYM-NCK-001",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked",
            "weight": "3.8g approx.",
            "size": "16 inches + 2 inch adjustable extension",
            "finish": "Mirror Polish with E-Shield Coating",
            "gemstone": "Central Pavé Sparkle",
            "clasp": "Lobster Claw Clasp"
        },
        "tags": ["Signature", "Iconic", "Gifting Favourite"],
        "featured": True,
        "newArrival": False,
        "inStock": True
    },
    {
        "id": "luminous-silver-choker",
        "name": "Luminous Herringbone Choker",
        "slug": "luminous-silver-choker",
        "category": "Necklaces",
        "collectionSlug": "necklaces",
        "description": "Silky-smooth liquid silver herringbone chain that lays perfectly flat against the collarbone, shimmering like liquid mercury.",
        "story": "Crafted using micro-articulated Italian link engineering for unparalleled drape and luster.",
        "images": [
            "/images/products/luminous-silver-choker-1.jpg",
            "/images/products/luminous-silver-choker-2.jpg"
        ],
        "price": 3100,
        "sku": "DYM-NCK-002",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked",
            "weight": "5.4g approx.",
            "size": "15 inches + 2 inch extension (3mm width)",
            "finish": "High-Gloss Rhodium Dipped",
            "gemstone": "None",
            "clasp": "Reinforced Lobster Clasp"
        },
        "tags": ["Statement", "Choker", "Luxury"],
        "featured": False,
        "newArrival": True,
        "inStock": True
    },

    # Bracelets
    {
        "id": "infinity-cuff-bracelet",
        "name": "Aura Sleek Open Silver Cuff",
        "slug": "infinity-cuff-bracelet",
        "category": "Bracelets",
        "collectionSlug": "bracelets",
        "description": "Minimalist open-ended bangle forged with tapered tips. Gently flexible for a customized fit on any wrist size.",
        "story": "A clean architectural statement worn standalone or stacked alongside your favourite timepiece.",
        "images": [
            "/images/products/infinity-cuff-bracelet-1.jpg",
            "/images/products/infinity-cuff-bracelet-2.jpg"
        ],
        "price": 3800,
        "sku": "DYM-BRC-001",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked",
            "weight": "8.5g solid silver",
            "size": "Adjustable Open Cuff (fits 5.5 - 7.2 inch wrists)",
            "finish": "Hand-Buffed High Polish",
            "gemstone": "None",
            "clasp": "Slip-on / Squeeze to Fit"
        },
        "tags": ["Cuff", "Solid Silver", "Gender Neutral"],
        "featured": True,
        "newArrival": False,
        "inStock": True
    },
    {
        "id": "sparkle-charm-tennis-bracelet",
        "name": "Pavé Sparkle Charm Tennis Bracelet",
        "slug": "sparkle-charm-tennis-bracelet",
        "category": "Bracelets",
        "collectionSlug": "bracelets",
        "description": "Delicate bezel-linked crystals interwoven on flexible 925 sterling silver settings for breathtaking daylight refraction.",
        "story": "A festive staple reimagined in lightweight sterling silver for modern celebrations.",
        "images": [
            "/images/products/sparkle-charm-tennis-bracelet-1.jpg",
            "/images/products/sparkle-charm-tennis-bracelet-2.jpg"
        ],
        "price": 3450,
        "sku": "DYM-BRC-002",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked",
            "weight": "4.6g approx.",
            "size": "6.5 inches + 1.5 inch extender chain",
            "finish": "Anti-Tarnish Rhodium Plating",
            "gemstone": "Precision Pavé Zirconia",
            "clasp": "Fold-over safety clasp with chain link"
        },
        "tags": ["Tennis Bracelet", "Festive", "Shine"],
        "featured": False,
        "newArrival": True,
        "inStock": True
    },

    # Anklets
    {
        "id": "moonlit-beaded-anklet",
        "name": "Moonlit Double-Layer Silver Anklet",
        "slug": "moonlit-beaded-anklet",
        "category": "Anklets",
        "collectionSlug": "anklets",
        "description": "Double cascading silver chain dotted with miniature diamond-cut spheres that catch every beam of sunlight as you stroll.",
        "story": "Infused with traditional coastal romance and contemporary bohemian grace.",
        "images": [
            "/images/products/moonlit-beaded-anklet-1.jpg",
            "/images/products/moonlit-beaded-anklet-2.jpg"
        ],
        "price": 2150,
        "sku": "DYM-ANK-001",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked",
            "weight": "3.5g approx.",
            "size": "9 inches + 1.5 inch extension",
            "finish": "Dual Coat Anti-Tarnish Lacquer",
            "gemstone": "None",
            "clasp": "Sturdy Spring Ring"
        },
        "tags": ["Boho", "Double Layer", "Summer Vibe"],
        "featured": True,
        "newArrival": False,
        "inStock": True
    },
    {
        "id": "whisper-bell-anklet",
        "name": "Whisper Dainty Chain Anklet",
        "slug": "whisper-bell-anklet",
        "category": "Anklets",
        "collectionSlug": "anklets",
        "description": "An ultra-fine curb chain with tiny suspended silver raindrops that produce a faint, whisper-soft rhythm with foot movement.",
        "story": "A modern homage to nostalgic Indian payals, stripped down to pure minimalist serenity.",
        "images": [
            "/images/products/whisper-bell-anklet-1.jpg",
            "/images/products/whisper-bell-anklet-2.jpg"
        ],
        "price": 1950,
        "sku": "DYM-ANK-002",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked",
            "weight": "2.9g approx.",
            "size": "9.5 inches + 1 inch extension",
            "finish": "High Polish Rhodium",
            "gemstone": "None",
            "clasp": "Lobster Claw"
        },
        "tags": ["Minimal Payal", "Tradition Reimagined", "Dainty"],
        "featured": False,
        "newArrival": True,
        "inStock": True
    },

    # Gifting Sets
    {
        "id": "everyday-elegance-gift-set",
        "name": "The Everyday Elegance Keepsake Set",
        "slug": "everyday-elegance-gift-set",
        "category": "Gifting Sets",
        "collectionSlug": "gifting-sets",
        "description": "Our signature Starlight Sparkle Pendant paired with matching Starlight studs. Packaged in a velvet-lined DEYAMI presentation drawer with authenticity card.",
        "story": "Curated to make someone special feel genuinely cherished without words.",
        "images": [
            "/images/products/everyday-elegance-gift-set-1.jpg",
            "/images/products/everyday-elegance-gift-set-2.jpg"
        ],
        "price": 4200,
        "sku": "DYM-SET-001",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked (Both Items)",
            "weight": "6.2g combined total",
            "size": "Pendant (16+2 in), Studs (8mm)",
            "finish": "Premium Rhodium Flash Plating",
            "gemstone": "AAA Cubic Zirconia Accents",
            "clasp": "Lobster & Push-back"
        },
        "tags": ["Gift Box", "Anniversary", "Birthday Special"],
        "featured": True,
        "newArrival": False,
        "inStock": True
    },
    {
        "id": "bridal-silver-keepsake-box",
        "name": "Silver Blossom Keepsake Trio",
        "slug": "bridal-silver-keepsake-box",
        "category": "Gifting Sets",
        "collectionSlug": "gifting-sets",
        "description": "A collector set combining our Eternal Facet Band, Celestial Drop Earrings, and Starlight Pendant in a velvet travel organizer.",
        "story": "The complete DEYAMI experience, ready to celebrate a milestone achievement or bridal trousseau.",
        "images": [
            "/images/products/bridal-silver-keepsake-box-1.jpg",
            "/images/products/bridal-silver-keepsake-box-2.jpg"
        ],
        "price": 6800,
        "sku": "DYM-SET-002",
        "specs": {
            "material": "925 Sterling Silver",
            "hallmark": "925 BIS Hallmarked (All Pieces)",
            "weight": "12.8g total silver weight",
            "size": "Standard Sized / Custom Ring Sizing on Request",
            "finish": "High-Spec Tarnish-Resistant Coating",
            "gemstone": "Handpicked Brilliant Cut Accents",
            "clasp": "Multiple Premium Findings"
        },
        "tags": ["Milestone Gift", "Bridal Trousseau", "Luxury Box"],
        "featured": True,
        "newArrival": True,
        "inStock": True
    }
]

for prod in products_data:
    with open(f"src/content/products/{prod['slug']}.json", 'w', encoding='utf-8') as f:
        json.dump(prod, f, indent=2)

print(f"Created {len(collections_data)} collections and {len(products_data)} products JSON files successfully!")
