"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']: 
        if not node:
            return None

        queue = deque()
        queue.append(node)
        oldtoNew = {}
        oldtoNew[node] = Node(node.val)

        while queue:
            curNode = queue.popleft()
            for n in curNode.neighbors:
                if n not in oldtoNew:
                    oldtoNew[n] = Node(n.val)
                    queue.append(n)
                oldtoNew[curNode].neighbors.append(oldtoNew[n])
                        
        return oldtoNew[node]
        
                        

                        
