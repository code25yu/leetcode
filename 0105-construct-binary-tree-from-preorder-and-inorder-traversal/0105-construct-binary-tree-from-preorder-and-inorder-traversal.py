# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_idx = { value : idx for idx, value in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(left, right):
            if left > right:
                return None
            # preorder의 처음값 = 현재루트
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            # inorder에서 루트의 위치 찾기
            index = inorder_idx[root_val]
            # 루트의 왼쪽트리, 오른쪽트리 구성하기 
            # Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
            # Output: [3,9,20,null,null,15,7]
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)
            return root 
        return helper(0, len(preorder) - 1)
            