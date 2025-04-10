import streamlit as st

# Product origin database (can be expanded!)
product_origin = {
    "iPhone": "USA",
    "Coca-Cola": "USA",
    "Tesla Model 3": "USA",
    "MacBook": "USA",
    "Nike Shoes": "USA",
    "Levi's Jeans": "USA",
    "Samsung Galaxy": "South Korea",
    "Toyota Corolla": "Japan",
    "Adidas Sneakers": "Germany",
    "Nespresso": "Switzerland",
    "Rivella": "Switzerland"
}

# App UI
st.set_page_config(page_title="Is it from the USA?", page_icon="🇺🇸")
st.title("🇺🇸 Is It From the USA?")
st.write("Enter a product name to check if it originates from the USA.")

product_input = st.text_input("🔍 Product Name")

if product_input:
    normalized_input = product_input.strip().title()
    
    if normalized_input in product_origin:
        origin = product_origin[normalized_input]
        if origin == "USA":
            st.success(f"✅ Yes, **{normalized_input}** is from the USA.")
        else:
            st.error(f"❌ No, **{normalized_input}** is from **{origin}**.")
    else:
        st.warning("🤔 Sorry, that product isn’t in our database yet.")
        st.info("💡 Try a well-known brand or suggest new ones to be added!")
