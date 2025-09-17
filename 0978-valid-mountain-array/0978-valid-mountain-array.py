class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # # 1.State-Tracking Approach
        # if len(arr) < 3:
        #     return False
        # up = True
        # for i in range(len(arr) - 1):
        #     if arr[i] == arr[i+1]:
        #         return False
        #     if up == False and arr[i] < arr[i+1]:
        #         return False
        #     if up == True and arr[i] > arr[i+1]:
        #         if i != 0:
        #             up = False
        #         else:
        #             return False
        # if up == False:
        #     return True
        # return False
        
        # 2. Two-Phase Linear Scan
        n = len(arr)
        if n < 3:
            return False
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1
