from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        zeros = nums.count(0)
        if zeros > 1:
            for i in range(len(nums)):
                ans.append(0)
        elif zeros == 0:
            res = prod(nums)
            for i in range(len(nums)):
                a = res // nums[i]
                ans.append(a)
        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    ans.append(0)
                else:
                    l = prod(nums[:i])
                    r = prod(nums[i+1:])
                    a = l*r
                    ans.append(a)
        return ans