class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if dividend==-2**31 and divisor ==-1:
            return 2147483647
        quotient=0

        negative=(dividend<0) != (divisor<0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        while dividend>=divisor:
            CQ=1
            current_divisor=divisor

            while current_divisor+current_divisor<=dividend:
                current_divisor+=current_divisor
                CQ+=CQ

            dividend-=current_divisor
            quotient+=CQ    

        if negative:
            quotient= -quotient
            # return qu

        return quotient

        