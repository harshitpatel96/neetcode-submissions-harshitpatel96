class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [ 1 7 2 5 4 7 3 6 ]
          l             r


          l  r  maxArea
          0  6    7*1
          1  6    6*6


        """
        n = len(heights)

        l = 0
        r = n-1
        max_area = 0
        while l < r:
            max_area = max(max_area, (r - l)*min(heights[r], heights[l]))
            if heights[r] < heights[l]: r -= 1
            else: l += 1
        
        return max_area




