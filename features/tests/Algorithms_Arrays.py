"""1 - Reverse a Statement
Build an algorithm that will print the given statement in reverse.
Example: Initial string = Everything is hard before it is easy
Reversed string = easy is it before hard is Everything
"""

str1 = "Everything is hard before it is easy"

words = str1.split(" ")
print(words)

words = words[-1::-1]
print(words)

outputstr1 = ' '.join(words)
print(outputstr1)


"""
1. Permutations
Write a solution that will print all permutations of a string.
A permutation is an act of changing the arrangement of characters.
Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}
"""


def permutations(word):
    if len(word) == 1:
        return [word]
    perms = permutations(word[1:])
    char = word[0]
    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])

    return result


print(permutations('ABC'))


"""
Count Characters
Create a program that will count vowels and consonants in a string.
Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}

"""

word = input('Enter e word: ')
vowel_count = 0

for c in word.lower():
    if c in 'aeiou':
        vowel_count += 1

consonant_count = len(word) - vowel_count

print(f'Number of vowels: {vowel_count}')
print(f'Number of cons: {consonant_count}')