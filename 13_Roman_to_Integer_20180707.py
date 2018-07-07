#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 11:07:45 2018

@author: lifanhong
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i, roman in enumerate(s):
            if roman == 'I':
                if i != len(s)-1 and (s[i+1] == 'V' or s[i+1] == 'X'):
                    num -= 1
                else:
                    num += 1
            elif roman == 'V':
                num += 5
            elif roman == 'X':
                if i != len(s)-1 and (s[i+1] == 'L' or s[i+1] == 'C'):
                    num -= 10
                else:
                    num += 10
            elif roman == 'L':
                num += 50
            elif roman == 'C':
                if i != len(s)-1 and (s[i+1] == 'D' or s[i+1] == 'M'):
                    num -= 100
                else:
                    num += 100
            elif roman == 'D':
                num += 500
            elif roman == 'M':
                num += 1000
        return num