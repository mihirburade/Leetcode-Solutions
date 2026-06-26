class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # m="mihir burade"
        x=s.split()
        return len(x[-1])