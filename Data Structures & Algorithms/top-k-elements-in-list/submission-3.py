class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        bucket = []
        for _ in range(len(nums)+1):
            bucket.append([])
    
        for n, count in dic.items():
            bucket[count].append(n)
        
        ans = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

