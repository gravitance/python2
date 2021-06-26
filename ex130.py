'''

EX 130 : TEXT MESSAGING

On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses are
needed for most letters. Pressing the number once generates the first letter on the
key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth
character listed for that key

Write a program that displays the key presses that must be made to enter a text
message read from the user. Construct a dictionary that maps from each letter or
symbol to the key presses. Then use the dictionary to generate and display the presses
for the user’s message. For example, if the user enters Hello, World! then your
program should output 4433555555666110966677755531111. Ensure that
your program handles both uppercase and lowercase letters. Ignore any characters
that aren’t listed in the table above such as semicolons and brackets

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
