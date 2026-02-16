import streamlit as st
import random
import time

st.set_page_config(page_title="Happy Birthday Didi 💖", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #ff1493;
    animation: glow 1.5s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px pink; }
    to { text-shadow: 0 0 25px red; }
}

.wish-box {
    font-size: 24px;
    color: #4b0082;
    text-align: center;
    margin-top: 20px;
    padding: 20px;
    border-radius: 20px;
    background-color: #ffe6f2;
    box-shadow: 0px 0px 25px hotpink;
}

.love-text {
    text-align: center;
    font-size: 22px;
    color: #d63384;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Dancing Cat GIF ----------
st.image("https://gifdb.com/images/high/dancing-cat-happy-birthday-sister-vr4whx4zgno63ci4.gif",
         use_column_width=True)

# ---------- Title ----------
st.markdown('<p class="title">🎉 Happy Birthday Didi! 💖</p>', unsafe_allow_html=True)

st.write("✨ Click below to generate a magical wish ✨")

# ---------- Wishes List ----------
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

if "last_wish" not in st.session_state:
    st.session_state.last_wish = ""

# ---------- Button ----------
if st.button("Generate Special Wish 🎁"):
    st.balloons()

    available = [w for w in wishes if w != st.session_state.last_wish]
    wish = random.choice(available)
    st.session_state.last_wish = wish

    placeholder = st.empty()
    animated_text = ""

    for char in wish:
        animated_text += char
        placeholder.markdown(
            f"<div class='wish-box'>{animated_text}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.04)

    st.markdown(
        '<p class="love-text">Love you forever Didi ❤️<br>– Your Little Brother 💖</p>',
        unsafe_allow_html=True
    )
