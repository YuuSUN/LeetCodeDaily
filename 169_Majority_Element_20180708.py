#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 13:44:16 2018

@author: lifanhong
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for n in d.keys():
            print(n)
            if d[n] > len(nums):
                return n
            
Solution().majorityElement([3,2,3])