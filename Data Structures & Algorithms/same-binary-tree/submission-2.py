# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.same = True
        def dfs(root1,root2):
            if (not root1 and not root2) or not self.same:
                return None
            if not root1 or not root2:
                self.same = False
            else:
                if root1.val != root2.val:
                    self.same = False
                dfs(root1.left,root2.left)
                dfs(root1.right,root2.right)

        dfs(p,q)

        return self.same
                

            
            

    