# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # dfs
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return (self.hasPathSum(root.left, targetSum - root.val) or 
                self.hasPathSum(root.right, targetSum - root.val))

#         # bfs
#         if not root:
#             return False
        
#         queue = deque([(root, root.val)])
#         while queue:
#             node, curr_sum = queue.popleft()
            
#             if not node.left and not node.right and curr_sum == targetSum:
#                 return True
            
#             if node.left:
#                 queue.append((node.left, curr_sum + node.left.val))
#             if node.right:
#                 queue.append((node.right, curr_sum + node.right.val))
        
#         return False 