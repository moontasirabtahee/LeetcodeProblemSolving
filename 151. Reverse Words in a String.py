class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = s.strip()
        print(p)
        p = s.strip().split(" ")
        p[:] = p[::-1]
        p = [word for word in p if word]
        return " ".join(p)



s = Solution()
print(s.reverseWords("the sky is blue"))
# Output should be "blue is sky the"
print(s.reverseWords("  hello world  "))
# Output should be "world hello"
print(s.reverseWords("a good   example"))
