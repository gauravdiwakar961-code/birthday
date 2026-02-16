import streamlit as st
import random
import time

st.set_page_config(page_title="Happy Birthday Didi 💖", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>
.title {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    color: #ff1493;
}

.wish-box {
    font-size: 24px;
    color: #4b0082;
    text-align: center;
    margin-top: 20px;
    padding: 20px;
    border-radius: 15px;
    background-color: #ffe6f2;
    box-shadow: 0px 0px 25px pink;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🎉 Happy Birthday Didi! 💖</p>', unsafe_allow_html=True)

# ---------- Wishes ----------
wishes = [
    "You are my strength and my biggest inspiration. 💕",
    "May your life shine brighter than the stars. 🌟",
    "You deserve unlimited happiness and success. 🎉",
    "Thank you for always supporting me. 🤗",
    "May every dream of yours come true. 💖",
    "You are not just my sister, you are my hero. 🦸‍♀️",
    "Your smile lights up our whole home. ☀️",
    "May this year bring peace, love and laughter. 🎂✨"
]

# Store last wish in session
if "last_wish" not in st.session_state:
    st.session_state.last_wish = ""

if st.button("Generate Special Wish 🎁"):
    st.balloons()

    # Ensure new wish every time
    available_wishes = [w for w in wishes if w != st.session_state.last_wish]
    wish = random.choice(available_wishes)
    st.session_state.last_wish = wish

    placeholder = st.empty()
    animated_text = ""

    # Typewriter animation
    for char in wish:
        animated_text += char
        placeholder.markdown(
            f"<div class='wish-box'>{animated_text}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.04)
