class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        left = 0
        right = len(nums)-1
        doubled_nums = [0]*len(nums)

        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                doubled_nums[i] = nums[left]**2
                left += 1
            else:
                doubled_nums[i] = nums[right]**2
                right -= 1
        return doubled_nums