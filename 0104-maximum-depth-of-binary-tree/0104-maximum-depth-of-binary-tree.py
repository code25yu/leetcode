# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # BFS
# class Solution(object):
#     def maxDepth(self, root):
#         if not root:
#             return 0
#         queue = deque([root])
#         depth = 0
#         while queue:
#             level_size = len(queue)
#             for idx in range(level_size):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right: 
#                     queue.append(node.right)
#             depth += 1
#         return depth

# DFS
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1