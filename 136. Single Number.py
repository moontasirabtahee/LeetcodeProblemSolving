class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        miss = 0
        for i in nums:
            miss ^= i
        return miss