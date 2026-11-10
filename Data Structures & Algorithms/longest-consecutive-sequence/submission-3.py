import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Simplest way is to sort it which would be O(nlogn) solution and no O(n). We need an O(n) solution.
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