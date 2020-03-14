# P-1.36
# Write a Python program that inputs a list of words, separated by whitespace,
# and outputs how many times each word appears in the list. You
# need not worry about efficiency at this point, however, as this topic is
# something that will be addressed later in this book.


def count_occurrences(words):
    alphabet = [chr(ord("a") + i) for i in range(26)]
    counts = {}

    for word in words.split(" "):
        word = word.lower()
        cleaned_word = ""
        for char in word:
            if char in alphabet:
                cleaned_word += char

        if cleaned_word not in counts:
            counts[cleaned_word] = 1
        else:
            counts[cleaned_word] += 1

    print("Occurrences of words inside the sentence\n")
    for key in counts:
        print("{}:{}".format(key, counts[key]))


def main():
    sentence = "Let's count words. This could be useful in the future, who knows? test test test"
    count_occurrences(sentence)


if __name__ == "__main__":
    main()
