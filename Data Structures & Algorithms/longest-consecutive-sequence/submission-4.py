import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self._hashset_solution(nums)
    def _hashset_solution(self, nums):
        numSet = set(nums)
        maxlen = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                maxlen = max(length, maxlen)
        
        return maxlen

    def hashmap_solution(self, nums):
        return None

    def _heapified_elegant(self, nums):
        return None

    def _heapified_solution_self_implemented(self, nums):
        """
        - Simplest way is to sort it which would be O(nlogn) solution and no O(n). We need an O(n) solution.
        - another approach is heap which would be O(n) time and O(n) space

        """
        n = len(nums)
        if n == 0 or n == 1: return n
        heapq.heapify(nums)
        # longest sequence:
        length = 1
        seen = set()
        prev = heapq.heappop(nums)
        seen.add(prev)
        maxlen = 1
        while nums:
            current = heapq.heappop(nums)
            if current not in seen:
                if current == prev + 1:
                    length += 1
                    maxlen = max(maxlen, length) 
                else:
                    length = 1
                
                seen.add(current)
                prev = current
                        
        return maxlen