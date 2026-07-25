class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        x=[]
        
        def back(opn,close):
            if len(x)==2*n:
                result.append("".join(x))
                return


            if opn<n:
                x.append("(")
                back(opn+1,close)
                x.pop()

            if close<opn:
                x.append(")")
                back(opn,close+1)
                x.pop()
        back(0,0)
        return result
