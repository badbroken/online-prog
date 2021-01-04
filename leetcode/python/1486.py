from functools import reduce

n = 10
start = 5
print(reduce(lambda x, y: x ^ y, [i for i in range(start, start + n*2, 2)]))
