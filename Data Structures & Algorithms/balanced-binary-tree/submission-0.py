# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):

            if root is None:
                return -1
            
            lheight = dfs(root.left)
            lright  = dfs(root.right)

            if abs(lheight - lright) == 2:
                self.balanced = False

            return max(lheight,lright) + 1
        
        dfs(root)
        return self.balanced
