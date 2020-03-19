# P-1.35
# The birthday paradox says that the probability that two people in a room
# will have the same birthday is more than half, provided n, the number of
# people in the room, is more than 23. This property is not really a paradox,
# but many people find it surprising. Design a Python program that can test
# this paradox by a series of experiments on randomly generated birthdays,
# which test this paradox for n = 5,10,15,20, . . . ,100.

from random import randrange


def same_birthday(n):
    birthdays = {}
    for person in range(n):
        new_date = randrange(1,366)
        if new_date in birthdays:
            return True
        else:
            birthdays[new_date] = 1
    return False


def main():
    print("We are testing the birthday paradox for different number of people")
    print("")
    print("{:16}{:20}{:}".format("Experiments", "Person per test", "Probability (%)"))

    for number_of_person in range(5, 105, 5):
        number_of_experiments = 10000
        same_birthday_cpt = 0
        for experiment in range(number_of_experiments):
            if same_birthday(number_of_person):
                same_birthday_cpt += 1

        probability = same_birthday_cpt / number_of_experiments * 100
        print("{:7} {:16} {:19.2f}".format(number_of_experiments, number_of_person, probability))


if __name__ == "__main__":
    main()
