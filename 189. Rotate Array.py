class Solution(object):



# 28 / 39 testcases passed
#
    # def rotate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     ro = nums[-k:] + nums[:-k]
    #     nums[:] = ro"""

# Time Limit Exceeded
# 35 / 39 testcases passed
#
#     def rotate(self, nums, k):
#         for i in range(k):
#             ro = nums[len(nums)-1:]+nums[:-1]
#             nums[:] = ro

# Time Limit Exceeded
# 35 / 39 testcases passed
#
#     def rotate(self, nums, k):
#         for i in range(k%len(nums)):
#             ro = nums[len(nums)-1:]+nums[:-1]
#             nums[:] = ro


    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
s.rotate(nums, 3)
print(nums)  # Output should be [5, 6, 7, 1, 2, 3, 4]