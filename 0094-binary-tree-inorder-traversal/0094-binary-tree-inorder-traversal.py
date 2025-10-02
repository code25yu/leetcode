# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. recursive solution
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
    
# # 2. iterative solution
# class Solution(object):
#     def inorderTraversal(self, root):
#         res = []
#         stack = []
#         now = root

#         while now or stack:
#             while now:
#                 stack.append(now)
#                 now = now.left
#             now = stack.pop()
#             res.append(now.val)
#             now = now.right
#         return res