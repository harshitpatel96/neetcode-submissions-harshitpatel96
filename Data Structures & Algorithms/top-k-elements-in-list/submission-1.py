import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1 2 2 3 3 3 k = 2
        {1: 1, 2: 2, 3: 3}
        return 2 and 3



        """
            
        counts = collections.defaultdict(int)
        for num in nums: 
            counts[num] += 1
        
        q = [(counts[key], key) for key in counts.keys()]

        heapq.heapify_max(q)
        
        return [heapq.heappop_max(q)[1] for i in range(k)]
