import streamlit as st
import random

st.set_page_config(page_title="Happy Birthday Didi 💖", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
.title-text {
    font-size: 36px;
    font-weight: bold;
    color: #ff1493;
    text-align: center;
}
.wish-text {
    font-size: 24px;
    color: #4b0082;
    margin-top: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Main Title
st.markdown('<p class="title-text">🎂 Happy Birthday Didi! 💖</p>', unsafe_allow_html=True)

# Sub-title
st.write("✨ You are amazing, strong, and loved beyond words! ✨")

# List of unique wishes
wishes = [
    "You are the heart of our family 💕",
    "May your life be filled with love and laughter 🎉",
    "Your smile lights up our world ☀️",
    "May you achieve every dream you hold 💎",
    "I am so blessed to have you as my sister 🌸",
    "May today and always bring you joy 💖",
    "You deserve all the happiness in the world 🎈",
    "Every moment with you is a precious memory 🌟"
]

# Button to generate a random wish
if st.button("Generate Special Wish 🎉"):
    st.balloons()
    random_wish = random.choice(wishes)
    st.markdown(f'<p class="wish-text">"{random_wish}"</p>', unsafe_allow_html=True)

st.write("---")
st.write("Made with ❤️ by Gaurav")
