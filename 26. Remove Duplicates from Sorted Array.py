class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if nums == []:
    #         return 0
    #
    #     i = 0
    #     for j in range(1, len(nums)):
    #         if nums[i] != nums[j]:
    #             i += 1
    #             nums[i] = nums[j]
    #
    #     return i+1

    def removeDuplicates(self, nums):
        if nums == []:
            return 0
        dub  = sorted(set(nums))
        for i in range(len(dub)):
            nums[i] = dub[i]
        return len(dub)

