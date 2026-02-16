import streamlit as st
import random

st.set_page_config(page_title="Happy Birthday Didi 💖", layout="centered")

# Custom CSS
st.markdown("""
<style>
.big-text {
    font-size: 24px;
    font-weight: bold;
    color: #ff4b8b;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("🎂 Birthday Wishes Generator 💖")
st.write("For My Lovely Elder Sister 💕")

# List of unique wishes
wishes = [
    "You are not just my sister, you are my superhero. 💖",
    "May your life shine brighter than all the candles on your cake! 🎂✨",
    "Thank you for always protecting and guiding me. 💕",
    "You are my first best friend and forever inspiration. 🌸",
    "May happiness follow you everywhere you go. 🎉",
    "You deserve all the love, success, and joy in the world. 💎",
    "Your smile makes our home brighter every day. 🌟",
    "I am lucky to have a sister like you. 💞"
]

# Button to generate wish
if st.button("Generate Birthday Wish 🎉"):
    st.balloons()
    random_wish = random.choice(wishes)
    st.markdown(f'<p class="big-text">{random_wish}</p>', unsafe_allow_html=True)

st.write("---")
st.write("Made with ❤️ by Gaurav")
