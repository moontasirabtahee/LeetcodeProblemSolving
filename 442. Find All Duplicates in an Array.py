class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for i in nums:
            ind = abs(i) - 1

            if nums[ind] < 0:
                r.append(abs(i))
            else:
                nums[ind] = -nums[ind]
        return r