class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        if length of array is exactly 3 then we simply have to check total sum of array to make decision.

        O(n^3) algorithm would consider every triplet. and would need to keep track of known triplets as a hashset to ensure it doesn't repeat them

        does sorting help? how?

        if we make a hashmap out of this with number as key and occurence as value

        [-4 -1 -1 0 1 2]
          i    j      k

          -4 -1 + 2 => -3
          -4 -1 + 2 => -3
          -4 + 0 + 2 => -2
          -4 + 1 + 2 => -1

          -1 -1 + 2 => 0 [[-1 -1 2]]
          
          -1 +0 +2 => 1
          -1 + 0 +1 => 0 [[-1 -1 2], [-1 0 1]]

`
        """
        return self.n_sqr_soln(nums)
    
    def possibilities(self, a, b, c):
        return [f"{a}{b}{c}", f"{a}{c}{b}", f"{b}{a}{c}", f"{b}{c}{a}", f"{c}{a}{b}", f"{c}{b}{a}"]

    def naiive_solution(self, nums):
        
        n = len(nums)
        if n == 3:
            if sum(nums) == 0:
                return [nums]
            return []
        
        res = []
        seen = set()
        for i in range(n):
            a = nums[i]
            for j in range(i+1, n):
                b = nums[j]
                for k in range(j+1, n):
                    c = nums[k]
                    if f"{a}{b}{c}" not in seen and sum([a,b,c]) == 0:
                        seen.update(self.possibilities(a,b,c))
                        res.append([a,b,c])

        return res

    def n_sqr_soln(self, nums):
        n = len(nums)
        if n == 3:
            return [nums] if sum(nums) == 0 else []

        res = []
        seen = set()
        snums = sorted(nums)

        for i in range(n):
            j = i+1
            k = n-1
            while j < k:
                s = snums[i] + snums[j] + snums[k]
                if s == 0:
                    if(snums[i], snums[j], snums[k]) not in seen: res.append([snums[i], snums[j], snums[k]])
                    seen.add((snums[i], snums[j], snums[k]))
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                elif s < 0:
                    j += 1

        
        return res
