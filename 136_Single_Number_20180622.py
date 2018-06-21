#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 23:04:27 2018

@author: lifanhong
"""
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appear = dict()
        for item in nums:
            if item in appear:
                del appear[item]
            else:
                appear[item] = 1
        for key in appear.keys():
            return key

print(Solution().singleNumber([4,1,2,1,2]))