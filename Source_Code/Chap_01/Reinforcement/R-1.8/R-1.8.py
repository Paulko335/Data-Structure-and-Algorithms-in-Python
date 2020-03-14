# R-1.8
# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index
# −n≤k<0, what is the equivalent index j ≥0 such that s[j] references
# the same element?

s = "This is a string"
n = len(s)
k = -3
j = n + k
if s[k] == s[j]:
    print(True)

# s[k] == s[n + k] if −n≤k<0