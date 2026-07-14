class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                water = min(heights[l],heights[r]) * (r-l)
                max_water = max(max_water,water)
        return max_water