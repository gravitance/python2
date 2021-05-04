'''

EX 10 : ARITHMETIC

Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10a
• The result of a^b

'''
import math

a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))

print(f'a + b = {a+b}')
print(f'b - a = {b-a}')
print(f'a * b = {a*b}')
print(f'quotient of a/b = {a//b}')
print(f'remainder of a/b = {a%b}')
print(f'log10(a) = {math.log10(a)}')
print(f'a^b = {a**b}')
