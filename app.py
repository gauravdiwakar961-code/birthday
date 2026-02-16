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

# ---------- Title ----------
st.markdown('<p class="title">🎉 Happy Birthday Didi! 💖</p>', unsafe_allow_html=True)

st.write("✨ Click below to generate a magical wish ✨")

# ---------- Cake GIF ----------
st.image(
