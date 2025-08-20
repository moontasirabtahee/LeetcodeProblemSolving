class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        letter, digit = coordinates[0], int(coordinates[1])
        print(letter, digit)
        if letter in {'a', 'c', 'e', 'g'} and digit % 2 != 0:
            return False
        elif letter in {'b', 'd', 'f', 'h'} and digit % 2 == 0:
            return False
        else:
            return True

s = Solution()
# Example usage:
print(s.squareIsWhite("a1"))  # Output: False
print(s.squareIsWhite("h3"))  # Output: True
print(s.squareIsWhite("c7"))  # Output: False