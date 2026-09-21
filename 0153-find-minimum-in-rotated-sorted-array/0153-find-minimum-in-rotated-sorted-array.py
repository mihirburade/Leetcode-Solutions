class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            middle=(left+right)//2

            if nums[middle]>nums[right]:
                left=middle+1

            if nums[middle]<nums[right]:
                right=middle

            # if nums[left]==nums[right]:
            #     left+=1
            #     right+=1

            if  right==middle==left:
                return nums[middle]