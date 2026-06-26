class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        expectedNums=[]

        for i in range(len(nums)):
            if nums[i]!=val:
                expectedNums.append(nums[i])

            else:
                pass

        for i in range(len(expectedNums)):
            nums[i]=expectedNums[i]
        
        return len(expectedNums)