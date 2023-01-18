from morseplayer import Game
import streamlit as st
from sound_creator import SoundCreator

menu = st.container()

with menu:    
    st.header("Title Level 1")
    SOS = {
        "Letter" : ["E", "T"],
        "Code": ["-", "*"],
        "Mnemonic": ["sí-sí-sí", "OH! MY! GOD!"]
    }

    st.table(SOS)



stobj = st.container()
sc = SoundCreator()

bottom = st.container()
with stobj:
    game = Game(st, handleelem=stobj,sound_creator=sc,output_under=bottom,level=1 )
    game.play()
        