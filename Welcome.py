import streamlit as st
import winsound
import time
from sound_creator import *
import numpy as np
import pandas as pd

header = st.container()
background = st.container()
tutorial = st.container()
references = st.container()

sound_module = SoundCreator()

with header:
    st.title("Morse Trainer Whop!")
    st.info("Welcome to **Morse Trainer!** The aim of this app is to teach you morse code through a series of interactive levels.")

    st.write("According to Wikipedia: \"Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes, or dits and dahs. Morse code is named after Samuel Morse, one of the inventors of the telegraph.\"")
    st.write("In short, Morse Code is a way to use short beeps and long beeps to convey messages.")

with background:

    st.header("The Morse Code Alphabet")
    st.write("Every letter is converted into a sequence of dots and dashes. Dots represent short beeps. Dashes represent long beeps. The most common letters, such as 'E' and 'T', usually have shorter sequences - making them faster to transmit.")
    st.image("assets/morse_code.webp")
    st.caption("*[Image Source](https://medium.com/fgd1-the-archive/morse-code-771534ff98e4)* :sunglasses:")

    st.markdown("""
    The Morse code adheres to the following rules:
    * The length of a dot is one unit.
    * A dash is three units.
    * The space between parts of the same letter is one unit.
    * The space between letters is three units.
    * The space between words is seven units.
    """)

    st.write("Using mnemonics is a popular way to make learning the morse sequences easier. Below is a visual mnemonic of the morse code alphabet. Read each letter top-down (except Z). The \"di\" represent short beeps/dots, and the \"dah\" represent long beeps/dashes.")

    st.image("assets/visualmnemonic.png")
    st.caption("*[Image Source](https://en.wikipedia.org/wiki/Morse_code_mnemonics)* :sunglasses:")

with tutorial:
    st.header("Tutorial")
    st.markdown("To learn the format of this guide, let us begin with the most important morse sequence: the emergency call **SOS**. To learn this sequence, we need two letters: **S** and **O**.")

    SOS = {
        "Letter" : ["S", "O"],
        "Code": ["* * *", "- - -"],
        "Mnemonic": ["sí-sí-sí", "OH! MY! GOD!"]
    }

    st.table(SOS)

    st.markdown("Have a listen to the letters **S** and **O** played *three times each* below:")

    s = sound_module.create_audio_from("S S S")
    st.audio(s, sample_rate=sound_module.sample_rate)

    o = sound_module.create_audio_from("O O O")
    st.audio(o, sample_rate=sound_module.sample_rate)

    st.markdown("Could you hear the difference? Try to say the corresponding letter while listening and learn their rhythm. Below you can hear a sequence of S's and O's in action together.")

    st.markdown("**Sequence:** SOS OOS SSO SOS")

    so_sequence = sound_module.create_audio_from("SOS OOS SSO SOS")
    st.audio(so_sequence, sample_rate=sound_module.sample_rate)

    st.subheader("Practice")
    st.write("Click play to hear a sequence of S's and O's. Type what you hear and press ENTER. The program will give you feedback.")
    
    audio = sound_module.create_audio_from("SOS SSO OOS SSO OSO")
    st.audio(audio, sample_rate=sound_module.sample_rate)

    SOS_input = st.text_input(":blue[Type what you hear] 👇", key="SOS")

    if SOS_input:
        correct_sequence = "SSOO"
        saved_input = st.session_state["SOS"]

        # Compare correct sequence with inputed sequence
        write_string = ""

        for c1, c2 in zip(list(correct_sequence), list(saved_input)[:len(correct_sequence)]):
            if c1.upper() == c2.upper():
                write_string += f":green[{c2}]"
            else:
                write_string += f":red[{c2}]"

        if len(saved_input) > len(correct_sequence):
            write_string += f":orange[{saved_input[len(correct_sequence):]}]"

        st.write(write_string)
        st.write(f"Correct: {correct_sequence}")

with references:
    st.header("References")

    st.markdown("""
    * Streamlit, [API Reference](https://docs.streamlit.io/library/api-reference)
    * Wikipedia, [Morse Code Mnemonic](https://en.wikipedia.org/wiki/Morse_code_mnemonics)
    * Chloe Wooldrage, Medium, ['Morse Code (1836)'](https://medium.com/fgd1-the-archive/morse-code-771534ff98e4)
    """)