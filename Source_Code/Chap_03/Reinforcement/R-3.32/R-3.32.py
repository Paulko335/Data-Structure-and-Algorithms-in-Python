# R-3.32
# Given an n-element sequence S, Algorithm D calls Algorithm E on each
# element S[i]. Algorithm E runs in O(i) time when it is called on element
# S[i]. What is the worst-case running time of Algorithm D?

print("""
S contains n elements
For every element i in S, E runs at O(i)
The worst case is:
O(1) + O(2) + O(3) + ... + O(n) = O(n(n+1)/2) = O(n^2)
""")
