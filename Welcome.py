import streamlit as st
import winsound
import time

header = st.container()

with header:
    st.title("Morse Trainer")
    st.write("Welcome to Morse Trainer! The aim of this app is to teach you morse code through a series of levels.")

    result = st.button("Click Here")

    if result:
        st.write("You clicked the button")
        winsound.Beep(500, 100)
        time.sleep(0.4)
        winsound.Beep(500, 100)