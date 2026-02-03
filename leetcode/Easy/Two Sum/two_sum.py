class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i,j]

        # from itertools import combinations

        # for i, j in combinations(range(len(nums)), 2):
        #     if nums[i] + nums[j] == target:
        #         return [i, j]