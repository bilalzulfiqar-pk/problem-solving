class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Time Complexity: O(n Log n)
        # Space Complexity: O(n)
        doubled_nums = [number ** 2 for number in nums]
        return sorted(doubled_nums)