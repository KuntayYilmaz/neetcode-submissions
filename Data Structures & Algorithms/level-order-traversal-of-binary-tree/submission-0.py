# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result = []
        if root:
            q.append(root)

        while q:
            inter_result = []
            n_q = len(q)
            for _ in range(n_q):
                node = q.popleft()
                inter_result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
            result.append(inter_result)

        return result