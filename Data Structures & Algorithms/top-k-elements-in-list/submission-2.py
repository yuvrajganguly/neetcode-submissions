class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        
        d = sorted(dic.items(), key = lambda x: x[1], reverse=True)
        ans = []
        for x in d[:k]:
            ans.append(x[0])
        return ans

