# from collections import defaultdict 

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Soultion1
        groups = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())

        # Soultion2
        # groups = defaultdict(list)
        # for s in strs:
        #     key = ''.join(sorted(s))
        #     groups[key].append(s)
        # return list(groups.values())

