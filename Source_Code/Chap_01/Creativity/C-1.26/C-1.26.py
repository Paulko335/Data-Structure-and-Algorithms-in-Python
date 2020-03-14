# C-1.26
# Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”


def is_arithmetic(a, b, c):
    integers = [str(a), str(b), str(c)]
    operators = "+-*/"

    n = len(integers)
    m = len(operators)

    # arithmetic format: a operator b == c
    possibilities = []
    for i in range(n):
        for j in range(m):
            for k in range(n):
                for l in range(n):
                    if i != k and i != l and k != l:
                        possibilities.append("{}{}{}=={}".format(integers[i], operators[j], integers[k], integers[l]))

    for possibility in possibilities:
        if eval(possibility):
            return True
    return False


a, b, c = input("Enter three integers, separated by a comma: ").split(",")
print(is_arithmetic(int(a), int(b), int(c)))
