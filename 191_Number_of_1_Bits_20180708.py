#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 13:09:21 2018

@author: lifanhong
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hw = 0
        while n > 0:
            if n % 2 == 1:
                hw += 1
            n //= 2
        return hw
    
print(Solution().hammingWeight(128))