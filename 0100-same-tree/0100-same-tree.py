# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # recursive solution
# class Solution(object):
#     def isSameTree(self, p, q):
#         if not p and not q:
#             return True 
#         if not p or not qp.val != q.val:
#             return False
#         return (self.isSameTree(p.left, q.left) and
#             self.isSameTree(p.right, q.right))

# # BFS(queue)
# from collections import deque

# class Solution(object):
#     def isSameTree(self, p, q):
#         queue = deque()
#         queue.append((p, q))

#         while queue:
#             node1, node2 = queue.popleft()
#             if not node1 and not node2:
#                 continue
#             if not node1 or not node2:
#                 return False
#             if node1.val != node2.val:
#                 return False
#             queue.append((node1.left, node2.left))
#             queue.append((node1.right, node2.right))
#         return True

# DFS(stack)
class Solution(object):
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        return True

