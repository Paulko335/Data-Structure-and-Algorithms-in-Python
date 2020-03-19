# P-1.34
# A common punishment for school children is to write out a sentence multiple
# times. Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the sentences and it should
# make eight different random-looking typos.

from random import randrange


def repeat_sentence(s, repetitions):
    alphabet = [chr(ord("a") + num) for num in range(26)]
    for rep_number in range(repetitions):
        typo_s = s
        typo_index = set()

        while len(typo_index) != 8:
            s_index = randrange(0, len(typo_s))
            s_char = typo_s[s_index]

            if s_index not in typo_index and s_char in alphabet:
                char_in_alphabet = alphabet[randrange(0, len(alphabet))]
                typo_s = typo_s[:s_index] + char_in_alphabet + typo_s[s_index + 1:]
                typo_index.add(s_index)
        print("{}. {}".format(rep_number, typo_s))


def main():
    sentence = "I will never spam my friends again."
    number = 100
    repeat_sentence(sentence, number)


if __name__ == "__main__":
    main()
