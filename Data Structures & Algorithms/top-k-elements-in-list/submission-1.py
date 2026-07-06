class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}

        for i in nums:
            if i not in group:
                group[i] = 1
            else:
                group[i] += 1

        sorted_group = sorted(group.items(), key= lambda x: x[1], reverse=True)
        ans = []

        for tuple_ele_1, tuple_ele_2 in sorted_group[:k]:
            ans.append(tuple_ele_1)
        
        return ans