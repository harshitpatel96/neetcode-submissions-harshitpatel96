from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0: return [[""]]
        if len(strs) == 1: return [strs]
        return self.__better_solution(strs)

    def __naiive_solution(self, strs):
        hashmap = defaultdict(list) # m space
        for word in strs: # m times
            s_word = "".join(sorted(word)) # (nlogn) where n is longest word length
            hashmap[s_word].append(word)
        
        return list(hashmap.values())

    def __better_solution(self, strs):
        results = defaultdict(list)
        for word in strs:
            key = [0]*26 # for each of the 26 letters of alphabet (O(1) space)
            for char in word:
                key[ord(char) - ord('a')] += 1 # ord(char) - ord("a") gives us an index on the array corresponding to character. the ord function returns ascii value of the char.
            results[tuple(key)].append(word)

        return list(results.values())