# C-1.19
# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

alphabet = [chr(ord("a") + i) for i in range(26)]
print(alphabet)
