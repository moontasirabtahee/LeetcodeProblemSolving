from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        print(count)
        if not s:
            return -1

        for i , char in enumerate(s):
            if count[char] == 1:
                return i
        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))  # Output should be 0
print(s.firstUniqChar("loveleetcode"))  # Output should be 2
print(s.firstUniqChar("aabb"))  # Output should be -1
