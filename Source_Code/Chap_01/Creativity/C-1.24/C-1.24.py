# C-1.24
# Write a short Python function that counts the number of vowels in a given
# character string.


def vowels_count(a_string):
    vowels_dict = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "y": 0}
    for char in a_string.lower():
        if char in vowels_dict:
            vowels_dict[char] += 1
    return sum(vowels_dict.values())


a_string = "Can you count the number of vowels in this sentence please?"
print(vowels_count(a_string))
