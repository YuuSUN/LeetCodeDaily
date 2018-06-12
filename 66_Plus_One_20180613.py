#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 00:57:36 2018

@author: lifanhong
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in range(len(digits)):
            number = number * 10 + digits[i]
        number += 1
        output = []
        for i in range(len(str(number))):
            output.append(int(str(number)[i]))
        return output