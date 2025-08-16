class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        pr = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                pr += i[0]
            # 120 / 126 testcases passed
            else:
                break

        return pr



s = Solution()

strs = ["flower", "flow", "flight"]

s.longestCommonPrefix(strs)  # Output should be "fl"
