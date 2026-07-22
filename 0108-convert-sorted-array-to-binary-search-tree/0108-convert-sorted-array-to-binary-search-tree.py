# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def tree(nums):

            if not nums:
                return None
            mid=len(nums)//2
            left=nums[:mid]
            right=nums[mid+1:]

            root=TreeNode(nums[mid])
            root.left=tree(left)
            root.right=tree(right)

            return root

        return tree(nums)

