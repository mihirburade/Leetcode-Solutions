class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        c_sum=0
        min_length=float('inf')

        for right in range(len(nums)):
            c_sum+=nums[right]

            while c_sum>=target:
                min_length=min(min_length,right-left+1)

                c_sum-=nums[left]
                left+=1
        if min_length==float('inf'):
            return 0

        return min_length