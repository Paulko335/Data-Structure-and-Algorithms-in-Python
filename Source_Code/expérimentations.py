import numpy as np

les_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in les_x:
    n = np.exp(x)
    print("Pour x = {}, n = {:.2f}".format(x, n))