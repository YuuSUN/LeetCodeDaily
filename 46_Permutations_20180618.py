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
                child = nums[:i] + nums[i+1:]
                p1 = self.permute(child)
                for j, itemj in enumerate(p1):
                    temp = itemj
                    temp.append(itemi)
                    output.append(temp)
            return output


print(Solution().permute([1,2,3,4]))