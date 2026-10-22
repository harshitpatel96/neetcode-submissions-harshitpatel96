from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        i = 0
        dict_S = defaultdict(int)
        dict_T = defaultdict(int)
        while i < len(s):
            dict_S[s[i]] += 1
            dict_T[t[i]] += 1
            i += 1
        
        for key in dict_S.keys():
            if not (dict_S[key] and dict_T[key]) or (dict_S[key] != dict_T[key]):
                return False
            
        return True