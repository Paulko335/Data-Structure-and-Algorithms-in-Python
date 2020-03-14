# R-2.16
# Our Range class, from Section 2.3.5, relies on the formula
# max(0, (stop − start + step − 1) // step)
# to compute the number of elements in the range. It is not immediately evident
# why this formula provides the correct calculation, even if assuming
# a positive step size. Justify this formula, in your own words.

print("""
Let's say we want to generate the range between 20 and 10 with a step of 5
We will obtain 10 and 15 but not 20 because the "stop" value is excluded from the serie.

If we examine the formula:
(stop - start) // step gives us the integer number of steps we can do in the range 

But doing so, we might count 1 too many step, because this calculation includes the "stop".
We correct this by substracting 1 to the range (stop - start)
Giving us : (stop - start - 1) // step

Finally, we must add 1 to the integer found, because we add the first step starting at "start"

This formula is also correct for negative steps

""")