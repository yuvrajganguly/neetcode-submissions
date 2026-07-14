class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        ans = []
        seen = set()
        for i in range(len((num))):
            l = i + 1
            r = len(num) - 1
            while r > l:
                cur = num[i] + num[l] + num[r]
                if cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    triplet = (num[i],num[l],num[r])
                    if triplet not in seen:
                        ans.append(list(triplet))
                        l += 1
                        r -= 1
                        seen.add(triplet)
                    else:
                        l += 1
                        r -= 1
                        
        return ans
