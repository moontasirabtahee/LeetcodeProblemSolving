# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
#
# This solution does not gives us the tree structure just the value
#
# class Solution(object):
#     def isSameTree(self, p, q):
#         """
#         :type p: Optional[TreeNode]
#         :type q: Optional[TreeNode]
#         :rtype: bool
#         """
#
#         def dfs(root,ans):
#             if not root:
#                 return []
#
#
#             ans.append(root.val)
#             dfs(root.left,ans)
#             dfs(root.right,ans)
#
#             return ans
#         ansp = []
#         ansq = []
#         p = dfs(p,ansp)
#         q = dfs(q,ansq)
#
#         if p == q:
#             return True
#         else:
#             return False
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)

