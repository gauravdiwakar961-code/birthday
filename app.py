import streamlit as st
import random
import time

st.set_page_config(
    page_title="Happy Birthday Didi ❤️",
    page_icon="🎂",
    layout="centered"
)

# -------------------- CSS --------------------
st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#ffe6f2,#fff5cc,#e6f7ff);
}

.title{
    text-align:center;
    color:#ff1493;
    font-size:50px;
    font-weight:bold;
    text-shadow:2px 2px 15px #ff69b4;
}

.sub{
    text-align:center;
    color:#8a2be2;
    font-size:22px;
}

.wish{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 0px 20px hotpink;
    color:#4b0082;
    font-size:24px;
    text-align:center;
    margin-top:20px;
}

.footer{
    text-align:center;
    color:#d63384;
    font-size:24px;
    margin-top:30px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------- Balloons --------------------
st.balloons()

# -------------------- GIF --------------------
st.image(
    "https://media.tenor.com/5bC5P8v0fVIAAAAM/happy-birthday.gif",
    use_container_width=True
)

# -------------------- Title --------------------
st.markdown("<div class='title'>🎉 HAPPY BIRTHDAY DIDI 🎂</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='sub'>💖 Wishing you endless happiness, success and love 💖</div>",
    unsafe_allow_html=True
)

st.write("")

# -------------------- Wishes --------------------
wishes = [

"🌸 Dear Didi, may your life always be filled with happiness, love and beautiful memories.",

"💖 Thank you for always supporting and caring for me. You are truly the best sister.",

"🌟 May God bless you with good health, success, peace and endless smiles.",

"🎂 I pray every dream in your heart comes true. You deserve all the happiness in the world.",

"❤️ You are not only my sister, you are my best friend and my biggest strength.",

"✨ May your smile always shine brighter than the stars.",

"🎁 Wishing you a wonderful birthday full of love, laughter and lots of cake.",

"🥳 Happy Birthday to the most amazing Didi in the world!"
]

if "last" not in st.session_state:
    st.session_state.last = ""

# -------------------- Button --------------------
if st.button("🎁 Click for a Special Birthday Wish"):

    available = [i for i in wishes if i != st.session_state.last]

    wish = random.choice(available)

    st.session_state.last = wish

    placeholder = st.empty()

    text = ""

    for ch in wish:
        text += ch
        placeholder.markdown(
            f"<div class='wish'>{text}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.03)

    st.balloons()

    st.markdown("""
<div class='footer'>
💖 Happy Birthday Once Again Didi 💖
<br><br>
May God always keep you smiling 😊
<br><br>
🎂 Enjoy your special day! 🎂
<br><br>
❤️ Love You Forever ❤️
<br>
— Your Loving Brother 🤗
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("⭐ Made with Love ⭐")
