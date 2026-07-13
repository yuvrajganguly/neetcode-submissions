class Solution:
    def isPalindrome(self, s: str) -> bool:
        forw = []
        bckw = []
        for c in range(len(s)):
            if s[c].isalnum():
                forw.append(s[c].lower())
        for c in range(len(s)-1, -1, -1):
            if s[c].isalnum():
                bckw.append(s[c].lower())
        if forw == bckw:
            return True
        else:
            return False

        
            