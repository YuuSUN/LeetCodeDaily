#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 01:58:42 2018

@author: lifanhong

The length of both num1 and num2 is < 110. —— what's the point of this?

test case:
    when output = "0"
    3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2) + 2)
        output = ""
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp = int(num1[-1-i]) * int(num2[-1-j])
                result[-1-i-j] += temp % 10
                if temp >= 10:
                    result[-2-i-j] += temp // 10 
        for k in range(len(result)):
            if result[-1-k] >= 10:
                result[-2-k] += result[-1-k] // 10
                result[-1-k] = result[-1-k] % 10
        #print(result)
        for digit in result:
            if digit != 0 or output != "" :
                output += str(digit)
        if output == "":
            output = "0"
        return output
        
print(Solution().multiply("3141592653589793238462643383279502884197169399375105820974944592","2718281828459045235360287471352662497757247093699959574966967627"))