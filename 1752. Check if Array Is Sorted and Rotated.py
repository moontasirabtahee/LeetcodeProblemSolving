class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0

        n = len(nums)  # Get the size of the list

        # Iterate through the list
        for i in range(n):
            # Check if the current element is greater than the
            # next element
            if nums[i] > nums[(i + 1) % n]:
                # Increment count if the sequence is out of
                # order
                count += 1

        # Return true if there is at most one point where the
        # sequence is out of order
        return count <= 1