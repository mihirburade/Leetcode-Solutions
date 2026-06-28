class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0

        i = 1
        while i * i <= x:
            i += 1

        return i - 1