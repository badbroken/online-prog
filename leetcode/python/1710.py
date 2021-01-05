from functools import reduce

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 4
new_list = sum(reduce(lambda x, y: x * y, i) for i in boxTypes)
print(new_list)
