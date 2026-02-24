# Time:O(n × n!) Space: O(n)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        permutations = []

        def backtrack(i):

            if i == len(nums):
                permutations.append(nums[:])
                return

            for j in range(i,len(nums)):
                #Swap
                nums[i], nums[j] = nums[j], nums[i]

                backtrack(i+1)

                #Undo Swap
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return permutations

# Time:O(n × n!) Space: O(n × n!)
# class Solution:
#     def permute(self, nums):
#         result = []
#         used = [False] * len(nums)

#         def backtrack(path):
#             # Base case
#             if len(path) == len(nums):
#                 result.append(path[:])  # copy
#                 return

#             for i in range(len(nums)):
#                 if used[i]:
#                     continue

#                 # Choose
#                 used[i] = True
#                 path.append(nums[i])

#                 # Explore
#                 backtrack(path)

#                 # Undo (Backtrack)
#                 path.pop()
#                 used[i] = False

#         backtrack([])
#         return result

# TEST CASES
print(Solution().permute([1,2,3]))
print(Solution().permute([0,1]))
print(Solution().permute([1]))