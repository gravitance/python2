'''

EX 47 : BIRTH DATE TO ASTROLOGICAL SIGN

The horoscopes commonly reported in newspapers use the position of the sun at the
time of one’s birth to try and predict the future. This system of astrology divides the
year into twelve zodiac signs, as outline in the table below:

Zodiac sign Date range

Capricorn December 22 to January 19
Aquarius January 20 to February 18
Pisces February 19 to March 20
Aries March 21 to April 19
Taurus April 20 to May 20
Gemini May 21 to June 20
Cancer June 21 to July 22
Leo July 23 to August 22
Virgo August 23 to September 22
Libra September 23 to October 22
Scorpio October 23 to November 21
Sagittarius November 22 to December 21

Write a program that asks the user to enter his or her month and day of birth. Then
your program should report the user’s zodiac sign as part of an appropriate output
message.

'''

month = input("Enter your month of birth: ").lower()
day = int(input("Enter your day of birth: "))

if month == "december":
    if day >= 22:
        sign = "Capricorn"
    else:
        sign = "Sagittarius"

elif month == "january":
    if day >= 20:
        sign = "Aquarius"
    else:
        sign = "Capricorn"

elif month == "february":
    if day >= 19:
        sign = "Pisces"
    else:
        sign = "Aquarius"

elif month == "march":
    if day >= 21:
        sign = "Aries"
    else:
        sign = "Pisces"

elif month == "april":
    if day >= 20:
        sign = "Taurus"
    else:
        sign = "Aries"

elif month == "may":
    if day >= 21:
        sign = "Gemini"
    else:
        sign = "Taurus"

elif month == "june":
    if day >= 21:
        sign = "Cancer"
    else:
        sign = "Gemini"

elif month == "july":
    if day >= 23:
        sign = "Leo"
    else:
        sign = "Cancer"

elif month == "august":
    if day >= 23:
        sign = "Virgo"
    else:
        sign = "Leo"

elif month == "september":
    if day >= 23:
        sign = "Libra"
    else:
        sign = "Virgo"

elif month == "october":
    if day >= 23:
        sign = "Scorpio"
    else:
        sign = "Libra"

elif month == "november":
    if day >= 22:
        sign = "Sagittarius"
    else:
        sign = "Scorpio"

else:
    sign = "error"

print(f"your sign is: {sign}.")