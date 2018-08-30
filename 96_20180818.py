#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 18:24:25 2018

@author: lifanhong
"""

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        nt = [0] * (n+1)
        nt[0] = 1
        nt[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1): #第j个
                nt[i] += nt[j-1] * nt[i-j]
        return nt[i]
    
print(Solution().numTrees(3))