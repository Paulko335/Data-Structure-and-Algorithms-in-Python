# R-4.6
# Describe a recursive function for computing the nth Harmonic number,
# Hn = the sum (Σ) from i=0 to n of 1/i.


def get_Harmonic_recursively(n):
    """Returns the Harmonic number of degree n"""
    if n == 1:
        return 1
    else:
        return 1/n + get_Harmonic_recursively(n-1)
