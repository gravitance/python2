'''

EX 136 : ANAGRAMS AGAIN

The notion of anagrams can be extended to multiple words. For example, “William
Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
spacing are ignored.

Extend your program from Exercise 135 so that it is able to check if two phrases
are anagrams. Your program should ignore capitalization, punctuation marks and
spacing when making the determination.

'''

def anagram(s):
    d = {}

    for char in s.replace(" ", "").lower():
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    
    return d

if __name__ == "__main__":

    s1 = input("Enter the 1st string: ")
    s2 = input("Enter the 2nd string: ")

    if anagram(s1) == anagram(s2):
        print(f'{s1} and {s2} are anagrams.')
    else:
        print(f'{s1} and {s2} are not anagrams.')