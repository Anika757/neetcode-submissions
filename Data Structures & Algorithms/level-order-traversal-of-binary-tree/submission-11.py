# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue1 = deque([root])

        while queue1:
            levelvalues = []
            levelsize = len(queue1)
            for temproot in range(levelsize):
                node = queue1.popleft()
                levelvalues.append(node.val)

                if node.left:

                    queue1.append(node.left)
                if node.right:

                    queue1.append(node.right)
            result.append(levelvalues)

        return result
        