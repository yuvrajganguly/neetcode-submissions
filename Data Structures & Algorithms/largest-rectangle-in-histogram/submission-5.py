class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for l in range(len(heights)):
            min_height = float("inf")
            for r in range (l, len(heights)):
                min_height = min(min_height, heights[r])
                area = min_height * (r-l+1)
                max_area = max(area, max_area)
        return max_area 