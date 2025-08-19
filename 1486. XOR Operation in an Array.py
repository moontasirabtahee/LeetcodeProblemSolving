class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [start + 2 * i for i in range(n)]
        ans = 0
        for num in nums:
            ans ^= num

        return ans