class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_of_array = []
        for a in range(len(nums)):
            if a == 0:
                sum_of_array.append(nums[a])
                continue
            sum_of_array.append(nums[a]+sum_of_array[-1])
        return sum_of_array