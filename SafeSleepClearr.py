# SafeSleepClear1.1.py

import time #Imports "time" giving us the ability to "sleep" the program
import sys
import os #Imports "os" giving us the ability to "clear" the terminal
import select

def safe_sleep_clear(seconds=1):
    time.sleep(seconds) #Sleeps for a certain amount of time (1 by default)
    while select.select([sys.stdin], [], [], 0)[0]:
        sys.stdin.read(1)
    os.system('cls' if os.name == 'nt' else 'clear') #Give the ilussion it clears the terminal

#Original copy made 2024 as a personal project & collaboration.
#BurntCr1sp, 2025

"""
▄▄▄ ▄▄▄ █    ▄▄▄ ▄▄▄ ▄▄▄    ▄▄▄ ▄▄▄ ▄▄▄    ▄▄▄ █ █        

█ ▄▄▄ █ █    █ █ ▄▄▄    ▄▄▄ █ ▄▄▄ █    ▄▄▄ █ ▄▄▄
"""
