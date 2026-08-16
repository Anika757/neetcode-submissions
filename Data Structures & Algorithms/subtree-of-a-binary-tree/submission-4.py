# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None:
            return False
        if q == None:
            return False
        return (p.val == q.val and self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left))  
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        if root == None:
            return False
        if subRoot == None:
            return True
        if self.isSameTree(root, subRoot):
            return True
        foundleft = self.isSubtree(root.left, subRoot)
        foundright = self.isSubtree(root.right,subRoot)
        return foundleft or foundright
        