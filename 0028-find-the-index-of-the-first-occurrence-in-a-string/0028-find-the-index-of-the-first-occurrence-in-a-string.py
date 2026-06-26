class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i=0
        j=len(needle)

        while j<=len(haystack):
            common=haystack[i:j]
            if common == needle:
                return i
            i+=1
            j+=1

        return -1
        