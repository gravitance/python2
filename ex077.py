'''

EX 77 : BINARY TO DECIMAL

Write a program that converts a binary (base 2) number to decimal (base 10). Your
program should begin by reading the binary number from the user as a string. Then
it should compute the equivalent decimal number by processing each digit in the
binary number. Finally, your program should display the equivalent decimal number
with an appropriate message.

formula: from the last bit, multiply by 2^(position from last, starting with 0), add to total

'''

binary = input("Enter a binary string: ")

index = 0
decimal = 0

for digit in reversed(binary):
    decimal += int(digit) * (2**index)
    index = index + 1

print(f"decimal: {decimal}")