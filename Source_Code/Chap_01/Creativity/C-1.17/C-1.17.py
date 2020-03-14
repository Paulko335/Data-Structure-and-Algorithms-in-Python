# C-1.17
# Had we implemented the scale function (page 25) as follows, does it work
# properly?
# def scale(data, factor):
# for val in data:
# val = factor
# Explain why or why not.

# No, it will simply create a new variable named val multiple time, data will not be modified