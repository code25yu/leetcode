# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# """
# :type root: Optional[TreeNode]
# :rtype: bool
# """

# DFS
# class Solution(object):
#     def isSymmetric(self, root):
#         def isMirror(t1, t2):
#             if not t1 and not t2:
#                 return True
#             if not t1 or not t2:
#                 return False
#             return (t1.val == t2.val and 
#                     isMirror(t1.left, t2.right) and
#                     isMirror(t1.right, t2.left))
#         return isMirror(root.left, root.right)
        
# BFS
class Solution(object):
    def isSymmetric(self, root):
        queue = deque([(root.left, root.right)])
        while queue:
            t1, t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        return True