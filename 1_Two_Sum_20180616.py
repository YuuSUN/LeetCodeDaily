#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 00:50:04 2018

@author: lifanhong
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        find_num = {} 
        for i, num in enumerate(nums):
            if num not in find_num:
                find_num[num] = [i]
            else:
                find_num[num].append(i)
        for i, num in enumerate(nums):
            if target == 2 * num and len(find_num[num]) == 2:
                return find_num[num]
            elif target - num in find_num and find_num[target - num][0] != i:
                return [i, find_num[target - num][0]]
            else:
                continue