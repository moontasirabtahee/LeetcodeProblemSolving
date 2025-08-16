class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1])

s = Solution()
print(s.lengthOfLastWord("Hello World"))  # Output should be 5
s.lengthOfLastWord("   fly me   to   the moon  ")  # Output should be 4
s.lengthOfLastWord("luffy is still joyboy")  # Output should be 6