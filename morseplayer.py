import streamlit as st
import threading
import winsound
import time
import math
import random
import os
import msvcrt
import threading


class Game():
    def __init__(self, stobj:st.container,handleelem,sound_creator,output_under, level=0 ) -> None:
        self.level = level
        self.seq_len = 5
        self.handleelem = handleelem
        self.sound_creator = sound_creator
        self.current_seq = ''
        self.output_under = output_under
        self.letters_by_level = {
            1:['E', 'T'],
            2:['A','I','M','N'],
            3:['D','G','K','O','R','S','U','W',]
        }
        self.st = stobj

        self.current_letters = self.letters_by_level[self.level]

    def generate_sequence(self, length:int):
        letters = self.current_letters
        seq = ''
        for i in range(length):
            seq = seq +  letters[int(random.random()*len(letters))]
        self.current_seq = seq

    def input_streamlit(self):
        print("s")

    def play(self):
        
        # Genereate sequence
        self.generate_sequence(self.seq_len)

        # Create audio file
        sound_file = self.sound_creator.create_audio_from(self.current_seq)
        st.audio(sound_file,sample_rate=self.sound_creator.sample_rate)
        # Create input box
        with self.handleelem:
            # Input box
            user_in = st.text_input("Write here", key="Inp")
            

            # Take user input one char at a time
            if user_in:
                st.write(user_in)
                print(st.session_state["Inp"])
                if user_in.upper() == self.current_seq:
                    # Genereate sequence
                    self.generate_sequence(self.seq_len)

                    # Create audio file
                    sound_file = self.sound_creator.create_audio_from(self.current_seq)
                    st.audio(sound_file,sample_rate=self.sound_creator.sample_rate)

                
if __name__ == "__main__":
    game = Game()
    game.play()
