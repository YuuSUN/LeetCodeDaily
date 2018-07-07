#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 10:13:25 2018

@author: lifanhong
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        output = str(x)[::-1]
        if output[-1] == '-':
            output = '-' + output[:-1]
        return int(output) if -2**31 <= int(output) <= 2**31-1 else 0