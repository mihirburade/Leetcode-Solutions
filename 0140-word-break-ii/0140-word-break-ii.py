class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordset=set(wordDict)

        def recursion(start):
            result=[]
           
           
            if start==len(s):
                return [""]
           
           
            for end in range(start+1,len(s)+1):
                word=s[start:end]

                if word in wordset:
                    sentenses=recursion(end)

                    for sentense in sentenses:
                        if sentense:
                            result.append(word+" "+sentense)

                        else:
                            result.append(word)

            return result
        return recursion(0)


            
                            


        