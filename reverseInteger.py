# -*- coding: utf-8 -*-
'''
# Created on May-15-20 14:49
# reverseInteger.py
# @author: exfocus
# @contact: kula147@163.com
# @version: python 2.7.15 64-bit
'''
"""
# @Problem: Given a 32-bit signed integer, reverse digits of an integer.
    Example 1: Input: 123   Output: 321
    Example 2: Input: -123  Output: -321
    Example 3: Input: 120   Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit 
signed integer range: [−2 31,  2 31  −1]. or the purpose of this problem, assume that your 
function returns 0 when the reversed integer overflows.
"""

"""
问题描述：
思路：如提示所述，处理的数字是 在32位有符号整数范围。那么需要考虑反向完的整数溢出，返回结果为0的情况。32位有符号的二进制补码[10000…000，01111…1111],
换算成10进制[-2147483648,2147483647]，首先判断输入x是否在输入值域之内，最后判断输出y是否在值域之内。

"""
class Solution:
    def reverse(self,x):
        if x>2147483647 or x<-2147483648:
            return 0
        else:
            if x>0:
                sign=1
            else :
                sign=-1
            x=abs(x)
            result=0
            while x!=0:
                result=result*10+x%10
                x=x/10
            if sign*result<2147483647 and sign*result>-2147483648:
                return sign*result
            else:
                return 0



if __name__ == "__main__":
    solution=Solution()
    det=1534236469
    print solution.reverse(det)


    