# Solution2
from typing import List 

# Solution3
# import heapq
# from typing import List

# Solution4
# from collections import Counter
# from typing import List

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # # Solution1
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        # result = []
        # for i in range(k):
        #     max_key = max(count, key=count.get)
        #     result.append(max_key)
        #     del count[max_key]
        # return result

        # Solution2
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(len(buckets) - 1, 0, -1): #뒤에서부터(높은 빈도부터) 순회
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result

        # # Solution3
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        # return heapq.nlargest(k, count.keys(), key=count.get)

        # # Solution4
        # count = Counter(nums)
        # return [num for num, freq in count.most_common(k)]