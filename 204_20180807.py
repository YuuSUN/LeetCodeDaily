#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:45:48 2018

@author: lifanhong
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        nums = [1] * n
        nums[0],nums[1] = 0,0
        for i in range(2, int(n**0.5)+1):
            if nums[i] != 0:
                nums[i*i:n:i] = [0] * len(nums[i*i:n:i])
        return sum(nums)
    
    