# C-1.25
# Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example,
# if given the string "Let's try, Mike.", this function would return
# "Lets try Mike".


def punctuation_remover(s):
    allowed_char = [chr(ord("a") + i) for i in range(26)] + [chr(ord("A") + i) for i in range(26)] + [" "]
    new_s = ""
    for char in s:
        if char in allowed_char:
            new_s += char
    return new_s


s = "Let's try, Mike."
print(punctuation_remover(s))
