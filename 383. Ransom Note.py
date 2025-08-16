from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = Counter(ransomNote)
        m = Counter(magazine)

        print(r)
        print(m)
        for i in r:
            print(r[i],m[i])
            if r[i]>m[i]:
                return False
        return True

s = Solution()
ransomNote = "a"
magazine = "b"
  # Output should be
# False
print(s.canConstruct(ransomNote, magazine))  # Output should be False
ransomNote = "aa"
magazine = "ab"
print(s.canConstruct(ransomNote, magazine))  # Output should be
# False
ransomNote = "aa"
magazine = "aab"
print(s.canConstruct(ransomNote, magazine))  # Output should be
