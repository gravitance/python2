'''

EX 63A : TEMPERATURE CONVERSION TABLE

Write a program that displays a temperature conversion table for degrees Celsius and
degrees Fahrenheit. The table should include rows for all temperatures between 0
and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
headings on your columns. The formula for converting between degrees Celsius and
degrees Fahrenheit can be found on the internet.

'''
celsius = []
for degree in range(10,101,10):
    celsius.append(degree)

print(f'-----------------------------------------')
print(f'      celsius             fahrenheit     ')
print(f'-----------------------------------------')

for degree in celsius:
    fahrenheit = (degree * 1.8) + 32
    print(f'        {degree}                  {fahrenheit}     ')
    print(f'-----------------------------------------')
