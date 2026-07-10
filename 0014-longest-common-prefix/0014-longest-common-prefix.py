class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0]
        n = len(first)
        for i in range(n):
            for other in strs[1:]:
                if i + 1 > len(other) or other[i] != first[i]:
                    return first[:i]
        return first