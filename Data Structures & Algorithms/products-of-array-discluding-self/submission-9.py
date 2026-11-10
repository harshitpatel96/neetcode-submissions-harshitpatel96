class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self._single_pass_forward_and_backward_self_implemented(nums)

    def _prefix_suffix_method_self_implemented_suboptimal(self, nums):
        """
        [1, 2, 3, 6] original array
                
        [1, 2, 6, 36] product of 0 to i

        [36, 36, 18, 6] product of i to n

        ans = [1*36, 18, 36, 18]
        the difference between this and solutions suboptimal prefix method is 
        in solution method:
            prefix[i] = nums[i-1]*prefix[i-1] => product of everything to the left of it
            suffix[i] = nums[i+1]*prefix[i+1] => product of everything to the right of it
        in my method:
            prefix[i] = nums[i]*prefix[i-1] => product of everything to the left and the number at i itself
            suffix[i] = nums[i]*prefix[i+1] => product of everything to the right and the number at i itself
        
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

    def _prefix_suffix_method_solution_suboptimal(self, nums):
        n = len(nums)
        res = [0]*n
        pref = [0]*n
        suff = [0]*n

        pref[0] = suff[n-1] = 1 # first of pref is 1 and last of suff is 1 because nothing exist as prefix of position 0 and suffix of position n-1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res

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

    def _prefix_suffix_more_efficiently_written_from_solution(self, nums):
        n = len(nums)
        prefix = 1
        res = []
        for i in range(n):
            res.append(prefix)
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

    def _single_pass_forward_and_backward_self_implemented(self, nums):
        n = len(nums)
        prefix = 1
        suffix = 1
        res = [0]*n
        i = 0
        j = n-1
        while i < n or j > -1:
            if i < j:
                res[i] = prefix
                res[j] = suffix
            elif i == j:
                res[i] = prefix * suffix
            else:
                res[i] *= prefix                
                res[j] *= suffix
            prefix *= nums[i]
            suffix *= nums[j]
            i += 1
            j -= 1
            
        return res
