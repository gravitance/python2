'''

EX 98 : HEXADECIMAL AND DECIMAL DIGITS

Write two functions, hex2int and int2hex, that convert between hexadecimal
digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and base 10 integers. The
hex2int function is responsible for converting a string containing a single hexadecimal
digit to a base 10 integer, while the int2hex function is responsible for converting an
integer between 0 and 15 to a single hexadecimal digit. Each function
will take the value to convert as its only parameter and return the converted value
as the function’s only result. Ensure that the hex2int function works correctly for
both uppercase and lowercase letters. Your functions should end the program with a
meaningful error message if an invalid parameter is provided.

'''

def hex2int(h):
    h = list(h)
    for i in range(len(h)):
        if h[i] >= "0" and h[i] <= "9":
            h[i] = int(h[i])
        elif h[i].upper() == "A":
            h[i] = 10
        elif h[i].upper() == "B":
            h[i] = 11
        elif h[i].upper() == "C":
            h[i] = 12
        elif h[i].upper() == "D":
            h[i] = 13
        elif h[i].upper() == "E":
            h[i] = 14
        elif h[i].upper() == "F":
            h[i] = 15
        else:
            return "Invalid."
    
    hx = 0
    index = 0

    for i in reversed(h):
        hx += i * (16**index)
        index += 1

    return hx

def int2hex(d):
    dlist = []

    while d > 0:
        r = d % 16
        d = d // 16
        if r >= 0 and r <= 9:
            dlist.append(r)
        elif r == 10:
            dlist.append("A")
        elif r == 11:
            dlist.append("B")
        elif r == 12:
            dlist.append("C")
        elif r == 13:
            dlist.append("D")
        elif r == 14:
            dlist.append("E")
        elif r == 15:
            dlist.append("F")
        else:
            return "Invalid."
    
    h = ""
    for i in reversed(dlist):
        h = h + str(i)

    return h

def main():
    h = "23d1"
    d = 9169
    print(hex2int(h))
    print(int2hex(d))

if __name__ == "__main__":
    main()