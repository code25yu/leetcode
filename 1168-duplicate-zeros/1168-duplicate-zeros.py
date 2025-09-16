class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

        # # 방법1
        # length = len(arr)
        # flag = 0
        # for i in range(length - 1):
        #     if arr[i] == 0:
        #         if flag == 0:
        #             for j in range(length - 1, i, -1):
        #                 arr[j] = arr[j - 1]
        #                 flag = 1
        #         else:
        #             flag = 0
        # return arr
        
        # # 방법2
        # n = len(arr)
        # i = 0
        # while (i < n):
        #     if arr[i] == 0:
        #         arr[i+1:n] = arr[i:n-1]
        #         i+=1
        #     i+=1
        # return arr 
        
        # 방법3
        n = len(arr)
        zeros = arr.count(0)
        i = n - 1
        
        while zeros > 0:
            if i + zeros < n:  
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
            i-=1
        return arr 
        
        
        
        
        
        
        