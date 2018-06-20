#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 04:41:51 2018

@author: lifanhong
"""
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x = min(rec1[2],rec2[2]) - max(rec1[0],rec2[0])
        y = min(rec1[3],rec2[3]) - max(rec1[1],rec2[1])
        return True if x > 0 and y > 0 else False