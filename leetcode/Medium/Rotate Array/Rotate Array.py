class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #Solution 1 Time: O(n) Space: O(1)
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

        #Solution 2 Time: O(n) Space: O(1)
        # n = len(nums)
        # k %= n
        # nums.reverse()
        # nums[:k] = reversed(nums[:k])
        # nums[k:] = reversed(nums[k:])

        # Solution 3 Time: O(n*k) Space: O(1)
        # n = len(nums)
        # k %= n
        # while k > 0:
        #     nums.insert(0, nums.pop())
        #     k-=1

        # Solution 4 Time: O(n) Space: O(n)
        # n = len(nums)
        # k %= n
        # temp = [0]*n
        # for i in range(n):
        #     temp[i] = nums[(i + n - k) % n]
        #     # temp[(i + k) % n] = nums[i]
        # nums[:] = temp