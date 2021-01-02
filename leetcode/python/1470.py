class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_1 = []
        shuffled_2 = []
        total_shuffled = []
        for i in range(n):
            shuffled_1.append(nums[i])
        for j in range(n, 2*n):
            shuffled_2.append(nums[j])
        for i in range(n):
            total_shuffled.append(shuffled_1[i])
            total_shuffled.append(shuffled_2[i])
        return total_shuffled