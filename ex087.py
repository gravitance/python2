'''

EX 87 : CENTRE A STRING IN THE TERMINAL

Write a function that takes a string of characters as its first parameter, and the width of
the terminal in characters as its second parameter. Your function should return a new
string that consists of the original string and the correct number of leading spaces
so that the original string will appear centered within the provided width when it is
printed. Do not add any characters to the end of the string. Include a main program
that demonstrates your function.

'''

def centering(s, width):

    if len(s) > width:
        return s
    
    else:
        spacing = (width - len(s)) // 2
        centered_string = (spacing * " ") + s
        return centered_string

def main():
    s = input("Enter a string: ")
    width = int(input("Enter the width of the terminal in characters (integer only): "))
    print(centering(s, width))

if __name__ == "__main__":
    main()