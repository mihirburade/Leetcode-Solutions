class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def main():
            left=0
            right=len(height)-1
            maximum=0

            while left < right:
                width=right-left
                if height[left]>height[right]:
                    area=height[right]*width
                    right-=1

                else:
                    area=height[left]*width
                    left+=1

                maximum=max(maximum,area)
            return maximum

        return main()
        
