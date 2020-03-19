# C-3.35
# Assuming it is possible to sort n numbers in O(nlog n) time, show that it
# is possible to solve the three-way set disjointness problem in O(n logn)
# time.


# This function is O(n log(n))
def disjoint3(A, B, C):
    '''Returns True is there is no element common to all three lists,
       assuming every list has unique elements.'''
    ABC = A + B + C
    ABC = ABC.sort()    # Sorting in O(nlog(n))
    for index in range(len(ABC - 2)):
        if ABC[index] == ABC[index + 1] == ABC[index + 2]:
            return False
    return True
