class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        for i in range(len(s), 0 ,-1):
            if i == len(s):
                total += numbers[s[i-1]]
            else:
                if numbers[s[i-1]] < numbers[s[i]]:
                    total -= numbers[s[i-1]]
                else:
                    total += numbers[s[i-1]]

        return total


s = Solution()
# Example usage:
print(s.romanToInt("III"))    # Output: 3
print(s.romanToInt("LVIII"))     # Output: 58
