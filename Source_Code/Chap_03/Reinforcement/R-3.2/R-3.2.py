# R-3.2
# The number of operations executed by algorithms A and B is 8nlog n and
# 2n2, respectively. Determine n0 such that A is better than B for n ≥ n0.

print("""
Finding n_0:

8n log(n) = 2 n^2
 4 log(n) = n
 log(n^4) = n
    n^4 = 2^n

It is true when n = 16""")
