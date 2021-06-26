'''

EX 135 : ANAGRAMS

Two words are anagrams if they contain all of the same letters, but in a different
order. For example, “evil” and “live” are anagrams because each contains one e, one
i, one l, and one v. Create a program that reads two strings from the user, determines
whether or not they are anagrams, and reports the result.

'''

def anagram(s):
    d = {}

    for char in s:
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