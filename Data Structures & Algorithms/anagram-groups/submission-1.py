class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total_strs = len(strs)
        """
        strs = ["act","pots","tops","cat","stop","hat"]
        output = [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        strs = ["act", "cat"]
        output = [["act", "cat"]]

        """

        return self._naiive_solution(strs)
    
    def _naiive_solution(self, strs):
        
        hashmap = {}
        for w in strs:
            k = "".join(sorted(w))
            if k in hashmap:
                hashmap[k].append(w)
            else:
                hashmap[k] = [w]

        return list(hashmap.values())

    def _second_soln(self, strs):
        hashmap