class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        1 <= strs.length <= 200
        """

        prefix = ""
        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            for string in strs:
                if string[i] != shortest[i]:
                    return prefix
            prefix += shortest[i]

        return prefix
