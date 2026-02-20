class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n) Space:O(1)
        if n <= 1:
            return n
        
        prev1 = 0
        prev2 = 1

        for i in range(2, n+1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        
        return prev2

        # Recursion method
        # Time: O(2^n) Space: O(n)
        # if n<=1:
        #     return n
        # else:
        #     return self.fib(n-1) + self.fib(n-2)

# Top-Down (Memoization) Time: O(n) Space: O(n)
# class Solution(object):
#     def fib(self, n, ht=None):

#         if ht is None:
#             ht = {0: 0, 1: 1} 

#         if n in ht:
#             return ht[n]
        
#         ht[n] = self.fib(n - 1, ht) + self.fib(n - 2, ht)
#         return ht[n]

# Bottom-Up (Tabulation) Time: O(n) Space: O(n)
# class Solution(object):
#     def fib(self, n):
#         if n <= 1:
#             return n
        
#         # Create the table (DP array)
#         dp = [0] * (n + 1)
#         dp[1] = 1
        
#         # Fill the table iteratively
#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
            
#         return dp[n]