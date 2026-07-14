class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for l in range(len(heights)):
            for r in range(len(heights)-1, 0, -1):
                water = min(heights[l],heights[r]) * (r-l)
                max_water = max(max_water,water)
        return max_water