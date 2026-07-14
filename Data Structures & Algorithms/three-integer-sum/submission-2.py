class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        ans = []
        for i in range(len((num))):
            seen = {}
            for j in range(i+1,len(num)):
                need = -(num[i] + num[j])
                if need in seen:
                    if sorted([num[i],num[j],need]) not in ans:
                        ans.append(sorted([num[i],num[j],need]))
                else:
                    seen[num[j]] = j
        return ans