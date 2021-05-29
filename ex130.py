'''

EX 130 : TEXT MESSAGING

On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses are
needed for most letters. Pressing the number once generates the first letter on the
key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth
character listed for that key

'''

keypad = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

s = "HELLO WORLD!"
keypresses = ""

for ch in s:
    for key, value in keypad.items():
        if ch in value:
            keypresses += key * (value.index(ch)+1)

print(keypresses)
