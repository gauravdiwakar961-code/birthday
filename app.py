import streamlit as st
import random
import time

st.set_page_config(page_title="Happy Birthday Didi 💖", layout="centered")

# ----------------- CSS Animation -----------------
st.markdown("""
<style>
.blink {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    color: #ff1493;
    animation: blink-animation 1.5s infinite;
}

@keyframes blink-animation {
    0% {opacity: 1;}
    50% {opacity: 0.5;}
    100% {opacity: 1;}
}

.wish-box {
    font-size: 24px;
    color: #4b0082;
    text-align: center;
    margin-top: 20px;
    padding: 20px;
    border-radius: 15px;
    background-color: #ffe6f2;
    box-shadow: 0px 0px 20px pink;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="blink">🎉 Happy Birthday Didi! 💖</p>', unsafe_allow_html=True)

st.write("✨ Click below to generate a magical wish ✨")

# Wishes list
wishes = [
    "You are my strength, my guide, and my forever inspiration. 💕",
    "May your life be filled with endless happiness and success. 🌸",
    "You deserve all the love and joy in this world. 💖",
    "Thank you for always standing beside me. 🤗",
    "May every dream you have turn into reality. 🌟",
    "You are not just my sister, you are my superhero. 🦸‍♀️",
    "Your smile makes everything brighter. ☀️",
    "May this birthday bring you peace, love, and laughter. 🎂✨"
]

# Button
if st.button("Generate Special Wish 🎁"):
    st.balloons()
    wish = random.choice(wishes)

    placeholder = st.empty()
    animated_text = ""

    # Typewriter animation
    for char in wish:
        animated_text += char
        placeholder.markdown(
            f"<div class='wish-box'>{animated_text}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.05)
