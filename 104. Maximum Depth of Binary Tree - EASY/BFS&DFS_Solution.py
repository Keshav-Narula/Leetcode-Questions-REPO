# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # DFS Recursive Solution
        #Time complexity is O(n) - traversing entire tree, all nodes
        #Space complexity is O(n) - height of the tree, worst case if not balanced
        
        # Base Case: Binary tree is empty, root is null, depth is 0
        if not root:
            return 0

        # Recursive case : traverses branches of trees, returns the depth of the longest subtree
        return 1 + (max(self.maxDepth(root.left), self.maxDepth(root.right)))

        # BFS non recursive solution, traverse level by level

        """
        #base case, tree is empty, depth is 0
        if not root:
            return 0

        #Intialize level counter and queue to hold nodes in tree as you traverse the tree levels and pop off nodes
        level = 0
        q = deque([root])

        while q:
            #take snapshot of the queue at that level
            for i in range(len(q)):
                node = q.popleft()
                #append all child nodes in next level to the queue
                if(node.left):
                    q.append(node.left)

                if(node.right):
                    q.append(node.right)
            #traversed through all nodes on that level, increase level counter
            level+= 1
    
        return level
        """
