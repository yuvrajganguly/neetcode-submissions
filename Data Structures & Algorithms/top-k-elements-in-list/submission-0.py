class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}

        for i in nums:
            if i not in group:
                group[i] = 1
            else:
                group[i] += 1

        n = sorted(group.items(), key= lambda x: x[1], reverse=True)
        ans = []

        for num, freq in n[:k]:
            ans.append(num)
        
        return ans