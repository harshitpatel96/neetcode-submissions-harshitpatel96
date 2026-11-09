class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        [1, 2, 3, 6] original array
                
        [1, 2, 6, 36] product of 0 to i

        [36, 36, 18, 6] product of i to n

        ans = [1*36, 18, 36, 18]
        """
        i = 0
        length = len(nums)

        fp = [1]*length
        while i < length:
            fp[i] = nums[i] if i == 0 else fp[i-1]*nums[i]
            i+=1
        
        j = length - 1
        bp = [1]*length
        while j >= 0:
            bp[j] = nums[j] if j == length - 1 else bp[j+1]*nums[j]
            j-=1
        
        ans = []
        for i in range(length):
            if i == 0: ans.append(bp[i+1])
            elif i == length-1: ans.append(fp[i-1])
            else: ans.append(fp[i-1]*bp[i+1])
        
        return ans