class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            l = max(height[:i]) if i > 0 else 0
            r = max(height[i+1:]) if i < len(height) - 1 else 0
            water = max(min(l,r) - height[i],0)
            ans += water
        return ans
