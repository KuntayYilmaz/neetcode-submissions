# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        result = 0
        isFound = False
        def dfs(root):
            nonlocal isFound,result,count
            if not root or isFound:
                return

            dfs(root.left)
            if isFound:
                return

            if count == 1:
                result = root.val
                isFound = True
                return    
            count -= 1
            
            dfs(root.right)

        dfs(root)
        return result
        


