class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        2 3 4 5 6 10 11 -> T = 11
           i       j

        o(nlogn)
        o(n)
        """
        # first solution incorrect, I sorted the list but that changes the indices, so its incorrect
        # nums.sort()
        # i,j = [0,len(nums)-1]
        # while i < j:
        #     s = nums[i] + nums[j]
        #     if s == target: return [i,j]
        #     if s < target:
        #         i += 1
        #     else:
        #         j -= 1

        """

        3, 2, 3
        3, 4, 3

        {
            3: 0,
            4: 1,
            3: 3,
        },

        3, 4, 5, 6 -> T = 7
        {
            4: 0,
            3: 1
        }
        """
        sum_dict = {}
        for i, num in enumerate(nums):
            if num in sum_dict:
                return [sum_dict[num], i]
            sum_dict[target-num] = i

        