class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # # O(N^2)
        # for i in range(len(arr)):
        #     for j in range(i + 1, len(arr)):
        #         # print (i, j)
        #         if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2:
        #             return True
        # return False
        
        # O(N): Hashset
        seen = set()
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False