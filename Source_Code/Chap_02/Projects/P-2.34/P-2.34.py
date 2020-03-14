# P-2.34
# Write a Python program that inputs a document and then outputs a barchart
# plot of the frequencies of each alphabet character that appears in
# that document.

import numpy as np
import matplotlib.pyplot as plt


def count_characters(input_file):
    char_occurrences = {chr(ord("a") + index): 0 for index in range(26)}
    with open(input_file, "r") as file:
        for line in file:
            for char in line:
                char = char.lower()
                if char in char_occurrences:
                    char_occurrences[char] += 1
    return char_occurrences

# If you want to be able to write the name, replace the line with "file_name=..." the "input(...)"
# input("Please enter the name of the file to analyse with the extension: ")
file_name = "document_to_analyse.txt"
occurrences = count_characters(file_name)

objects = occurrences.keys()
x_pos = np.arange(len(objects))
count = occurrences.values()

plt.bar(x_pos, count)
plt.xticks(x_pos, objects)
plt.ylabel("Occurrence")
plt.title("Distribution of characters in the document")
plt.show()
