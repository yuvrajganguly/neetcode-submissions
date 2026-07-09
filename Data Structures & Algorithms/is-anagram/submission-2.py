class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False

        anagram = {}

        for st in s:
            if st in anagram:
                anagram[st] += 1
            else: 
                anagram[st] = 1
        
        for st in t:
            if st in anagram:
                anagram[st] -= 1
            else:
                return False
        
        for c in anagram.values():
            if c != 0:
                return False
            
        return True