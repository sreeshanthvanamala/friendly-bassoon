"""
data.py — Single source of truth for MiniStore product catalog.
Imported by both app.py (homepage) and pages/2_Support_Chatbot.py (chatbot).
"""
 
PRODUCTS = [
    {
        "id": 1,
        "name": "Merino Wool Crew",
        "category": "Apparel",
        "price": 89.00,
        "emoji": "🧥",
        "description": "Ultra-fine 18.5-micron merino that regulates temperature and resists odour. Wear it three days straight. Nobody will know.",
    },
    {
        "id": 2,
        "name": "Oak Cutting Board",
        "category": "Home",
        "price": 64.00,
        "emoji": "🪵",
        "description": "End-grain white oak with a juice groove. Naturally antimicrobial and built to outlast every knife in your kitchen.",
    },
    {
        "id": 3,
        "name": "Matte Ceramic Mug",
        "category": "Home",
        "price": 28.00,
        "emoji": "☕",
        "description": "Wheel-thrown stoneware with a sand-textured matte glaze. Holds 12 oz and keeps coffee warm longer than machine-made alternatives.",
    },
    {
        "id": 4,
        "name": "Wireless Desk Charger",
        "category": "Tech",
        "price": 49.00,
        "emoji": "⚡",
        "description": "15W Qi2 fast charge for iPhone and Android. Slim aluminium body — sits on a desk without looking like an accessory.",
    },
    {
        "id": 5,
        "name": "Linen Tote Bag",
        "category": "Apparel",
        "price": 36.00,
        "emoji": "👜",
        "description": "Heavy-duty natural linen, reinforced cotton straps. Holds a full grocery run or a 13-inch laptop without bowing.",
    },
    {
        "id": 6,
        "name": "Cold Brew Kit",
        "category": "Kitchen",
        "price": 42.00,
        "emoji": "🫙",
        "description": "2-litre glass jar, stainless mesh filter, rubber lid seal. Makes a litre of concentrate in 12 hours — no electricity, no pods.",
    },
    {
        "id": 7,
        "name": "Minimalist Desk Clock",
        "category": "Home",
        "price": 55.00,
        "emoji": "🕰️",
        "description": "Solid beech body, silent quartz sweep movement. No ticking. Tells the time and nothing else.",
    },
    {
        "id": 8,
        "name": "Brass Mechanical Pencil",
        "category": "Tech",
        "price": 22.00,
        "emoji": "✏️",
        "description": "Brass barrel, 0.5 mm lead, smooth clip. Feels like a tool that costs twice as much.",
    },
]
 
CATEGORIES = ["All"] + sorted(set(p["category"] for p in PRODUCTS))
