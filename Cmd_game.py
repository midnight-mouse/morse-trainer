import threading
import winsound
import time
import math
import random
import os
import msvcrt
import threading

morse_dict = {
    "A": "*-",
    "B": "-***",
    "C": "-*-*",
    "D": "-**",
    "E": "*",
    "F": "**-*",
    "G": "--*",
    "H": "****",
    "I": "**",
    "J": "*---",
    "K": "-*-",
    "L": "*-**",
    "M": "--",
    "N": "-*",
    "O": "---",
    "P": "*--*",
    "Q": "--*-",
    "R": "*-*",
    "S": "***",
    "T": "-",
    "U": "**-",
    "V": "***-",
    "W": "*--",
    "X": "-**-",
    "Y": "-*--",
    "Z": "--**"
}


class Game():
    def __init__(self) -> None:
        self.level = 0
        self.current_letters = ''
        self.current_seq = ''
        self.letters_by_level = {
            1:['E', 'T'],
            2:['A','I','M','N'],
            3:['D','G','K','O','R','S','U','W',]
        }
        self.new_level()
        self.morse_dict = {
            "A": "*-",
            "B": "-***",
            "C": "-*-*",
            "D": "-**",
            "E": "*",
            "F": "**-*",
            "G": "--*",
            "H": "****",
            "I": "**",
            "J": "*---",
            "K": "-*-",
            "L": "*-**",
            "M": "--",
            "N": "-*",
            "O": "---",
            "P": "*--*",
            "Q": "--*-",
            "R": "*-*",
            "S": "***",
            "T": "-",
            "U": "**-",
            "V": "***-",
            "W": "*--",
            "X": "-**-",
            "Y": "-*--",
            "Z": "--**"
        }

    def new_level(self):
        self.level += 1
        if self.level in self.letters_by_level.keys():
            for letter in self.letters_by_level[self.level]:
                self.current_letters = self.current_letters + letter
                time.sleep(0.2)
        
    def generate_sequence(self, length:int):
        letters = self.current_letters
        seq = ''
        for i in range(length):
            seq = seq +  letters[int(random.random()*len(letters))]
        self.current_seq = seq

    def sound_letter(self, letter):
        dot = 150 # ms
        letter_code = self.morse_dict[letter]

        # Sound each char in a word
        for cur_char in letter_code:
            if cur_char == "*":
                # Short sound
                winsound.Beep(500,dot)
            elif cur_char == "-":
                # Long sound
                winsound.Beep(500,3 * dot)
            time.sleep(dot/1000)
        time.sleep(3*dot/1000)

    def sound_sequence(self):
        for letter in self.current_seq:
            self.sound_letter(letter=letter)
    
    def input_char_by_char(self, corr_string, auto_clear=True):
        mystr = corr_string
        actual_in = []
        tempstr = ""
        for i in range(len(mystr)):
            tempstr = tempstr + "_"
        for i in range(len(mystr)):
            if auto_clear:
                os.system("cls")
                self.print_available()
            print(f"String: {tempstr}")
            mychar = msvcrt.getch()
            actual_in.append(mychar.decode())

            # If correct add to arr
            if mychar.decode().upper() == mystr[i]:
                tempstr = list(tempstr)
                tempstr[i] = mychar.decode()
                tempstr = "".join(tempstr)
            # Else output a !
            else:
                tempstr = list(tempstr)
                tempstr[i] = "!"
                tempstr = "".join(tempstr)
            i+=1
            print(tempstr)

            time.sleep(0.1)
        return "".join(actual_in)
    
    def print_available(self):
            print(f"Available letters: { self.current_letters }")
            for letter in self.current_letters:
                print(letter + " : " + self.morse_dict[letter])

    def play(self):
        seq_len = 5
        while True:
            self.generate_sequence(seq_len)
            soundthread = threading.Thread(target=self.sound_sequence)
            soundthread.start()

            # Take user input one char at a time
            user_in = self.input_char_by_char(self.current_seq)
            if user_in == b"\x03":
                exit(0)
            
            #print("Correct:  " + self.current_seq.lower())
            soundthread.join()
            if user_in.upper() == self.current_seq:
                # Clear screen
                os.system("cls")

                print("Correct!! ")
                print("New level!! \n")
                time.sleep(1)

                os.system("cls")
                print("New letters to lern: ")
                self.new_level()
                
                time.sleep(2)
            else:
                os.system("cls")
                print("Wrong :-/")
                print("Your: " + user_in)
                print("Correct: " + self.current_seq.lower())
                time.sleep(1)
                os.system("cls")

            
            


        
                


game = Game()
game.play()
