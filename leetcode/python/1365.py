nums =  [6,5,4,8]
final_count = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] > nums[j]:
            count += 1
    final_count.append(count)
print(final_count)
