# app.py
# MiniStore - Demo E-Commerce Website using Streamlit

import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS Styling
# --------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }

    .hero-section {
        background: linear-gradient(135deg, #4F46E5, #7C3AED);
        padding: 40px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: bold;
    }

    .hero-text {
        font-size: 18px;
    }

    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        height: 320px;
    }

    .product-name {
        font-size: 20px;
        font-weight: bold;
        color: #222;
    }

    .product-price {
        font-size: 24px;
        color: #16a34a;
        font-weight: bold;
        margin-top: 10px;
    }

    .category-tag {
        background-color: #e0e7ff;
        color: #4338ca;
        padding: 5px 10px;
        border-radius: 15px;
        display: inline-block;
        margin-bottom: 10px;
        font-size: 12px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        color: gray;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sample Product Data
# --------------------------------------------------
products = [
    {
        "name": "Wireless Bluetooth Headphones",
        "price": 2999,
        "category": "Electronics",
        "description": "Premium sound quality with noise cancellation."
    },
    {
        "name": "Smart Fitness Watch",
        "price": 4999,
        "category": "Electronics",
        "description": "Track steps, heart rate, sleep, and workouts."
    },
    {
        "name": "Casual Cotton T-Shirt",
        "price": 799,
        "category": "Fashion",
        "description": "Comfortable and stylish everyday wear."
    },
    {
        "name": "Leather Wallet",
        "price": 1299,
        "category": "Fashion",
        "description": "Premium genuine leather wallet with RFID protection."
    },
    {
        "name": "Coffee Maker",
        "price": 3499,
        "category": "Home Appliances",
        "description": "Brew fresh coffee in minutes."
    },
    {
        "name": "Study Desk Lamp",
        "price": 1499,
        "category": "Home Appliances",
        "description": "Adjustable LED lamp with eye protection technology."
    }
]

# --------------------------------------------------
# Initialize Cart
# --------------------------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(list(set([p["category"] for p in products])))

selected_category = st.sidebar.selectbox(
    "Filter by Category",
    categories
)

# Shopping Cart Summary
st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart Summary")

cart_items = len(st.session_state.cart)
cart_total = sum(item["price"] for item in st.session_state.cart)

st.sidebar.metric("Items", cart_items)
st.sidebar.metric("Total", f"₹{cart_total}")

# --------------------------------------------------
# Homepage Hero Section
# --------------------------------------------------
st.markdown("""
<div class="hero-section">
    <div class="hero-title">🛍️ Welcome to MiniStore</div>
    <div class="hero-text">
        Discover amazing products at unbeatable prices.
        Shop smarter, faster, and better.
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Featured Products Section
# --------------------------------------------------
st.subheader("⭐ Featured Products")
st.write("Explore our best-selling and trending products.")

# Filter Products
if selected_category != "All":
    filtered_products = [
        p for p in products if p["category"] == selected_category
    ]
else:
    filtered_products = products

# --------------------------------------------------
# Product Grid Layout using st.columns
# --------------------------------------------------
cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        st.markdown(f"""
        <div class="product-card">
            <div class="category-tag">{product['category']}</div>
            <div class="product-name">{product['name']}</div>
            <p>{product['description']}</p>
            <div class="product-price">₹{product['price']}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            f"Add to Cart",
            key=product["name"]
        ):
            st.session_state.cart.append(product)
            st.success(f"{product['name']} added to cart!")

# --------------------------------------------------
# Cart Details Section
# --------------------------------------------------
st.markdown("---")
st.subheader("🛒 Cart Details")

if st.session_state.cart:

    for item in st.session_state.cart:
        st.write(f"• {item['name']} - ₹{item['price']}")

    st.success(
        f"Total Amount: ₹{sum(item['price'] for item in st.session_state.cart)}"
    )

else:
    st.info("Your cart is currently empty.")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("""
<div class="footer">
    ©️ 2026 MiniStore | Demo E-Commerce Website Built with Streamlit
</div>
""", unsafe_allow_html=True)
import streamlit as st

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ MiniStore")
st.subheader("Welcome to MiniStore")

# Product Catalog
products = {
    "Wireless Headphones": {
        "price": "$99",
        "description": "Noise-cancelling Bluetooth headphones."
    },
    "Smart Watch": {
        "price": "$149",
        "description": "Track fitness and notifications."
    },
    "Gaming Mouse": {
        "price": "$59",
        "description": "High precision RGB gaming mouse."
    }
}

st.header("Our Products")

cols = st.columns(3)

for col, (name, details) in zip(cols, products.items()):
    with col:
        st.markdown(f"### {name}")
        st.write(details["description"])
        st.success(details["price"])

# Floating support button
st.markdown("""
<style>
.support-btn{
    position:fixed;
    bottom:20px;
    right:20px;
    background:#ff4b4b;
    color:white;
    padding:12px 18px;
    border-radius:30px;
    text-decoration:none;
    font-weight:bold;
    z-index:9999;
}
</style>

<a class="support-btn" href="/Support_Chatbot" target="_self">
💬 Support Chat
</a>
""", unsafe_allow_html=True)

st.info("You can also open 'Support Chatbot' from the left sidebar.")