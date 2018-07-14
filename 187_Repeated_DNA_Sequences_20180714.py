#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 21:42:30 2018

@author: lifanhong
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        se = dict()
        out = []
        for i in range(len(s) - 9):
            if s[i:i+10] not in se:
                se[s[i:i+10]] = 1
            elif s[i:i+10] not in out:
                out.append(s[i:i+10])
        return out
    
print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))