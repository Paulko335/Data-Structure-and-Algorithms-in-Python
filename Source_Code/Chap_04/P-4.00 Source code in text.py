import os

def disk_usage(path):
    total = os.path.getsize(path)
    for filename in os.listdir(path):
        if os.path.isdir(filename):
            total += os.path.getsize(os.path.join(path, filename))
    return total

def power(x, n):
    floor = n//2
    if n == 0:
        return 1
#    elif n % 2 == 0:
#        partial = power(x, floor)
#        return partial * partial
#    else:
#        partial = power(x, floor)
#        return x * partial * partial

    else:
        partial = power(x, floor)
        result = partial * partial
        if n % 2 == 1:
            result = x * result
        return result

print(power(2, 10))