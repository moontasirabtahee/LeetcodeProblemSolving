class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        expected_sum = (len_nums * (len_nums + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum