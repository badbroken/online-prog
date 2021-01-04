nums = [1,1,2,3]
decompressed = []
for i in range(0, len(nums) - 1, 2):
    for j in range(nums[i]):
        decompressed.append(nums[i + 1])

print(decompressed)
