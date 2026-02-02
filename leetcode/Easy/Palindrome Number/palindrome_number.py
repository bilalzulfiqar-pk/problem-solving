class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xstring = str(x)
        return xstring == xstring[::-1]

        # rstring = xstring[::-1]

        # # for i,ch in enumerate(xstring):
        # for i in range(len(xstring)):
        #     if (xstring[i] != rstring[i]):
        #         return False
        # return True
