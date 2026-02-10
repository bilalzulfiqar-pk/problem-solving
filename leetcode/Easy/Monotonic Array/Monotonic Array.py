class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        inc = dec = True

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                inc = False
            if nums[i] < nums[i+1]:
                dec = False

        return inc or dec

        # return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or \
        #        all(nums[i] >= nums[i+1] for i in range(len(nums)-1))