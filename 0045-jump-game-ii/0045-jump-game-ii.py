class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump=0
        farthest=0
        current_end=0

        for i in range(len(nums)-1):
            farthest=max(farthest,nums[i]+i)

            if i==current_end:
                jump+=1
                current_end=farthest

        return jump