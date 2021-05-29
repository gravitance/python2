'''

EX 133 : WRITE OUT NUMBERS IN ENGLISH

While the popularity of cheques as a payment method has diminished in recent years,
some companies still issue them to pay employees or vendors. The amount being
paid normally appears on a cheque twice, with one occurrence written using digits,
and the other occurrence written using English words. Repeating the amount in two
different forms makes it much more difficult for an unscrupulous employee or vendor
to modify the amount on the cheque before depositing it.

In this exercise, your task is to create a function that takes an integer between 0 and
999 as its only parameter, and returns a string containing the English words for that
number. For example, if the parameter to the function is 142 then your function should
return “one hundred forty two”. Use one or more dictionaries to implement
your solution rather than large if/elif/else constructs. Include a main program that
reads an integer from the user and displays its value in English words.

'''

ones = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}

tens = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

hundreds = {
    "1": "one hundred",
    "2": "two hundred",
    "3": "three hundred",
    "4": "four hundred",
    "5": "five hundred",
    "6": "six hundred",
    "7": "seven hundred",
    "8": "eight hundred",
    "9": "nine hundred"
}

integer = int(input("Enter an integer (0 to 999): "))

try:
    integer = str(integer)
    word = ""

    if integer == "0":
        word = "zero"
    
    else:
        if len(integer) > 2:

            for key, value in hundreds.items():
                if integer[-3] == key:
                    word += value + " "
        
        if len(integer) > 1:

            if integer[-2] == "1":
                for key, value in ones.items():
                    if integer[-2:] == key:
                        word += value
                        
            else:

                for key, value in tens.items():
                    if integer[-2] == key:
                        word += value + " "

                for key, value in ones.items():
                    if integer[-1] == key:
                        word += value

    print(f"The value in words is: {word}.")

except ValueError:
    print("Invalid integer.")