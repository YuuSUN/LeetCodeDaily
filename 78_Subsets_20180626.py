#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 22:39:12 2018

@author: lifanhong

"""
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        for i,item in enumerate(nums):
            temp = []
            for j in subsets:
                temp.append(j + [item])
            subsets += temp
        return subsets
        
nums = [1,2,3,4]
k = Solution().subsets(nums)
print(k)