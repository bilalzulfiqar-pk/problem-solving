class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time: O(n)
        left = 0
        right = len(height)-1
        max_area = 0

        while left<right:
            w = right - left
            h = min(height[left],height[right])
            a = w * h
            if a > max_area:
                max_area = a
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return max_area
        
        # # Time: O(n^2)
        # n = len(height)
        # max_area = 0
        
        # for i in range(n):
        #     for j in range(i+1,n):
        #         w = j-i
        #         h = min(height[i],height[j])
        #         a = w*h
        #         if a > max_area:
        #             max_area = a
        # return max_area
