class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        n = len(s)
        j = n-1
        while i < j:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum() : j -= 1
            if not s[i].lower() == s[j].lower(): return False
            i += 1
            j -= 1
        return True