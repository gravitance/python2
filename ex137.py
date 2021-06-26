'''

EX 137 : SCRABBLE SCORE

In the game of Scrabble™, each letter has points associated with it. The total score
of a word is the sum of the scores of its letters. More common letters are worth fewer
points while less common letters are worth more points. The points associated with
each letter are shown below:

One point A, E, I, L, N, O, R, S, T and U
Two points D and G
Three points B, C, M and P
Four points F, H, V, W and Y
Five points K
Eight points J and X
Ten points Q and Z

Write a program that computes and displays the Scrabble™ score for a word.
Create a dictionary that maps from letters to point values. Then use the dictionary to
compute the score.

A Scrabble™ board includes some squares that multiply the value of a letter
or the value of an entire word. We will ignore these squares in this exercise.

'''

points = {
    "AEILNORSTU": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10
}

word = input("Enter a word: ").upper()
total = 0

for char in word:
    for key, value in points.items():
        if char in key:
            total += value

print(f'"{word}" has a score of {total}.')
