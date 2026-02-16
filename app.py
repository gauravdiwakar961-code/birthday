import streamlit as st

# Title
st.title("🎂 Birthday Celebration App 🎂")

# Inputs
name = st.text_input("Enter the Birthday Girl's Name")
age = st.number_input("Enter Age", min_value=1, step=1)

# Button
if st.button("Celebrate 🎉"):
    st.success(f"🎉 Happy {age} Birthday, {name}! 🎂")
    st.balloons()

