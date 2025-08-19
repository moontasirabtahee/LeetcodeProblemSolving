# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        pre = []
        def preorder(root):
            if not root:
                return
            else:
                pre.append(root.val)
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        return pre
#iterative

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans