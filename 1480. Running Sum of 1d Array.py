class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        array = []

        for i in range(len(nums)):
            sum += nums[i]
            array.append(sum)

        return array