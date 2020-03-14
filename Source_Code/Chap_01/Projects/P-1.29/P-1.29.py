# P-1.29
# Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.

chars = "abcdefgh"


def permutations(string):
    if string == "":
        return [string]
    else:
        possibilities = []
        for word in permutations(string[1:]):
            for position in range(len(word) +1):
                possibilities.append(word[:position] + string[0] + word[position:])
    return possibilities


print(len(permutations(chars)))
