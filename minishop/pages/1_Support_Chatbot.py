import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support Assistant")

# Product information known by chatbot
products = {
    "wireless headphones": "$99",
    "smart watch": "$149",
    "gaming mouse": "$59"
}

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            """
Hello! Welcome to MiniStore Support.

I can help with:
- Products
- Delivery
- Refunds
- Returns
- Payment methods
- Order status
            """
        }
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


def chatbot_response(user_query):

    query = user_query.lower()

    # Product questions
    for product, price in products.items():
        if product in query:
            return f"{product.title()} is available for {price}."

    if "product" in query:
        return (
            "Available products:\n\n"
            "• Wireless Headphones - $99\n"
            "• Smart Watch - $149\n"
            "• Gaming Mouse - $59"
        )

    # Delivery
    if any(word in query for word in ["delivery", "shipping"]):
        return (
            "Standard delivery takes 3-5 business days. "
            "Express delivery takes 1-2 business days."
        )

    # Refunds
    if "refund" in query:
        return (
            "Refund requests are processed within "
            "5-7 business days after approval."
        )

    # Returns
    if "return" in query:
        return (
            "Products can be returned within "
            "30 days of purchase."
        )

    # Payment
    if any(word in query for word in
           ["payment", "pay", "upi", "card"]):
        return (
            "We accept:\n"
            "- UPI\n"
            "- Credit Cards\n"
            "- Debit Cards\n"
            "- Net Banking\n"
            "- PayPal"
        )

    # Order Status
    if any(word in query for word in
           ["order", "status", "track"]):
        return (
            "Please provide your Order ID. "
            "Order tracking will be integrated in future versions."
        )

    return (
        "Sorry, I didn't understand that.\n\n"
        "Try asking about products, delivery, refunds, "
        "returns, payment methods, or order status."
    )


# Chat Input
prompt = st.chat_input("Ask a question...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = chatbot_response(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)
        # pages/1_Support_Chatbot.py

```python
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore AI Support Assistant")

# Initialize OpenAI Client
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# Store Catalog
PRODUCT_CATALOG = """
MiniStore Product Catalog

1. Wireless Headphones
   - Price: $99
   - Noise-cancelling Bluetooth headphones

2. Smart Watch
   - Price: $149
   - Fitness tracking and smart notifications

3. Gaming Mouse
   - Price: $59
   - High precision RGB gaming mouse
"""

# System Prompt
SYSTEM_PROMPT = f"""
You are MiniStore's professional customer support assistant.

Your responsibilities:
- Help customers with products.
- Help with orders.
- Help with delivery and shipping.
- Help with refunds.
- Help with returns.
- Help with payment methods.

Store Product Information:
{PRODUCT_CATALOG}

Rules:
1. Only answer questions related to MiniStore.
2. Topics allowed:
   - Products
   - Orders
   - Delivery
   - Shipping
   - Refunds
   - Returns
   - Payments
3. If the customer asks unrelated questions
   (sports, politics, coding, exams, entertainment, etc.)
   politely redirect them back to MiniStore support topics.
4. Be professional, concise, and helpful.
5. Do not invent products not listed in the catalog.
"""

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! Welcome to MiniStore Support.\n\n"
                "I can help you with:\n"
                "- Products\n"
                "- Orders\n"
                "- Delivery\n"
                "- Refunds\n"
                "- Returns\n"
                "- Payments"
            )
        }
    ]

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
prompt = st.chat_input("Ask a MiniStore support question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Build Conversation
    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    conversation.extend(st.session_state.messages)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=conversation,
        temperature=0.3
    )

    assistant_reply = response.choices[0].message.content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
```
