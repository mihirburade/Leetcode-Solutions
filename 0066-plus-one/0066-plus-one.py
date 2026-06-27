class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=""
        for i in digits:
            a+=str(i)
        
        x=int(a)+1
        ans=[]
        for i in str(x):
            ans.append(int(i))
        return ans