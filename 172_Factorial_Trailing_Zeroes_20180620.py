#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 23:30:26 2018

@author: lifanhong
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            output = n // 5 + self.trailingZeroes(n // 5)
            return output
        
print(Solution().trailingZeroes(23))