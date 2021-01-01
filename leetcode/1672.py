class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for a in accounts:
            richest = max(sum(a), richest)
        return richest