# R-3.1
# Graph the functions 8n, 4nlog n, 2n2, n3, and 2n using a logarithmic scale
# for the x- and y-axes; that is, if the function value f (n) is y, plot this as a
# point with x-coordinate at logn and y-coordinate at logy.

import numpy as np
import matplotlib.pyplot as plt

n = range(1, 128)

plt.figure()
plt.title("Comparison of functions on a log_2 scale")

# Plotting functions
plt.plot(n, [8*i for i in n], label="8n")
plt.plot(n, [4*i*np.log2(i) for i in n], label="4n log(n)")
plt.plot(n, [2*i*i for i in n], label="2n^2")
plt.plot(n, [i*i*i for i in n], label="n^3")
plt.plot(n, [2**i for i in n], label="2^n")

# Setting logarithmic scale of base 2
plt.yscale("log", basey=2)
plt.xscale("log", basex=2)

# Axis labels
plt.xlabel("Log_2(n)")
plt.ylabel("Log_2( f(n) )")

plt.legend()
plt.show()
