# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        wholeTreeGone = False
        def dfs(root,target,prev):
            nonlocal wholeTreeGone
            if not root:
                return
            dfs(root.left,target,root)
            dfs(root.right,target,root)

            if not root.left and not root.right and target == root.val:
                if prev == None:
                    wholeTreeGone = True
                elif prev.left == root:
                    prev.left = None
                else:
                    prev.right = None
        
        dfs(root,target,None)
        if wholeTreeGone:
            return None
        return root