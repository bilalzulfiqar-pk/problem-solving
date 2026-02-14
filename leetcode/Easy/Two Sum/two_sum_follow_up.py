class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Sol #1 O(n)
        seen = {}
        for i in range(len(nums)):
            y = target - nums[i]

            if y in seen:
                return [seen[y],i]

            seen[nums[i]] = i


        # Sol #2 O(n^2)
        # for i in range(len(nums)):
        #     y = target - nums[i]
        #     if y in nums:
        #         y_index = nums.index(y)
        #         if y_index != i:
        #             return [i,y_index]

        # Sol #3 O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i,j]

        # Sol #4 O(n^2)
        # from itertools import combinations

        # for i, j in combinations(range(len(nums)), 2):
        #     if nums[i] + nums[j] == target:
        #         return [i, j]