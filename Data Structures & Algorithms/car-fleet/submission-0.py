class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        time = []
        ans = 0
        for i in range(len(position)):
            dic[position[i]] = speed[i]
        d = sorted(dic.items(), reverse = True)
        for pos, spd in d:
            curr_time = (target - pos)/spd
            if not time or curr_time > time[-1]:
                ans += 1
                time.append(curr_time)
        return ans

