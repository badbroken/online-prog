nums = [1, 2, 3, 4, 0]
index = [0, 1, 2, 3, 0]

target_array = []
for i in range(len(nums)):
    target_array.insert(index[i], nums[i])

print(target_array)
