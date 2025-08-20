class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        print((s+s)[1:-1])
        if s in (s+s)[1:-1]:
            return True
        return False

s = Solution()
# Example usage:
print(s.repeatedSubstringPattern("abab"))  # Output: True
print(s.repeatedSubstringPattern("aba"))   # Output: False
print(s.repeatedSubstringPattern("abcabcabcabc"))  # Output: True
print(s.repeatedSubstringPattern("a"))     # Output: False
