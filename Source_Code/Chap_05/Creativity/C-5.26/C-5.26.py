# C-5.26
# Let B be an array of size n ≥ 6 containing integers from 1 to n−5, inclusive,
# with exactly five repeated. Describe a good algorithm for finding the
# five integers in B that are repeated.


def find_five_repeating(lst):
    lst = sorted(lst)
    freq = 0
    old = lst[0]
    for index in range(1, len(lst)):
        new = lst[index]
        if new == old:  # if there is a repetition, add one to freq
            freq += 1
            if freq == 5: # if freq is equal to 5, the integer is found
                return new
        else:
            freq = 1  # they are not matching, therefore freq == 1 for the new int
        old = new  # old is the old new
    return None


B = [1, 2, 2, 2, 2, 2, 5, 6]
print(find_five_repeating(B))
