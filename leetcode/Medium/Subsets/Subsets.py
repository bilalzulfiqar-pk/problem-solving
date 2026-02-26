class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Time: O(n * 2^n) Space: O(n * 2^n) (all solutions)

        # Sol: 1
        result = []

        def backtrack(start, path):
            result.append(path[:])  
            
            for i in range(start, len(nums)):
                path.append(nums[i])        
                backtrack(i + 1, path)     
                path.pop()                 
        
        backtrack(0, [])
        return result

        # # Sol: 2
        # output = []
        # def helper (nums, i, subset):
        #     if i == len(nums):
        #         output.append(subset[:])
        #         return
            
        #     helper(nums, i+1, subset)

        #     subset.append(nums[i])

        #     helper(nums, i+1, subset)

        #     subset.pop()
        # helper(nums, 0, [])
        # return output

        # # Sol: 3 (Iterative)
        # result = [[]]
        
        # for num in nums:
        #     new_subsets = []
        #     for subset in result:
        #         new_subsets.append(subset + [num])
        #     result.extend(new_subsets)
        
        # return result

# TEST CASES
print(Solution().subsets([1,2,3]))
print(Solution().subsets([0]))
print(Solution().subsets([1,5,8,9]))