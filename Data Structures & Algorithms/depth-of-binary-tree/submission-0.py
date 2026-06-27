# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        level = 0
        if root:
            queue.appendleft(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.pop()
                if curr.left:
                    queue.appendleft(curr.left)
                if curr.right:
                    queue.appendleft(curr.right)

            level += 1

        return level