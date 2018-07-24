#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:22:43 2018

@author: lifanhong
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        tran = dict()
        out = ""
        for i, char in enumerate(s):
            if char not in tran:
                tran[char] = t[i]
            out += tran[char]
        return True if out == t else False
        