import time
import os

RESET = "\033[0m"
BRIGHT = "\033[1m"
CLEAR_SCREEN = "\033[2J"
CURSOR_HOME = "\033[H"

def clear():
    print(CLEAR_SCREEN + CURSOR_HOME, end='')

# Obfuscated duck frames encoded as hex strings
_obf_frames_hex = [
    # Frame 1
    "2020202020205f5f0a202020203c286f2029735f5f5f0a202020202820202e5f3e202f0a202020202020607c7c7c27",
    # Frame 2 (adds colored 'Quack!')
    "2020202020205f5f0a202020203c286f2029735f5f5f0a202020202820202e5f3e202f0a202020202020607c7c7c270a202020202020202033335d517561636b210033305d",
    # Frame 3 (adds colored 'QUACK!!')
    "2020202020205f5f0a202020203c286f2029735f5f5f0a202020202820202e5f3e202f0a202020202020607c7c7c270a202020202020202033315d515541434b2120",
]

def _decode_frame(hex_str: str) -> str:
    # Decode hex to bytes, then to string
    return bytes.fromhex(hex_str).decode("ascii")

def _colorize(text: str, color_code: str) -> str:
    return f"\033[{color_code}m{text}{RESET}"

def animate_duck_hidden():
    frames = []
    for i, h in enumerate(_obf_frames_hex):
        frame = _decode_frame(h)
        if i == 1:
            # Insert yellow "Quack!" line
            frame += "\n   " + _colorize("Quack!", "33")
        elif i == 2:
            # Insert red "QUACK!!" line
            frame += "\n   " + _colorize("QUACK!!", "31")
        frames.append(BRIGHT + frame + RESET)

    for _ in range(3):
        for frame in frames:
            clear()
            print(frame)
            time.sleep(0.5)

if __name__ == "__main__":
    animate_duck_hidden()
