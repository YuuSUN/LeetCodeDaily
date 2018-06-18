#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 23:28:53 2018

@author: lifanhong
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return([nums])
        else:
            output = []
            for i, itemi in enumerate(nums):
                p1 = self.permute(nums[:i] + nums[i+1:])
                for j, itemj in enumerate(p1):
                    itemj.append(itemi)
                    output.append(itemj)
            return output


print(Solution().permute([1,2,3,4]))