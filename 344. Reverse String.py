class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s

s = Solution()
print(s.reverseString(["h", "e", "l", "l", "o"]))  # Output should be ["o", "l", "l", "e", "h"]
