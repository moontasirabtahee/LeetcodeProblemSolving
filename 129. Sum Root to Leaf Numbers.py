# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node,Cursum):
            if not node:
                return 0

            Cursum = Cursum*10 + node.val

            if not node.left and not node.right:
                return Cursum

            return dfs(node.left,Cursum)+dfs(node.right,Cursum)

        return dfs(root,Cursum=0)

