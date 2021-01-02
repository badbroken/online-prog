class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kids_candies = []
        for a in candies:
            if a+extraCandies >= max(candies):
                kids_candies.append(True)
                continue
            kids_candies.append(False)
        return kids_candies