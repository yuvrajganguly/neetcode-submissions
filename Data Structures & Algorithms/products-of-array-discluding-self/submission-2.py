from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        group = []

        zeros = nums.count(0)
        if zeros > 1:
            for x in range(len(nums)):
                group.append(0)
            return group
        elif zeros == 0:
            pr = prod(nums)
            for x in range(len(nums)):
                g = pr // nums[x]
                group.append(g)
            return group
        else:
            for x in range(len(nums)):
                if nums[x] != 0:
                    group.append(0)
                else:
                    ans = prod(nums[:x]) * prod(nums[x+1:])
                    group.append(ans)
            return group