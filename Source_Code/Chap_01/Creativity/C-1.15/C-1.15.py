# C-1.15
# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).


def are_distincts(numbers):
    set_of_distinct = set()
    for number in numbers:
        if number not in set_of_distinct:
            set_of_distinct.add(number)
        else:
            return False
    return True


distinct_numbers = [1, 2, 3, 4]
print(are_distincts(distinct_numbers))

numbers = [1, 2, 3, 4, 4]
print(are_distincts(numbers))
