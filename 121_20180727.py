#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:29:45 2018

@author: lifanhong
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi = 2**31
        ma = 0
        for p in prices:
            if p < mi:
                mi = p
            elif p - mi > ma:
                ma = p - mi
        return ma

print(Solution().maxProfit([7,1,5,3,6,4]))