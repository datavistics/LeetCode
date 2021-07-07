from timeit import timeit

print(timeit("1 * (1-0);1 * (0-1)"))
print(timeit("1 * (not 0);1 *(not 1)"))
