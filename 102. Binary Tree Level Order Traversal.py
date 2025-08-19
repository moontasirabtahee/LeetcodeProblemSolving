from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans = []
        que = deque([root])

        if not root:
            return ans

        while que:
            level = []

            for i in range(len(que)):
                cur = que.popleft()
                level.append(cur.val)

                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            ans.append(level)

        return ans
