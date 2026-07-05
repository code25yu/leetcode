class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = { 'I': 1, 
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }
        total = 0
        n = len(s)
        for i in range(n):
            current = dic[s[i]]
            if i + 1 < n and current < dic[s[i + 1]]:
                total -= current
            else:
                total += current
        return total