class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self._division_method(nums)

    def _prefix_suffix_method_self_implemented(self, nums):
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

    def _division_method(self, nums):
        zero_cnt = 0
        zero_indices = set()
        prod = 1
        n = len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                zero_cnt += 1
                zero_indices.add(i)
            else:
                prod *= num
        if zero_cnt > 1: return [0]*n
        if zero_cnt == 1: return [0 if i not in zero_indices else prod for i in range(n)]
        return [prod//num for num in nums]
