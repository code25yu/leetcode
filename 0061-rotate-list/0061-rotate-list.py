# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

#         def rotate(head):
#             last = prev = head
#             while last and last.next:
#                 prev = last
#                 last = last.next
#             last.next = head
#             prev.next = None
#             return last
        
#         def size(head):
#             n = 0
#             while head:
#                 head = head.next
#                 n+=1
#             return n

#         new_head = head
#         if head:
#             n = size(head)
#             for i in range(k if not n else k % n):
#                 new_head = rotate(new_head)
  
#         return new_head

        if not head or not head.next or k == 0:
            return head
        
        # 1. 길이 계산 및 tail 찾기
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # 2. k를 n으로 모듈로   
        k = k % n 
        if k == 0:
            return head
        
        # 3. 원형 연결
        tail.next = head
        
        # 4. 새로운 tail 위치 찾기
        steps_to_new_tail = n - k
        new_tail = tail
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
            
        return new_head
        