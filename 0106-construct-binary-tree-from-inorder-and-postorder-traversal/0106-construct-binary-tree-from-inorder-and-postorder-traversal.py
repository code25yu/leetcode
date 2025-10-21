# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # 중복 원소가 없으므로 value -> index 매핑을 미리 만들어 둔다 (O(1)접근이 가능하도록)
        inorder_idx = {value: idx for idx, value in enumerate(inorder)}

        # postorder를 뒤에서부터 꺼내 쓰기 위해 index 포인터 사용
        self.post_idx = len(postorder) - 1
        
        # 재귀 함수 
        def helper(left, right):
            # 서브트리 구간이 비었으면 반환
            if left > right:
                return None
            # postorder의 마지막 값 = 현재 루트
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            # inorder에서 루트의 위치 찾기
            index = inorder_idx[root_val]
            # 순서주의 : postorder는 root가 뒤이므로, 오른쪽 서브트리 먼저 구성해야 함
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)
            