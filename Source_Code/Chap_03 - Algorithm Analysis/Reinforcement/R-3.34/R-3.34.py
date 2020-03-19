# R-3.34
# There is a well-known city (which will go nameless here) whose inhabitants
# have the reputation of enjoying a meal only if that meal is the best
# they have ever experienced in their life. Otherwise, they hate it. Assuming
# meal quality is distributed uniformly across a person’s life, describe
# the expected number of times inhabitants of this city are happy with their
# meals?

# Let n be the number of days lived
# People in this city eat only one meal a day
# Therefore, the probability of enjoying a meal is 1/n everyday
#
# The average cumulative number of times an inhabitant enjoyed a meal is the sum of 1/i,
# where i goes from 1 to n

import matplotlib.pyplot as plt

maximum_age = 100       # years
n = maximum_age * 365   # years * days/ years =  years
total_enjoyed_days = 0

xs = []
ys = []

for i in range(1, n+1):
    xs.append(i/365)    # X-axis will be shown in years
    total_enjoyed_days += 1/i
    ys.append(total_enjoyed_days)

plt.plot(xs, ys)
plt.xlabel("Years lived")
plt.ylabel("Average meals enjoyed")
plt.title("Average cumulative number of times an inhabitant\n enjoyed his meal in a well-known city")
plt.show()

print("Y is a harmonic number and we know that it is O(log(n))")
