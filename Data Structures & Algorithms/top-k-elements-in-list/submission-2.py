import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1 2 2 3 3 3 k = 2
        {1: 1, 2: 2, 3: 3}
        return 2 and 3
        """

        return self._min_heap(nums, k)
            
    def _max_heap(self, nums, k):

        ### this is less effecient than min heap as we will be required to store all elements into the q and then pop out k elements whereas in min heap we can always keep the length of heap equal to K and then we just return those k element. The time complexity stays same.
        counts = collections.defaultdict(int)
        for num in nums: 
            counts[num] += 1
        
        q = [(counts[key], key) for key in counts.keys()]

        heapq.heapify_max(q)
        
        return [heapq.heappop_max(q)[1] for i in range(k)]

    def _min_heap(self, nums, k):
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1

        heap = []
        for key in counts.keys():
            heapq.heappush(heap, (counts[key], key))
            if len(heap) > k: # here if length becomes more than K we pop smallest element
                heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for i in range(k)]