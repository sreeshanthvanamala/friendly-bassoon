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