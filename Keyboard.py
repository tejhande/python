qwerty_layout = [    ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "backspace"],
    ["tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\"],
    ["caps lock", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "enter"],
    ["shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "shift"],
    ["fn", "ctrl", "alt", "cmd", " ", "cmd", "alt", "left arrow", "down arrow", "up arrow", "right arrow"]
]

for row in qwerty_layout:
    for character in row:
        print(character, end="\t")
    print("\n")
