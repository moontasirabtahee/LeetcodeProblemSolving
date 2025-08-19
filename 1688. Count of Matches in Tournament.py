class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        Tmatch = 0
        while n != 1:
            if n%2 == 0:
                Tmatch += n/2
                n = n/2
            else:
                Tmatch += n//2
                n = ((n-1)/2) + 1

        return Tmatch