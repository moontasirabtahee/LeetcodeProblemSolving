class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        fullList = list(range(1, len(nums) + 1))
        miss = list(set(fullList) - set(nums))
        return miss