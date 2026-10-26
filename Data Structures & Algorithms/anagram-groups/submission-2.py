from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0: return [[""]]
        if len(strs) == 1: return [strs]
        return self.__naiive_solution(strs)

    def __naiive_solution(self, strs):
        hashmap = defaultdict(list)
        for word in strs:
            s_word = "".join(sorted(word))
            hashmap[s_word].append(word)
        
        return list(hashmap.values())